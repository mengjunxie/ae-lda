"""
=====================================================================
extract interventions
=====================================================================
"""
print __doc__

import re
import logging
import urllib2
import os
import codecs
from copy import deepcopy
from lxml import etree
import time
import base64
import pickle

# Display progress logs on stdout
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] [%(levelname)s]: %(message)s')
                    
logger = logging.getLogger(__name__)

study_drugs_xml_file = os.path.abspath('../../../../result/clinicaltrails.gov/study_drugs.xml')

study_drugs_root = etree.parse(study_drugs_xml_file)

studies = study_drugs_root.findall('study')

logger.info("number of cancer studies: %d"%len(studies))

drugs = []
a = 0
for study in studies:
    study_drugs = study.findall('drug')

    if len(study_drugs) > 0:
        a += 1
    else:
        continue

    for study_drug in study_drugs:
        drugs.append(study_drug.text)

logger.info("number of cancer studies using drugs: %d"%a)
logger.info("number of drugs: %d"%len(drugs))

logger.info("number of unique drugs: %d"%len(set(drugs)))

result_folder = os.path.abspath("../../../../result/clinicaltrails.gov/")



drugs_f = open('%s/study_drugs.dump'%result_folder, 'w')
drugs_f.write(base64.b64encode(pickle.dumps(set(drugs))))
drugs_f.close()

drugs_txt_f = codecs.open('%s/study_drugs.txt'%result_folder, encoding='utf-8', mode='w')
for drug in set(drugs):
    print >> drugs_txt_f, drug
drugs_txt_f.close()