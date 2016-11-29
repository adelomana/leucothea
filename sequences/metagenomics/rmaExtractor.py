### this script creates the input files for MEGAN5 and runs them in batch mode

import os,sys

# 0. user defined variables
print 'defining user variables...'
workingDir='/Volumes/omics4tb/alomana/projects/rossSea/src/metagenomics/'
dataDir='/Volumes/omics4tb/alomana/projects/rossSea/data/metagenomics/rma.refseq/'
meganPath='/Applications/MEGAN/MEGAN.app/Contents/MacOS/JavaApplicationStub'
hitsDir='/Volumes/omics4tb/alomana/projects/rossSea/data/metagenomics/taxonHits/'

# 1. defining the input files
files=os.listdir(dataDir)
inputFiles=[element for element in files if 'rmaz' not in element]

# 2. creating the runner file
for inputFile in inputFiles:
    
    label=inputFile.split('.rma')[0]
    print 'creating runner file %s...'%label

    runnerFile='extractors/runner_%s.txt'%label
    with open(runnerFile,'w') as f:
        
        f.write("open file='%s%s';\n"%(dataDir,inputFile))
        f.write("collapse rank='Species';\n")
        f.write("select rank='Species';\n")
        f.write("set drawer=RectangularPhylogram;\n")
        f.write("show window=message;\n")
        f.write("list summary=all;\n")
        f.write("quit;\n")

    # 2. executing
    print 'executing runner file %s...'%label
    cmd='%s -g -E -c %s%s > %s%s.txt'%(meganPath,workingDir,runnerFile,hitsDir,label)

    print
    print cmd
    print

    os.system(cmd)
    print
    print '%s job completed.'%label

    
