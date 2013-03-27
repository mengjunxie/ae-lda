"""
=====================================================================
tweets to sql
=====================================================================
"""
print __doc__

import logging
import os
import re
import MySQLdb

# Display progress logs on stdout
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] [%(levelname)s]: %(message)s')

logger = logging.getLogger(__name__)

twitter_data_f = open(os.path.abspath("../../../../data/twitter/tweet_data_basic.tsv"), 'r')

line = twitter_data_f.readline()

#CREATE SCHEMA `tweet_data` DEFAULT CHARACTER SET utf8 ;
# Open database connection
db = MySQLdb.connect("localhost","root","","tweet_data" )

# prepare a cursor object using cursor() method
cursor = db.cursor()



#print line
#print [column.strip() for column in line.rstrip().split('\t')]
for line in twitter_data_f:
    if len(line.rstrip()) == 0:
        continue
    #tweet_id, user_id, timestamp, time_friendly, location, tweet_text = tuple([column.strip() for column in line.rstrip().split('\t')])

    #tweet_text = re.escape(tweet_text)
    #print [column.strip() for column in line.rstrip().split('\t')]
    cursor.execute('INSERT INTO tweets (tweet_id, user_id, timestamp, time_friendly, location, tweet_text) VALUES (%s, %s, %s, %s, %s, %s)', tuple([column.strip() for column in line.rstrip().split('\t')]))

    #print insert_sql
    #quit()

print cursor.rowcount
cursor.close ()
db.commit()
db.close ()
quit()