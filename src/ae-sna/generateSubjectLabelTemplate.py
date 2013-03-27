"""
=====================================================================
generate csv file for labeling subjects
=====================================================================
"""
print __doc__

import logging
import os
from lxml import etree
import numpy as np
import re

#from misc import AlchemyAPI
from misc.util import *

# Display progress logs on stdout
logging.basicConfig(level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s]: %(message)s')

logger = logging.getLogger(__name__)

def main():
    drugs = ['avastin','melphalan','tamoxifen','taxotere']

    subjectLabels_f = open(os.path.abspath("../../misc/subjectLabelTemplates.csv"), 'w')

    for drug in drugs:
        print >> subjectLabels_f,"%s,,"%drug

        data_folder = '../../result/twitter-user-timeline-by-drug/%s/result'%drug


        input_files = os.listdir(data_folder)


        for input_file in input_files:
            if not input_file.endswith('A.txt.xml'):
                continue

            m = re.match("(\d+).A.txt.xml",input_file)

            userId = m.group(1)
            print >> subjectLabels_f,"%s,0,0"%userId



    subjectLabels_f.close()

    return


if __name__ == '__main__':
    main()
