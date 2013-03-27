"""
=====================================================================
http://clinicaltrials.gov/ct2/search/browse?brwse=intr_alpha_all
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


f = urllib2.urlopen('http://clinicaltrials.gov/ct2/search/browse?brwse=intr_alpha_all')

contents = f.read()

drugs_r = re.findall(r"<a.*?href=\"(/ct2/results\?intr=.*?)\">(.*)</a>", contents)

drugs = []

for url, drug in drugs_r:

    drugs.append(drug)

drugs_f = open('%s/drugs.dump'%result_folder, 'w')
drugs_f.write(base64.b64encode(pickle.dumps(drugs)))
drugs_f.close()