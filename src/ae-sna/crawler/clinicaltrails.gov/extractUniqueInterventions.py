"""
=====================================================================
extract stats on interventions
=====================================================================
"""
print __doc__

import re
import logging
import os
from lxml import etree
import collections

# Display progress logs on stdout
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] [%(levelname)s]: %(message)s')
                    
logger = logging.getLogger(__name__)
       
interventions_xml = os.path.abspath("../../../../result/clinicaltrails.gov/interventions.xml")

root = etree.parse(interventions_xml)

interventions_elms = root.xpath('/interventions/intervention')

interventions = []

for intervention_elm in interventions_elms:
    type = intervention_elm.findtext("intervention_type")
    name = intervention_elm.findtext("intervention_name")
    
    interventions.append("%s:%s"%(type,name))
    
    other_names = intervention_elm.findall("other_name")
    
    for name in other_names:
        name = name.text
        #print name
        interventions.append("%s:%s"%(type,name))
        
print collections.Counter(interventions)

interventions_text_f = open(os.path.abspath('../../../../result/clinicaltrails.gov/interventions.txt'), 'w')
for intervention in set(interventions):
    print >> interventions_text_f, intervention
interventions_text_f.close()
