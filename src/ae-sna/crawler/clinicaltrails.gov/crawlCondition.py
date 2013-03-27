"""
=====================================================================
http://clinicaltrials.gov/ct2/search/browse?brwse=cond_cat
=====================================================================
"""
print __doc__

import re
import logging
import urllib2
import os
import base64
import pickle

# Display progress logs on stdout
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] [%(levelname)s]: %(message)s')
                    
logger = logging.getLogger(__name__)

root_url = 'http://clinicaltrials.gov'


result_folder = os.path.abspath("../../../../result/clinicaltrails.gov/")


f = urllib2.urlopen('http://clinicaltrials.gov/ct2/search/browse?brwse=cond_cat')

contents = f.read()

categories = re.findall(r"<a.*?href=\"(/ct2/search/browse\?brwse=cond_cat_BC\d+)\">(.*)</a>", contents)

conds = {}

for url, category in categories:
    
    if category not in conds:
        conds[category] = []
                        
    f = urllib2.urlopen("%s%s"%(root_url,url))
    contents = f.read()

    conditions = re.findall(r"<a.*?href=\"(/ct2/results\?cond=.*?)\">(.*)</a>", contents)
    
    for url, condition in conditions:
        #print("%s:%s"%(category,condition))
        #print >> conditions_f, "%s:%s"%(category,condition)
        conds[category].append(condition)
    
print conds
conditions_f = open('%s/conditions.dump'%result_folder, 'w')
conditions_f.write(base64.b64encode(pickle.dumps(conds)))
conditions_f.close()