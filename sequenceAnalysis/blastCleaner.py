### this script removes all hits from DIAMOND whose identity is lower than 0.70.
### the script expects a parallel environment, 5 threads are launched

import sys,multiprocessing,os
from multiprocessing import pool

def selector(inputFile):

    '''
    this function writes a new file with the selected hits
    '''

    outputFile=inputFile.replace('File','FileStrict')
    
    freq=0.
    nS=0
    nT=0

    with open(inputFile,'r') as f:
        with open(outputFile,'w') as g:
            for line in f:
                vector=line.split('\t')
                identity=float(vector[2])
                nT=nT+1
                if identity > threshold:
                    g.write(line)
                    nS=nS+1
                    
    freq=float(nS)/float(nT)

    return freq,nS,nT

### MAIN

# 0. user defined variables
inputFileDir='/Volumes/omics4tb/alomana/projects/rossSea/data/metagenomics/diamond/'
threshold=70.

# 1. selecting the input files
print 'selecting input files...'
inputFiles=[]
selectedDirs=os.listdir(inputFileDir)
selectedDirs=['Sample_DS-184436', 'Sample_DS-184444', 'Sample_DS-184468', 'Sample_DS-184469', 'Sample_DS-184465', 'Sample_DS-184460']
selectedDirs=['Sample_DS-184466']
for element in selectedDirs:
    fileName1=inputFileDir+element+'/readsFile1.m8'
    fileName2=inputFileDir+element+'/readsFile2.m8'
    inputFiles.append(fileName1)
    inputFiles.append(fileName2)

# 2. computing
print 'computing...'

all_freq=[]
all_nS=[]
all_nT=[]

# entering a parallel instance
hydra=multiprocessing.pool.Pool(5)
output=hydra.map(selector,inputFiles)
    
# 3. messages printing
print
allFreq=[]
for i in range(len(output)):

    print 'about file %s ...'%str(i+1)
    print 'total number of hits %s'%(output[i][2])
    print 'number of accepted hits %s'%(output[i][1])
    print 'frequency of acceptance %s'%(output[i][0])
    print

    allFreq.append(output[i][0])

print 'most successful frequencty',max(allFreq)
print 'least successful frequency',min(allFreq)
    
