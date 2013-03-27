"""
=====================================================================
extract user twitter timeline into a text file
=====================================================================
"""
print __doc__

import logging
import os
#import argparse
#from time import time
from lxml import etree
#import urllib2,urllib,json
import operator
import cld
import unicodedata
import string
import re
#from misc import AlchemyAPI
from misc.util import *
import csv

# Display progress logs on stdout
logging.basicConfig(level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s]: %(message)s')

logger = logging.getLogger(__name__)

#start = time()

STRIP_NON_EN = True
STRIP_RT = True
COMBINE_MULTIPLE_POINTS = True
ALL_TWEETS = False
OUT='DRUG'
DRUG_USE_ONLY = False

N_PRE = 0
N_AFTER = 0

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

    #print collections.Counter(userIds)
    #quit()

    return userIds,subjects


uIds,subjects = get_subjects()


class Tweet(object):

    def __init__(self, tweet_id,user_id, timestamp, created_at, tweet_text):
        '''
        '''
        self.tweet_id = tweet_id
        self.user_id = user_id
        self.timestamp = timestamp
        self.tweet_text = tweet_text
        self.created_at = created_at


def remove_unicode_chr(data):
    #print type(data)
    return ''.join(x for x in unicodedata.normalize('NFKD', data) if x in string.printable)

def process_tweet_xml_elm(tweet_xml_elm):
    tweet_text = etree.tostring(tweet_xml_elm.find("tweet_text"), method='text', encoding="UTF-8")
    tweet_text =  remove_unicode_chr(smart_unicode(tweet_text))

    tweet_id = tweet_xml_elm.find("tweet_id").text
    timestamp = tweet_xml_elm.find("timestamp").text
    created_at = tweet_xml_elm.find("created_at").text
    user_id = tweet_xml_elm.find("user_id").text

    langName, lang, isReliable, textBytesFound, details =  cld.detect(tweet_text, pickSummaryLanguage=True, removeWeakMatches=False)

    #STRIP_NON_EN:

    if (STRIP_NON_EN and lang != 'en') or (STRIP_RT and tweet_text.upper().startswith("RT")):
        return lang,None

    return lang,Tweet(tweet_id,user_id,timestamp,created_at,tweet_text)


def process_user_timeline(inputFile, outFolder):

    tweetIds = []
    inputFile = "%s/%s"%(outFolder,inputFile)
    #if not os.path.exists(outFolder):
    #    os.mkdir(outFolder)

    parser = etree.XMLParser(encoding="UTF-8", ns_clean=True,recover=True)

    drug_root = etree.parse(inputFile,parser=parser)

    #print drugName
    outFolder = "%s/%s"%(outFolder,OUT)

    if not os.path.exists(outFolder):
        os.mkdir(outFolder)

    drug_regex_string = ""
    for drug_name in drug_root.xpath("//drug-name"):
        print drug_name.text
        if drug_regex_string == "":
            drug_regex_string = drug_name.text
        else:
            drug_regex_string = "%s|%s"%(drug_regex_string,drug_name.text)

    drug_regex_string = "(%s)"%drug_regex_string

    for user_timeline in drug_root.xpath("//user-timeline"):

        userId = user_timeline.get("user_id")

        if DRUG_USE_ONLY and (userId not in subjects or subjects[userId].drugUseFlag == 0):
            continue


        lang_dict = {}

        user_tweets = []

        #numOfRT = 0

        for tweet_xml_elm in user_timeline.findall("tweet"):

            lang,tweet = process_tweet_xml_elm(tweet_xml_elm)

            if lang not in lang_dict:
                lang_dict[lang] = 1
            else:
                lang_dict[lang] += 1

            if tweet:
                user_tweets.append(tweet)

        l = len(user_tweets)

        nL = len(lang_dict)

        if l == 0 or nL == 0:
            continue

        lang = max(lang_dict.iteritems(), key=operator.itemgetter(1))[0]

        if lang != "en":
            continue

        user_tweets.sort(key=lambda x: x.timestamp, reverse=False)

        if ALL_TWEETS:
            out_file = '%s/%s.A.txt'%(outFolder,userId)
            user_timeline_f = open(out_file, 'w')


            for tweet in user_tweets:
                if tweet.tweet_id in tweetIds:
                    #print "ddd"
                    continue

                tweetIds.append(tweet.tweet_id)
                print >> user_timeline_f, tweet.tweet_text

            user_timeline_f.close()
        else:
            e_user_tweets = []

            for index,user_tweet in enumerate(user_tweets):
                if re.search(drug_regex_string,user_tweet.tweet_text,re.I):
                    #print user_tweet.timestamp,user_tweet.created_at,user_tweet.tweet_text
                    tweets = []

                    s = index - N_PRE
                    if s < 0:
                        s = 0

                    for p_index in range(s,index):
                        tweets.append(user_tweets[p_index])

                    f = index + N_AFTER + 1

                    if f > l:
                        f = l

                    for a_index in range(index,f):
                        tweets.append(user_tweets[a_index])

                    e_user_tweets.append(tweets)

            l = len(e_user_tweets)

            if l == 0:
                continue

            if COMBINE_MULTIPLE_POINTS:

                out_file = '%s/%s.%s.txt'%(outFolder,userId,OUT)

                user_timeline_f = open(out_file, 'w')

                for index,user_tweets in enumerate(e_user_tweets):
                    for tweet in user_tweets:
                        if tweet.tweet_id in tweetIds:
                            #print "ddd"
                            continue

                        tweetIds.append(tweet.tweet_id)
                        print >> user_timeline_f, tweet.tweet_text

                user_timeline_f.close()

            else:


                for index,user_tweets in enumerate(e_user_tweets):

                    out_file = '%s/%s.%s.%d.txt'%(outFolder,userId,OUT,index)

                    user_timeline_f = open(out_file, 'w')

                    for tweet in user_tweets:
                        print >> user_timeline_f, tweet.tweet_text

                    user_timeline_f.close()


    return len(tweetIds)


def main():
    data_folder = "../../result/twitter-user-timeline-by-drug/"

    input_files = os.listdir(data_folder)

    cnt = 0
    for input_file in input_files:
        if not input_file.endswith('.xml'):
            continue
        cnt += process_user_timeline(input_file, data_folder)

    print cnt
    return


if __name__ == '__main__':
    main()