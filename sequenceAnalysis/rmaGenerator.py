### this script creates the input files for MEGAN5 and runs them in batch mode

import os,sys

def suffixesFinder(label):

    '''
    this function finds the suffixes of the reads
    '''

    inputFileName=dataDir+'fasta/%s/readsFile1.fasta'%label
    with open(inputFileName,'r') as f:
        line=f.readline()
        vector=line.split()
        suffix1=vector[-1]

    inputFileName=dataDir+'fasta/%s/readsFile2.fasta'%label
    with open(inputFileName,'r') as f:
        line=f.readline()
        vector=line.split()
        suffix2=vector[-1]

    suffixes=[suffix1,suffix2]

    return suffixes

### MAIN

# 0. user defined variables
print 'defining user variables...'
dataDir='/Volumes/omics4tb/alomana/projects/rossSea/data/metagenomics/'
inputDirs=['Sample_DS-184436', 'Sample_DS-184444', 'Sample_DS-184460', 'Sample_DS-184465', 'Sample_DS-184468', 'Sample_DS-184469', 'Sample_DS-184466']
meganPath='/Applications/MEGAN/MEGAN.app/Contents/MacOS/JavaApplicationStub'
currentDir='/Volumes/omics4tb/alomana/projects/rossSea/src/metagenomics/'

# 1. creating the runner file
for label in inputDirs:
    
    print 'creating runner file %s...'%label

    suffixes=suffixesFinder(label)

    runnerFile='runners/runner_%s.txt'%label
    
    with open(runnerFile,'w') as f:
        
        f.write("load taxGIFile='/Applications/MEGAN/class/resources/files/gi_taxid-March2015X.bin';\n")
        f.write("set taxUseGIMap=true;\n")
        f.write("load keggGIFile='/Applications/MEGAN/class/resources/files/gi2kegg-Feb2015X.bin';\n")
        f.write("set keggUseGIMap=true;\n")
        f.write("load seedGIFile='/Applications/MEGAN/class/resources/files/gi2seed.map';\n")
        f.write("set seedUseGIMap=true;\n")
        f.write("load cogGIFile='/Applications/MEGAN/class/resources/files/ncbi/ncbi.map';\n")
        f.write("set cogUseGIMap=true;\n")

        f.write("import blastFile='%sdiamond/%s/readsFileStrict1.m8', '%sdiamond/%s/readsFileStrict2.m8' "%(dataDir,label,dataDir,label))
        f.write("fastaFile='%sfasta/%s/readsFile1.fasta', '%sfasta/%s/readsFile2.fasta' "%(dataDir,label,dataDir,label))
        f.write("meganFile='%smegan/%s.rma' "%(dataDir,label))
        f.write("maxMatches=100 minScore=50.0 maxExpected=0.01 topPercent=10.0 minSupport=1 minComplexity=0.0 useMinimalCoverageHeuristic=false useSeed=true useCOG=true useKegg=true paired=true ")
        f.write("suffix1='%s' suffix2='%s' "%(suffixes[0],suffixes[1]))
        f.write("useIdentityFilter=false textStoragePolicy=InRMAZ blastFormat=BlastTAB mapping='Taxonomy:BUILT_IN=true,Taxonomy:GI_MAP=true,SEED:GI_MAP=true,KEGG:GI_MAP=true,COG:GI_MAP=true,COG:REFSEQ_MAP=true';\n")
        f.write("quit;\n")

    # 2. executing
    print 'executing runner file %s...'%label
    cmd='%s -g -E -c %s%s'%(meganPath,currentDir,runnerFile)

    print
    print cmd
    print

    os.system(cmd)
    print
    print '%s job completed.'%label
    
