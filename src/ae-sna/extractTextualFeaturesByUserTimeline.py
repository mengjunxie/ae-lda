"""
=====================================================================
extract textural features
=====================================================================
"""
print __doc__

import logging
import os
import csv
import re
import numpy as np
import collections
from misc.util import *

# Display progress logs on stdout
logging.basicConfig(level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s]: %(message)s')

logger = logging.getLogger(__name__)


url_re = re.compile(r"(http.*?|www\..*?)\s+",re.I)
pronoun_re = re.compile(r'(all|another|any|anybody|anyone|anything|both|each|either|everybody|everyone|everything|few|he|her|hers|herself|him|himself|his|I|it|its|itself|many|me|mine|my|myself|neither|no one|nobody|none|nothing|one|others|our|ours|ourselves|she|some|somebody|someone|something|that|their|theirs|them|themselves|these|they|this|us|we|what|which|who|whom|whose|you|your|yours|yourself|yourselves)', re.I)
negative_re = re.compile(r'(not|no|donot|doesn\'t|don\'t|have\'t|has\'t|cannot|can\'t)')
hashtag_re = re.compile(r'(#.*?)\s+',re.I)
reply_re = re.compile(r'(@.*?)\s+',re.I)


def number_of_reply_tag(text):
    s = 0
    for m in reply_re.findall(" %s "%text):
        s += len(str(m).strip().split('@')) - 1

    return s

def number_of_hashtag(text):
    s = 0
    for m in hashtag_re.findall(" %s "%text):
        s += len(str(m).strip().split('#')) - 1

    return s

def number_of_negative(text):
    return len(negative_re.findall(text))

def number_of_pronouns(text):
    return len(pronoun_re.findall(text))

def number_of_urls(text):
    s = len(url_re.findall(" %s "%text))
    return s

drug_use_bows_regex = {}
drug_use_bows_f = open(os.path.abspath("../../misc/DRUG-USE-BOWs.txt"), 'r')

for line in drug_use_bows_f:
    if line.strip() == "":
        continue

    ngram_index,regex_s = line.strip().split(',')
    drug_use_bows_regex[int(ngram_index)] = re.compile(r"(%s)"%regex_s,re.I)


keylist = drug_use_bows_regex.keys()
keylist.sort()

def bows_count(text):

    fv = []
    for key in keylist:
        fv.append(len(drug_use_bows_regex[key].findall(text)))

    return fv

drug_names = ['Avastin',
              'Bevacizumab',
              'Melphalan',
              'ALKERAN',
              'Rupatadin',
              'Rupafin',
              'Urtimed',
              'Tamoxifen',
              'Nolvadex',
              'Taxotere',
              'Docetaxel']

drug_names_regex = "(%s)"%("|".join(drug_names))

drug_names_re = re.compile(drug_names_regex, re.I)

def drug_count(text):
    return len(drug_names_re.findall(text))


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


def extract_textural_features(inputFile):
    tweets_f = open(os.path.abspath(inputFile), 'r')

    subjectFVs = []


    for tweet_text in tweets_f:
        if tweet_text.strip() == '':
            continue

        subjectFV = []



        subjectFV.append(number_of_reply_tag(tweet_text))
        subjectFV.append(number_of_hashtag(tweet_text))
        subjectFV.append(number_of_negative(tweet_text))
        subjectFV.append(number_of_pronouns(tweet_text))
        subjectFV.append(number_of_urls(tweet_text))
        subjectFV.append(drug_count(tweet_text))
        subjectFV.extend(bows_count(tweet_text))

        subjectFVs.append(subjectFV)

    return np.sum(subjectFVs,axis=0)

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

def main():
    data_folder = "../../result/twitter-user-timeline-by-drug/R/"

    input_files = os.listdir(data_folder)

    uIds,subjects = get_subjects()

    subjectFeatureMatrix = []


    for input_file in input_files:
        if not input_file.endswith('.txt'):
            continue

        if input_file.endswith('processed.txt'):
            continue

        m = re.match("(\d+).*?txt",input_file)

        userId = m.group(1)

        subject = [userId,subjects[userId].drugUseFlag,subjects[userId].sideEffectsFlag]

    print len(subjectFeatureMatrix)


    #np.save("../../result/classification-features/textural-features-ae.npy", subjectFeatureMatrix)



    return


if __name__ == '__main__':
    main()