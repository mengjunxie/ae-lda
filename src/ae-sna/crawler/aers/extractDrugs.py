"""
=====================================================================
extrac Drugs
=====================================================================
"""
print __doc__

from lxml import etree
import logging
import os
import re
import MySQLdb
import base64
import pickle
#from misc.util import *

# Display progress logs on stdout
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] [%(levelname)s]: %(message)s')

logger = logging.getLogger(__name__)

# Open database connection
db = MySQLdb.connect("localhost","root","","tweet_data" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

aers_path = "../../../../data/aers/" 

aers_folder = os.path.abspath(aers_path)

aers_sgms = os.listdir(aers_folder)

total = len(aers_sgms) - 1
i = 0

drugs = []

for sgm in aers_sgms:
    print "%s: %.2f%%" % (sgm, (float(i) / total * 100))
    i += 1
    
    sgm_root = etree.parse("%s/%s" % (aers_path, sgm))
    
    for drug in sgm_root.findall('//drug'):
        #etree.tostring(drug)
        drugs.append(drug.find('medicinalproduct').text)


result_folder = os.path.abspath("../../../../result/aers/")

drugs_f = open('%s/drugs.dump'%result_folder, 'w')
drugs_f.write(base64.b64encode(pickle.dumps(set(drugs))))
drugs_f.close()