### this script reads the input fasta files and calls DIAMOND. The output files are in .m8 format. Script to be run in aegir under SGE environment.

import os,sys

def diamondDBbuilder():

    '''
    this function creates a runner file to be run in aegir under the SGE
    '''

    print 'building the database for DIAMOND...'
    # creating runner file
    inputFile=scratchDir+'databaseBuilder.sh'
    with open(inputFile,'w') as g:
        g.write('#!/bin/bash\n\n')
        g.write('#$ -N database\n')
        g.write('#$ -o %s/messages_database_DIAMOND.o.txt\n'%scratchDir)
        g.write('#$ -e %s/messages_database_DIAMOND.e.txt\n'%scratchDir)
        g.write('#$ -P Bal_alomana\n')
        g.write('#$ -pe serial %s\n'%threads)
        g.write('#$ -q baliga\n')
        g.write('#$ -S /bin/bash\n\n')
        g.write('cd /users/alomana\n')
        g.write('source .bash_profile\n\n')

        cmd='time '+diamondPath+' makedb --in '+dataBaseFastaFile+' -d '+dataBaseDiamondPath+' --threads '+str(threads)
        g.write('%s\n\n'%cmd)
        
    g.close()

    # submitting to queue
    cmd='qsub %s'%inputFile
    os.system(cmd)

    return None

def runnerCreator(tag):

    '''
    this function creates the runner files of aegir SGE system
    '''

    minimalTag=tag.split('-')[1]
    
    inputFile='sgeRunners/%s.sh'%tag
    with open(inputFile,'w') as g:
        g.write('#!/bin/bash\n\n')
        g.write('#$ -N %s\n'%minimalTag)
        g.write('#$ -o %s/messagesDIAMOND_%s.o.txt\n'%(scratchDir,minimalTag))
        g.write('#$ -e %s/messagesDIAMOND_%s.e.txt\n'%(scratchDir,minimalTag))
        g.write('#$ -P Bal_alomana\n')
        g.write('#$ -pe serial %s\n'%threads)
        g.write('#$ -q baliga\n')
        g.write('#$ -S /bin/bash\n\n')
        g.write('cd /users/alomana\n')
        g.write('source .bash_profile\n\n')

        cmd='time '+diamondPath+' blastx -d '+dataBaseDiamondPath+' -q '+fastaFilesDir+tag+'/readsFile1.fasta -a '+diamondOutputDir+tag+'/readsFile1'+' --threads '+str(threads)+' --sensitive -e 1e-5' # e-value reference, http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3613424/
        g.write('%s\n\n'%cmd)

        cmd=diamondPath+' view -a '+diamondOutputDir+tag+'/readsFile1'+'.daa -o '+diamondOutputDir+tag+'/readsFile1'+'.m8'
        g.write('%s\n\n'%cmd)

        cmd='time '+diamondPath+' blastx -d '+dataBaseDiamondPath+' -q '+fastaFilesDir+tag+'/readsFile2.fasta -a '+diamondOutputDir+tag+'/readsFile2'+' --threads '+str(threads)+' --sensitive -e 1e-5'
        g.write('%s\n\n'%cmd)

        cmd=diamondPath+' view -a '+diamondOutputDir+tag+'/readsFile2'+'.daa -o '+diamondOutputDir+tag+'/readsFile2'+'.m8'
        g.write('%s\n\n'%cmd)

    g.close()

    return None

# 0. user defined variables
threads=40
diamondPath='/proj/omics4tb/alomana/software/diamond-linux64_binary_v0.7.11/diamond'
dataBaseFastaFile='/proj/omics4tb/alomana/software/diamond-linux64_binary_v0.7.11/complete.nonredundant_protein.all.version.january.19.faa'
dataBaseDiamondPath='/proj/omics4tb/alomana/software/diamond-linux64_binary_v0.7.11/refseq_jan_19_complete.nonredundant_protein'
fastaFilesDir='/proj/omics4tb/alomana/projects/rossSea/data/metagenomics/fasta/'
diamondOutputDir='/proj/omics4tb/alomana/projects/rossSea/data/metagenomics/diamond/'
scratchDir='/proj/omics4tb/alomana/scratch/diamond/'

# 1. building DIAMOND db
#diamondDBbuilder()
#sys.exit()

# 2. define the inputs
foundFolders=os.listdir(fastaFilesDir)
readsDirs=[element for element in foundFolders if 'Sample' in element]

readsDirs=['Sample_DS-184436']

# 3. create launching the SGE calling files
print 'launching senders in SGE...'
for sample in readsDirs:

    newDir=diamondOutputDir+sample
    if not os.path.exists(newDir):
        os.mkdir(newDir)  
    
    runnerCreator(sample)

    # 2.1. launching
    cmd='qsub sgeRunners/%s.sh'%sample
    os.system(cmd)

print '... all done.'
