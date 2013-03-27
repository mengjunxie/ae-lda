"""
=====================================================================
search for ae by drugs
=====================================================================
"""
print __doc__

import logging
import os
import re
import MySQLdb
from lxml import etree
from misc.util import *

# Display progress logs on stdout
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] [%(levelname)s]: %(message)s')

logger = logging.getLogger(__name__)

interventions_f = open(os.path.abspath("../../result/clinicaltrails.gov/interventions.txt"), 'r')

aers_folder = os.path.abspath("../../../../data/aers/")

aers_sgms = os.listdir(aers_folder)

for line in interventions_f:
    print "ddd"