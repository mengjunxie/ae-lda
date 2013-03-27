"""
=====================================================================
extract concept codes
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

semTypes = {}
semTypes_f = open(os.path.abspath("../../misc/SRDEF"), 'r')

for line in semTypes_f:
    if line.rstrip() == '':
        continue

    #print line.rstrip().split('|')
    type,t,c,_,d,_,_,_,s,_,_ = line.rstrip().split('|')
    if type <> 'STY':
        continue
    semTypes[s] = {'t':t,'c':c,'d':d}

semGroups = {}

semGroups_f = open(os.path.abspath("../../misc/SemGroups.txt"), 'r')

for line in semGroups_f:
    if line.rstrip() == '':
        continue

    #print line.rstrip().split('|')
    g,d,t,_ = line.rstrip().split('|')

    semGroups[t] = {'g':g,'d':d}


aSemGroups = ['ANAT', 'CHEM', 'PHYS', 'OCCU', 'ORGA', 'PHEN', 'ACTI', 'OBJC', 'CONC', 'LIVB', 'GENE', 'PROC', 'DEVI', 'GEOG', 'DISO']

tSemGroups = ['DISO', 'CHEM','DEVI','PHYS','GENE']
    #semTypes[semA] = semType
    #semTypes.append(semA)

class Concept(object):

    def __init__(self, score, cui, preferred_name, sem_type):
        '''
        '''
        self.score = score
        self.cui = cui
        self.preferred_name = preferred_name
        self.sem_type = sem_type
        self.sem_type_desc = semTypes[sem_type]['c']
        self.sem_group = semGroups[semTypes[sem_type]['t']]['g']
        self.sem_group_desc = semGroups[semTypes[sem_type]['t']]['d']


    def __repr__( self ):
        return "score: %s; cui: %s; preferred_name: %s; sem_type: %s; sem_type_desc: %s"%(self.score,self.cui,self.preferred_name,self.sem_type,self.sem_type_desc)


def process_metamap_xml(inputFile, outFolder):

    inputFile = "%s/%s"%(outFolder,inputFile)
    parser = etree.XMLParser(encoding="UTF-8", ns_clean=True,recover=True)

    concepts_root = etree.parse(inputFile,parser=parser)

    concepts = []

    semGroup_count = {}

    for semGroup in tSemGroups:
        semGroup_count[semGroup] = 0

    for candidate in concepts_root.xpath("//Mappings[@Count>0]/Mapping/Candidates/Candidate"):
        concept = Concept(abs(int(candidate.find("CandidateScore").text)),candidate.find("CandidateCUI").text, candidate.find("CandidatePreferred").text, candidate.find("./SemTypes/SemType").text)

        if concept.sem_group not in tSemGroups:
            continue

        concepts.append(concept)
        semGroup_count[concept.sem_group] += 1


    return semGroup_count,concepts


def main():
    data_folder = "../../result/twitter-user-timeline-by-drug/avastin/result"


    input_files = os.listdir(data_folder)

    subjectFeatureMatrix = []

    for input_file in input_files:
        if not input_file.endswith('A.txt.xml'):
            continue

        concepts_f = open(os.path.abspath("%s/%s.cuis.txt"%(data_folder,input_file)), 'w')

        m = re.match("(\d+).A.txt.xml",input_file)

        userId = m.group(1)
        semGroup_count,concepts = process_metamap_xml(input_file, data_folder)

        for concept in concepts:
            print >> concepts_f,"%s %s (%s) [%s]-(%s)-[%s]"%(concept.score,concept.cui,concept.preferred_name,concept.sem_group_desc,concept.sem_type,concept.sem_type_desc)

        concepts_f.close()

        #print >> subjectLabels_f,"%s|"%userId

        #subjectFV = process_metamap_xml(input_file, data_folder)
        #subject = [userId,0] + subjectFV

        #subjectFeatureMatrix.append(subject)

    #subjectFeatureMatrix = np.array(subjectFeatureMatrix)

    #subjectLabels_f.close()
    #print subjectFeatureMatrix

    return


if __name__ == '__main__':
    main()


