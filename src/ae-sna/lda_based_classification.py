"""
=====================================================================
test lda in gensim
=====================================================================
"""
print __doc__

import re, os, csv, base64, pickle

from scipy import interp
import pylab as pl
from sklearn.metrics import roc_curve, auc

from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from svm.util import *
from svm import feature_selection
from svm import sampling
from svm import scaling

from sklearn.svm import SVC
from gensim import corpora, models, similarities
import logging
import nltk

from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet as wn

lda_num_topics = 100
lsi_num_topics = 100
rp_num_topics = 300

wordNetLemmatizer = WordNetLemmatizer()

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR)

logger = logging.getLogger(__name__)

class Tweet(object):

    def __init__(self, user_id, timestamp, created_at, tweet_text):
        '''
        '''
        self.user_id = user_id
        self.timestamp = timestamp
        self.tweet_text = tweet_text
        self.created_at = created_at

class Subject(object):

    def __init__(self, userId, drugUseFlag, sideEffectsFlag):
        '''
        '''
        self.userId = userId
        self.drugUseFlag = drugUseFlag
        self.sideEffectsFlag = sideEffectsFlag

    def __repr__( self ):
        return "userId: %s; drugUseFlag: %s; sideEffectsFlag: %s;"%(self.userId,self.drugUseFlag,self.sideEffectsFlag)


def get_subjects():
    subjectLabels = csv.reader(open("../../misc/subjectLabels.csv", "rU"))

    subjects = {}
    l=lambda i: 1 if int(i) > 0 else 0

    userIds = []
    for row in subjectLabels:
        userId = row[0]
        drugUseFlag = l(row[1])
        sideEffectsFlag = l(row[2])
        subjects[userId] = Subject(userId,drugUseFlag,sideEffectsFlag)

        userIds.append(userId)

    return userIds,subjects



def loadstopwords():

    filtered_words_f = open(os.path.abspath("../../misc/mallet-stopwords-en.txt"), 'r')

    filtered_words = []
    for line in filtered_words_f:
        if line.strip() == "":
            continue

        filtered_words.append(line.strip())

    return filtered_words

reply_tag_re = re.compile(r'(@.*?)\s+',re.I)
def strip_reply_tags(text):
    return reply_tag_re.sub('\1',' %s '%text)

url_re = re.compile(r"(http.*?|www\..*?|bit\.ly.*?)\s+",re.I)
def strip_urls(text):
    return url_re.sub('\1',' %s '%text)

def mreplace(s, chars, replace_to = ''):

    for char in chars:
        s = str(s).replace(char,replace_to)

    return s

#preprocess indiviudal tweet, such as removing the reply tag, the url, etc.
def preprocess_tweet(tweet):
    tweet = strip_urls(strip_reply_tags(tweet))

    return tweet.lower()


#symbols that need to be removed when appearing as part of other words
replace_symbols = ['\x01','!',".","?","$","#", '1','2','0','3','4','5','6','7','8','9']

#symbols that need to be removed when appearing as a word
single_letter_symbols = ['/','\'']
#single_letter_symbols.extend(replace_symbols)

stopwords = loadstopwords() #set('for a of the and to in that was is'.split())
stopwords.extend(nltk.corpus.stopwords.words('english'))

stopwords.extend(single_letter_symbols)

twitter_stopwords = ['rt','i\'m','it\'s','that\'s','don\'t','i\'ve','n\'t','ly','\'m','--', '||', 'll', 'ff']
stopwords.extend(twitter_stopwords)

#Anything else with be None, and will be removed from the corpus
#morphy_tag = {'NN.*':wn.NOUN,
#              'JJ.*':wn.ADJ,
#              'VB.*':wn.VERB,
#              'RB.*':wn.ADV}

morphy_tag = {'NN':wn.NOUN,
              'JJ':wn.ADJ,
              'VB':wn.VERB,
              'RB':wn.ADV}

drugs = ['avastin','bevacizumab','melphalan','alkeran','rupatadin','rupafin','urtimed','tamoxifen','nolvadex','taxotere','docetaxel']

def preprocess_and_tokenize_document(document):

    tokenized_document = []

    #lancasterStemmer = nltk.LancasterStemmer()
    #porterStemmer = nltk.PorterStemmer()

    for line in document:

        tokenized_line = nltk.word_tokenize(line)
        processed_tokenized_line = []

        tagged_line = nltk.pos_tag(tokenized_line)


        for w in tagged_line:
            word = w[0]
            tag = w[1]
            s_tag = tag[:2]

            if word in drugs:
                word = 'drug'
            else:
                wnWord = wn.synsets(word)
                if len(wnWord) > 0 and s_tag in morphy_tag:
                    processed_tokenized_line.append(wordNetLemmatizer.lemmatize(word, morphy_tag[s_tag]))
            #print(w + "===" + wordNetLemmatizer.lemmatize(w) + "===" + porterStemmer.stem(w))

        tokenized_document.extend(tokenized_line)


    tokenized_document = [word for word in [mreplace(word, replace_symbols) for word in tokenized_document if word not in single_letter_symbols and len(word) > 1] if len(word) > 1 and word not in stopwords]

    return tokenized_document



def preprocess_tokenized_documents(tokenized_documents, tokens_once = None):

    #tokens_once is only collected on training set, for testing set, use the tokens_once from the training set.
    if tokens_once == None:
        all_tokens = sum(tokenized_documents, [])
        tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)

    documents = []
    for tokenized_document in tokenized_documents:
        # first, we need remove words that only appeared once...
        # and we replace the drug name to the word drug... so that we don't really care the name of the drugs...
        documents.append([word for word in tokenized_document if word not in list(tokens_once)])


    return tokens_once, documents


def load_corpus():
    data_folder = "../../result/twitter-user-timeline-by-drug/DRUG/"

    input_files = os.listdir(data_folder)

    uIds,subjects = get_subjects()

    documents = []

    instances = []

    for input_file in input_files:

        if not input_file.endswith('.txt'):
            continue

        m = re.match("(\d+).*?txt",input_file)

        userId = m.group(1)

        if userId not in subjects:
            continue

        #subject = [userId,subjects[userId].drugUseFlag,subjects[userId].sideEffectsFlag]

        txt_f = open(os.path.abspath("%s%s"%(data_folder,input_file)), 'r')

        #tweets is a document collection of tweets
        tweets = []
        for tweet in txt_f:
            if tweet.rstrip() == '':
                continue
            tweets.append(preprocess_tweet(tweet))

        document = preprocess_and_tokenize_document(tweets)

        documents.append(document)
        instances.append(subjects[userId])

    return instances,documents


#train the lda on D_train and generate topic distribution of each document as features
def getFeatureMatrixFromLDA(y_train, y_test, D_train, D_test, all = True, mode=None):

    num_topics = 20

    D_train_corpus = None
    D_test_corpus = None

    dictionary = None
    if mode != "positive_only":
        if all == True:
            All_D = []
            All_D.extend(D_train)
            All_D.extend(D_test)

            tokens_once, D_tokenized = preprocess_tokenized_documents(All_D)
            dictionary = corpora.Dictionary(D_tokenized)

            corpus = [dictionary.doc2bow(document) for document in All_D]

            _, D_train_tokenized = preprocess_tokenized_documents(D_train, tokens_once)
            _, D_test_tokenized = preprocess_tokenized_documents(D_test, tokens_once)

            D_train_corpus = [dictionary.doc2bow(document) for document in D_train_tokenized]
            D_test_corpus = [dictionary.doc2bow(document) for document in D_test_tokenized]
        else:
            tokens_once, D_train_tokenized = preprocess_tokenized_documents(D_train)
            _, D_test_tokenized = preprocess_tokenized_documents(D_test, tokens_once)

            dictionary = corpora.Dictionary(D_train_tokenized)

            D_train_corpus = corpus = [dictionary.doc2bow(document) for document in D_train_tokenized]
            D_test_corpus = [dictionary.doc2bow(document) for document in D_test_tokenized]
    elif mode == "positive_only":
        if all == True:
            p_y_train = np.flatnonzero(y_train == 1)
            p_y_test = np.flatnonzero(y_test == 1)

            D = []
            D.extend(D_train[p_y_train])
            D.extend(D_test[p_y_test])

            tokens_once, D_tokenized = preprocess_tokenized_documents(D)
            dictionary = corpora.Dictionary(D_tokenized)

            corpus = [dictionary.doc2bow(document) for document in D]

            _, D_train_tokenized = preprocess_tokenized_documents(D_train, tokens_once)
            _, D_test_tokenized = preprocess_tokenized_documents(D_test, tokens_once)

            D_train_corpus = [dictionary.doc2bow(document) for document in D_train_tokenized]
            D_test_corpus = [dictionary.doc2bow(document) for document in D_test_tokenized]
        else:
            p_y_train = np.flatnonzero(y_train == 1)

            D = D_train[p_y_train]

            tokens_once, D_tokenized = preprocess_tokenized_documents(D)
            dictionary = corpora.Dictionary(D_tokenized)

            corpus = [dictionary.doc2bow(document) for document in D]

            _, D_train_tokenized = preprocess_tokenized_documents(D_train, tokens_once)
            _, D_test_tokenized = preprocess_tokenized_documents(D_test, tokens_once)

            D_train_corpus = [dictionary.doc2bow(document) for document in D_train_tokenized]
            D_test_corpus = [dictionary.doc2bow(document) for document in D_test_tokenized]


    lda = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics, update_every=1, chunksize=10000, passes=20)

    #lda.show_topics(topics=-1)

    X_train = []

    for vec in D_train_corpus:
        featureVector = np.zeros(20)

        for tId, tp in lda[vec]:
            featureVector[tId] = tp

        X_train.append(featureVector)

    X_test = []

    for vec in D_test_corpus:
        featureVector = np.zeros(20)

        for tId, tp in lda[vec]:
            featureVector[tId] = tp

        X_test.append(featureVector)

    return lda, np.array(X_train), np.array(X_test)


# SVM setup
# Set the parameters by cross-validation
#tuned_parameters = [{'kernel': ['linear'], 'C': [1, 10, 100, 1000, 10000]}]

# Set the parameters by cross-validation
tuned_parameters = [{'kernel': ['rbf'], 'gamma': range_log2based(1, -13, -2),
                     'C': range_log2based(-2, 11, 2)}]#,
                    #{'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]

scores = [
    ('precision', precision_score),
    ('recall', recall_score),
    ]

score_name = 'recall'
score_func = recall_score

fselector = feature_selection.FeatureSelector(mode='fscore', params={'tuned_parameters': tuned_parameters, 'min_num_of_features': 2})

result_folder = os.path.abspath("../../result/lda")

def getBoWCorpus(documents):
    dictionary = corpora.Dictionary(documents)
    bow_corpus = [dictionary.doc2bow(document) for document in documents]

    return bow_corpus, dictionary

def extract_lda_features(bow_corpus, dictionary):

    lda = models.ldamodel.LdaModel(corpus=bow_corpus, id2word=dictionary, num_topics=lda_num_topics, update_every=1, chunksize=10000, passes=20)

    lda_corpus = lda[bow_corpus]

    X = []
    for doc in lda_corpus:
        featureVector = np.zeros(lda_num_topics)

        for tId, tp in doc:
            featureVector[tId] = tp

        X.append(featureVector)

    return np.array(X)

def extract_log_entropy_features(bow_corpus, dictionary):

    tfidf = models.tfidfmodel.TfidfModel(bow_corpus, normalize=True)

    tfidf_corpus = tfidf[bow_corpus]

    logentropy = models.logentropy_model.LogEntropyModel(corpus=tfidf_corpus,id2word=dictionary)

    logentropy_corpus = logentropy[bow_corpus]

    X = []

    max = 0
    for doc in logentropy_corpus:
        for tId, tp in doc:
            if tId > max:
                max = tId

    for doc in logentropy_corpus:

        featureVector = np.zeros(max + 1)

        for tId, tp in doc:
            featureVector[tId] = tp

        X.append(featureVector)

    return np.array(X)

def extract_rp_features(bow_corpus, dictionary):

    tfidf = models.tfidfmodel.TfidfModel(bow_corpus, normalize=True)

    tfidf_corpus = tfidf[bow_corpus]

    rp = models.rpmodel.RpModel(corpus=tfidf_corpus,id2word=dictionary,num_topics=rp_num_topics)

    rp_corpus = rp[tfidf_corpus]

    X = []

    max = 0
    for doc in rp_corpus:
        for tId, tp in doc:
            if tId > max:
                max = tId

    for doc in rp_corpus:
        featureVector = np.zeros(max + 1)

        for tId, tp in doc:
            featureVector[tId] = tp

        X.append(featureVector)

    return np.array(X)


def extract_lsi_features(bow_corpus, dictionary):
    tfidf = models.tfidfmodel.TfidfModel(bow_corpus, normalize=True)

    tfidf_corpus = tfidf[bow_corpus]

    lsi = models.LsiModel(tfidf_corpus, id2word=dictionary, num_topics=lsi_num_topics)

    lsi_corpus = lsi[tfidf_corpus]

    X = []
    for doc in lsi_corpus:

        featureVector = np.zeros(lda_num_topics)

        for tId, tp in doc:
            featureVector[tId] = tp

        X.append(featureVector)

    return np.array(X)


def main():
    n_bootstraps = 100

    instances,documents = load_corpus()

    y_o = np.array([subject.drugUseFlag for subject in instances])

    bow_corpus, dictionary = getBoWCorpus(documents)

    X_rp = extract_rp_features(bow_corpus, dictionary)
    X_lda = extract_lda_features(bow_corpus, dictionary)
    X_log_entropy = extract_log_entropy_features(bow_corpus, dictionary)
    X_lsi = extract_lsi_features(bow_corpus, dictionary)

    X_raw = np.append(X_rp, X_log_entropy, axis=1)
    X_raw = np.append(X_raw, X_lda, axis=1)
    X_raw = np.append(X_raw, X_lsi, axis=1)
    # get rid of features that are zero-vectors
    X_o = []

    index_mapping = {}
    cnt = 0
    for i, x in enumerate(X_raw.transpose()):
        zeros = np.zeros(len(x))
        if not np.array_equal(x, zeros):
            X_o.append(x)
            index_mapping[i] = cnt
        cnt += 1

    X_o = np.array(X_o).transpose()
    scaler = scaling.Scaler()
    scaler.fit(X_o)

    X_o = scaler.transform(X_o)


    downSampling = sampling.BalancedDownSampling(y_o, n_bootstraps=n_bootstraps, random_state=None)

    mean_tpr = 0.0
    mean_fpr = np.linspace(0, 1, 100)
    all_tpr = []
    all_acc = []

    result = {}

    cnt = 0

    for i, sample_indices in enumerate(downSampling):

        y = y_o[sample_indices]
        X = X_o[sample_indices]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1.0/10.0, random_state=0)

        fselected = fselector.select(X_train, y_train)

        print(fselected)

        X_train = X_train[:, fselected.best_features]
        X_test = X_test[:, fselected.best_features]

        print("# Tuning hyper-parameters for %s" % score_name)

        clf = GridSearchCV(SVC(C=1, probability=True), tuned_parameters, score_func=score_func)
        clf.fit(X_train, y_train, cv=5)

        print("Best parameters set found on development set: %s" % clf.best_estimator_)
        print("==========")

        clf = clf.best_estimator_

        y_true, y_pred = y_test, clf.predict(X_test)

        probas_ = clf.predict_proba(X_test)

        acc = accuracy(y_test, y_pred)
        print("Accuracy: %s", acc)
        all_acc.append(acc)

        fpr, tpr, thresholds = roc_curve(y_test, probas_[:, 1])
        mean_tpr += interp(mean_fpr, fpr, tpr)
        mean_tpr[0] = 0.0
        roc_auc = auc(fpr, tpr)
        print("ROC_AUC: %s", roc_auc)


        cnt += 1

    pl.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6), label='Luck')

    mean_acc = np.sum(all_acc) / cnt



    print('(Mean ACC: %0.2f)' % mean_acc)
    mean_tpr /= n_bootstraps
    mean_tpr[-1] = 1.0
    mean_auc = auc(mean_fpr, mean_tpr)
    pl.plot(mean_fpr, mean_tpr, 'k--', color='red',
        label='Mean ROC (area = %0.2f)' % mean_auc, lw=2)

    #plt.text(0.8, .5, ' Mean ACC: %0.2.f' % mean_acc)
    pl.xlim([-0.05, 1.05])
    pl.ylim([-0.05, 1.05])
    pl.xlabel('False Positive Rate (FTR)')
    pl.ylabel('True Positive Rate (TPR)')
    pl.title('(Mean ACC: %0.2f)' % (mean_acc))
    pl.legend(loc="lower right")

    pl.show()

    return


if __name__ == '__main__':
    main()