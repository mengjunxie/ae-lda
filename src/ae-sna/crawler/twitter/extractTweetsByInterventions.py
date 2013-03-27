"""
=====================================================================
twitter cralwer
=====================================================================
"""
print __doc__

from copy import deepcopy
from lxml import etree
from urllib import urlencode
import StringIO
import logging
import os
import re
import urllib2

# Display progress logs on stdout
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] [%(levelname)s]: %(message)s')
                    
logger = logging.getLogger(__name__)

interventions_txt_f = os.path.abspath("../../../../result/clinicaltrails.gov/interventions.txt")

f = open(interventions_txt_f, 'r')

search_api_url = 'http://search.twitter.com/search.atom'

tweets_root = etree.Element("tweets")

for line in f:

    type, name = line.rstrip().split(':', 1)
	
    url = '%s?%s&show_user=true&include_entities=true&result_type=mixed' % (search_api_url, urlencode({'q':name}))
	
    q = "%s:%s" % (type, name)
    q = q.decode('utf-8')
    tweet = etree.Element("tweet", q=q)
    
    try:
        f = urllib2.urlopen(url)
        contents = f.read()
    
        #print contents
    
        feed = etree.parse(StringIO.StringIO(contents))
        
        for elm in feed.findall("//{http://www.w3.org/2005/Atom}entry"):
            
            tweet.append(deepcopy(elm))
            
        

    except (urllib2.HTTPError), e:
        tweet.set("error", "%s"%e)
    
    tweets_root.append(tweet)
    
    break
	
	
tweets_xml_f = open(os.path.abspath('../../../../result/twitter/tweets_by_interventions.xml'), 'w') 
tweets_xml_f.write(etree.tostring(tweets_root, pretty_print=True, xml_declaration=True, encoding="UTF-8"))
tweets_xml_f.close()
    
    
	
