# this pipeline converts species-specific extracted reads into input for megan

import os,sys

def hitsExtracter(sample):

    '''
    this function extracts species-specific reads and writes a file
    '''

    print('working with {}...'.format(sample))
    
    # f.1. obtain read names
    readNames=[]
    inputFileName=extractedReadsDir+sample
    with open(inputFileName,'r') as f:
        for line in f:
            vector=line.split()
            if vector[0][0] == '>':
                name=vector[0].replace('>','')
                readNames.append(name)
    print('\t {} reads found.'.format(len(readNames)))

    # f.2. define the searching files
    searchingFileTag=sample.split('.')[0]
    putativeFiles=os.listdir(diamondOriginalDir)
    searchingFiles=[element for element in putativeFiles if searchingFileTag in element]

    # f.3. search
    outputFileName=diamondSpeciesDir+sample.replace('.fasta','.m8')
    g=open(outputFileName,'w')

    # f.3.1. build a dictionary with read names and hits
    for hole in searchingFiles:
        print('\t\t reading file {}...'.format(hole))
        fullSet={}
        inputFileName=diamondOriginalDir+hole        
        with open(inputFileName,'r') as f:
            for line in f:
                vector=line.split()
                readName=vector[0]
                if readName not in fullSet:
                    fullSet[readName]=[line]
                else:
                    fullSet[readName].append(line)

        # f.3.2. writing found hits
        print('\t\t writing found hits...')
        for readName in readNames:
            try:
                for element in fullSet[readName]:
                    g.write(element)
            except:
                pass
    g.close()

    return None

# 0. define user defined variables
extractedReadsDir='/Volumes/omics4tb/alomana/projects/rossSea/data/metatranscriptomics/speciesSpecific/fasta/'
diamondOriginalDir='/Volumes/omics4tb/alomana/projects/rossSea/data/metatranscriptomics/diamond/'
diamondSpeciesDir='/Volumes/omics4tb/alomana/projects/rossSea/data/metatranscriptomics/speciesSpecific/diamond/'

# 1. select working samples
samples=os.listdir(extractedReadsDir)

# 2. launch parelel pipeline each for input file
for sample in samples:
    hitsExtracter(sample)

# find the diamond hit, and create a diamond file

# next steps will be call megan for functions specific, summary of functions and 
