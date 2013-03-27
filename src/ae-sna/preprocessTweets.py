"""
=====================================================================
extract user twitter timeline into a text file
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



#pronoun_re = re.compile(r'(all|another|any|anybody|anyone|anything|both|each|either|everybody|everyone|everything|few|he|her|hers|herself|him|himself|his|I|it|its|itself|many|me|mine|my|myself|neither|no one|nobody|none|nothing|one|others|our|ours|ourselves|she|some|somebody|someone|something|that|their|theirs|them|themselves|these|they|this|us|we|what|which|who|whom|whose|you|your|yours|yourself|yourselves)', re.I)
#negative_re = re.compile(r'(not|no|donot|doesn\'t|don\'t|have\'t|has\'t|cannot|can\'t)')
#hashtag_re = re.compile(r'(#.*?)\s+',re.I)

filtered_words_f = open(os.path.abspath("../../misc/WORDS-FILTER.txt"), 'r')

filtered_words = []
for line in filtered_words_f:
    if line.strip() == "":
        continue

    filtered_words.append(line.strip())

filtered_words_re = re.compile(r"(%s)\s+"%'|'.join(filtered_words),re.I)
def strip_filtered_words(text):
    return filtered_words_re.sub('\1',' %s '%text)

reply_tag_re = re.compile(r'(@.*?)\s+',re.I)
def strip_reply_tags(text):
    return reply_tag_re.sub('\1',' %s '%text)

url_re = re.compile(r"(http.*?|www\..*?|bit\.ly.*?)\s+",re.I)
def strip_urls(text):
    return url_re.sub('\1',' %s '%text)


def preprocess_tweets(inputFile):

    tweets_f = open(os.path.abspath(inputFile), 'r')

    tweets_processed_f = open(os.path.abspath("%s.processed.txt"%inputFile), 'w')

    for tweet_text in tweets_f:
        if tweet_text.strip() == '':
            continue

        tweet_text = strip_urls(tweet_text)
        #tweet_text = strip_reply_tags(tweet_text)
        #tweet_text = strip_filtered_words(tweet_text)

        print >> tweets_processed_f, tweet_text.strip()

    tweets_processed_f.close()
    tweets_f.close()

    return

def main():
    data_folder = "../../result/twitter-user-timeline-by-drug/DRUG/"

    input_files = os.listdir(data_folder)

    for input_file in input_files:
        if not input_file.endswith('.txt'):
            continue

        preprocess_tweets("%s/%s"%(data_folder,input_file))

    return


if __name__ == '__main__':
    main()