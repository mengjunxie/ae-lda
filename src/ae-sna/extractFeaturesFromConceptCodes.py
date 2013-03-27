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
import csv

#from misc import AlchemyAPI
from misc.util import *

# Display progress logs on stdout
logging.basicConfig(level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s]: %(message)s')

logger = logging.getLogger(__name__)

semTypes = {}
semTypes_f = open(os.path.abspath("../../misc/SRDEF"), 'r')

aSemTypes = []

for line in semTypes_f:
    if line.rstrip() == '':
        continue

    #print line.rstrip().split('|')
    type,t,c,_,d,_,_,_,s,_,_ = line.rstrip().split('|')
    if type <> 'STY':
        continue

    semTypes[s] = {'t':t,'c':c,'d':d}

    aSemTypes.append(s)

aSemTypes = set(aSemTypes)

tSemTypes = aSemTypes

semGroups = {}

semGroups_f = open(os.path.abspath("../../misc/SemGroups.txt"), 'r')

for line in semGroups_f:
    if line.rstrip() == '':
        continue

    #print line.rstrip().split('|')
    g,d,t,_ = line.rstrip().split('|')

    semGroups[t] = {'g':g,'d':d}


aSemGroups = ['ANAT', 'CHEM', 'PHYS', 'OCCU', 'ORGA', 'PHEN', 'ACTI', 'OBJC', 'CONC', 'LIVB', 'GENE', 'PROC', 'DEVI', 'GEOG', 'DISO']

tSemGroups = aSemGroups #['DISO', 'CHEM','DEVI','PHYS','GENE']
    #semTypes[semA] = semType
    #semTypes.append(semA)
featureSets = []

for semGroup in tSemGroups:
    featureSets.append(semGroup)

for semType in tSemTypes:
    featureSets.append(semType)

for x in [ 35,  50,  59, 149]:
    y =  x-22
    print featureSets[y]

quit()


MIN_SCORE = 800

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

    semType_count = {}

    semGroup_count = {}

    for semGroup in tSemGroups:
        semGroup_count[semGroup] = 0

    for semType in tSemTypes:
        semType_count[semType] = 0

    try:
        for candidate in concepts_root.xpath("//Mappings[@Count>0]/Mapping/Candidates/Candidate"):
            concept = Concept(abs(int(candidate.find("CandidateScore").text)),candidate.find("CandidateCUI").text, candidate.find("CandidatePreferred").text, candidate.find("./SemTypes/SemType").text)

            if concept.sem_group not in tSemGroups:
                continue

            if int(concept.score) < MIN_SCORE:
                continue

            concepts.append(concept)
            semGroup_count[concept.sem_group] += 1
            semType_count[concept.sem_type] += 1
    except:
        logger.info(inputFile)

    return semType_count,semGroup_count,concepts

class Subject(object):

    def __init__(self, userId, drugUseFlag, sideEffectsFlag):
        '''
        '''
        self.userId = userId
        self.drugUseFlag = drugUseFlag
        self.sideEffectsFlag = sideEffectsFlag

    def __repr__( self ):
        return "userId: %s; drugUseFlag: %s; sideEffectsFlag: %s;"%(self.userId,self.drugUseFlag,self.sideEffectsFlag)

def get_subjects():
    subjectLabels = csv.reader(open("../../misc/subjectLabels.csv", "rU"))

    subjects = {}
    l=lambda i: 1 if int(i) > 0 else 0

    userIds = []
    for row in subjectLabels:
        userId = row[0]
        drugUseFlag = l(row[1])
        sideEffectsFlag = l(row[2])
        subjects[userId] = Subject(userId,drugUseFlag,sideEffectsFlag)

        userIds.append(userId)


    return userIds,subjects


def main():
    data_folder = "../../result/twitter-user-timeline-by-drug/R/result"

    input_files = os.listdir(data_folder)

    uIds,subjects = get_subjects()

    subjectFeatureMatrix = []

    for input_file in input_files:
        if not input_file.endswith('.xml'):
            continue

        m = re.match("(\d+).*?xml",input_file)

        userId = m.group(1)

        if subjects[userId].drugUseFlag == 0:
            continue

        semType_count,semGroup_count,concepts = process_metamap_xml(input_file, data_folder)


        subjectFV = []

        for semGroup in tSemGroups:
            subjectFV.append(semGroup_count[semGroup])

        for semType in tSemTypes:
            subjectFV.append(semType_count[semType])

        subject = [userId] + subjectFV

        subjectFeatureMatrix.append(subject)

    subjectFeatureMatrix = np.array(subjectFeatureMatrix)

    print len(subjectFeatureMatrix)
        #subjectLabels_f.close()
    np.save("../../result/classification-features/ae-tweets-semGroups-semTypes.npy", subjectFeatureMatrix)


    return


if __name__ == '__main__':
    main()


