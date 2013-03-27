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

drugs_dump_f = open(os.path.abspath("../../../../result/clinicaltrails.gov/drugs.dump"), 'r')
drugs = pickle.loads(base64.b64decode(drugs_dump_f.read()))
drugs_dump_f.close()

target_conditions = 'Cancers and Other Neoplasms'

result_folder = os.path.abspath("../../../../result/clinicaltrails.gov/xml/")

raw_xmls = os.listdir(result_folder)

total = len(raw_xmls) - 1
i = 0

start_date_range = {'start':time.strptime('May 2009', "%B %Y"),
                    'end':time.strptime('November 2010', "%B %Y")}

studies = etree.Element("studies")
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

    nct_id = root.find("//nct_id").text
    study = etree.Element("study", nct_id=nct_id)

    intervention_names = []
    drug_keywords = []

    for elm in root.findall("intervention"):

        intervention_type = elm.find("intervention_type").text

        #print intervention_type
        if intervention_type != 'Drug':
            continue

        intervention_names.append(elm.find("intervention_name").text)

        for o_elm in elm.findall("other_name"):
            #print o_elm.text
            intervention_names.append(o_elm.text)


    for name in intervention_names:
        #for drug in drugs:
            #if drug in name:
        drug_keywords.append(name)

    #print intervention_names
    #print drug_keywords

    for drug_keyword in set(drug_keywords):
        drug_keyword_elm = etree.Element("drug")
        drug_keyword_elm.text = drug_keyword

        study.append(deepcopy(drug_keyword_elm))

        #print etree.tostring(drug_keyword_elm)

        #quit()

    studies.append(study)

    #print etree.tostring(studies)
    #quit()
        #print etree.tostring(elm, pretty_print=True)
    #interventions_root.append(deepcopy(root.findall("intervention")))

interventions_xml_f = open(os.path.abspath('../../../../result/clinicaltrails.gov/study_drugs.xml'), 'w')
interventions_xml_f.write(etree.tostring(studies, pretty_print=True, xml_declaration=True, encoding="UTF-8"))
interventions_xml_f.close()
    
