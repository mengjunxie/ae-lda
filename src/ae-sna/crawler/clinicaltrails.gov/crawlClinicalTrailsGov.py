"""
=====================================================================
test cralwer
=====================================================================
"""
print __doc__

import re
import logging
import urllib2
import os

# Display progress logs on stdout
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] [%(levelname)s]: %(message)s')
                    
logger = logging.getLogger(__name__)
       
result_folder = os.path.abspath("../../../../result/clinicaltrails.gov/xml/")

root_url = 'http://clinicaltrials.gov'

f = urllib2.urlopen('http://clinicaltrials.gov/ct2/crawler/')

contents = f.read()

urls = re.findall(r"/ct2/crawl/\d+", contents)

total = len(urls) - 1
i = 0
for url in urls:
    print "%.2f%%"%(float(i)/total*100)
    
    f = urllib2.urlopen("%s%s"%(root_url,url))
    contents = f.read()
    
    for m in re.finditer(r"/ct2/show/NCT\d+", contents):
        url = m.group(0)
        nct_id = re.search(r"NCT\d+", url).group(0)
     
        f = urllib2.urlopen("%s%s?resultsxml=true"%(root_url,url))
        contents = f.read()       
        
        
        f = open('%s/%s.xml'%(result_folder,nct_id), 'w')
        f.write(contents)
        f.close()
        
    i += 1


