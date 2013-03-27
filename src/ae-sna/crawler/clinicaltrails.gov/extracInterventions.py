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
from copy import deepcopy
from lxml import etree
import time
import base64
import pickle

# Display progress logs on stdout
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] [%(levelname)s]: %(message)s')
                    
logger = logging.getLogger(__name__)

conditions_dump_f = open(os.path.abspath("../../../../result/clinicaltrails.gov/conditions.dump"), 'r')
conditions = pickle.loads(base64.b64decode(conditions_dump_f.read()))
conditions_dump_f.close()

target_conditions = 'Cancers and Other Neoplasms'

result_folder = os.path.abspath("../../../../result/clinicaltrails.gov/xml/")

raw_xmls = os.listdir(result_folder)

total = len(raw_xmls) - 1
i = 0

start_date_range = {'start':time.strptime('May 2009', "%B %Y"),
                    'end':time.strptime('November 2010', "%B %Y")}
interventions_root = etree.Element("interventions")
#study_status_filter = ['Recruiting', 'Active, not recruiting']
for xml_file in raw_xmls:
    print "%.2f%%" % (float(i) / total * 100)
    i += 1
    root = etree.parse("%s/%s" % (result_folder, xml_file))
    #if root.find("overall_status").text not in study_status_filter:
    #    continue
    if root.find("start_date") == None:
        continue
    
    #print root.find("start_date").text
    start_date = time.strptime(root.find("start_date").text, "%B %Y")
    
    if start_date >= start_date_range['end'] or start_date <= start_date_range['start']:
        continue
    
    exist = False
    
    for condition in root.findall('condition'):
        if condition.text in conditions[target_conditions]:
            #print condition.text
            exist = True
            break
    
    if not exist:
        continue
     
    for elm in root.findall("intervention"):
        interventions_root.append(deepcopy(elm))
        #print etree.tostring(elm, pretty_print=True)
    #interventions_root.append(deepcopy(root.findall("intervention")))

interventions_xml_f = open(os.path.abspath('../../../../result/clinicaltrails.gov/interventions.xml'), 'w') 
interventions_xml_f.write(etree.tostring(interventions_root, pretty_print=True, xml_declaration=True, encoding="UTF-8"))
interventions_xml_f.close()
    
