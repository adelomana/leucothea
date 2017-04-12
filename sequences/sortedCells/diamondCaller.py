### this script reads the input fasta files and calls DIAMOND. The output files are in .m8 format. Script to be run in aegir under SGE environment.

import os,sys

def diamondDBbuilder():

    '''
    this function creates a runner file to be run in aegir under the SGE
    '''

    print('building the database for DIAMOND...')
    # creating runner filels
    
    inputFile=scratchDir+'databaseBuilder.sh'
    with open(inputFile,'w') as g:
        g.write('#!/bin/bash\n\n')
        g.write('#$ -N dbBuild\n')
        g.write('#$ -o %smessages_database_DIAMOND.o.txt\n'%scratchDir)
        g.write('#$ -e %smessages_database_DIAMOND.e.txt\n'%scratchDir)
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
    
    inputFile='{}sgeRunners/nr.{}.sh'.format(scratchDir,tag)
    with open(inputFile,'w') as g:
        g.write('#!/bin/bash\n\n')
        g.write('#$ -N n.%s\n'%tag)
        g.write('#$ -o %smessages.DIAMOND.RS.nr.%s.o.txt\n'%(scratchDir,tag))
        g.write('#$ -e %smessages.DIAMOND.RS.nr.%s.e.txt\n'%(scratchDir,tag))
        g.write('#$ -P Bal_alomana\n')
        g.write('#$ -pe serial %s\n'%threads)
        g.write('#$ -q baliga\n')
        g.write('#$ -S /bin/bash\n\n')
        g.write('cd /users/alomana\n')
        g.write('source .bash_profile\n\n')

        cmd='time '+diamondPath+' blastx -d '+dataBaseDiamondPath+' -q '+fastaFilesDir+tag+'.fasta'+' -o '+diamondOutputDir+tag+'.m8'+' --threads '+str(threads)+' --sensitive -e 1e-5' # e-value reference, http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3613424/
        g.write('%s\n\n'%cmd)

    g.close()

    return None

# 0. user defined variables
threads=40
diamondPath='/proj/omics4tb/alomana/software/diamond-linux64_v0.8.30/diamond'
dataBaseFastaFile='/proj/omics4tb/alomana/software/diamond-linux64_v0.8.30/nr.91680400.20160801.fa'
dataBaseDiamondPath='/proj/omics4tb/alomana/software/diamond-linux64_v0.8.30/nr.91680400.20160801'
fastaFilesDir='/proj/omics4tb/alomana/projects/rossSea/data/sortedCells/FASTA/'
diamondOutputDir='/proj/omics4tb/alomana/projects/rossSea/data/sortedCells/diamond/'
scratchDir='/proj/omics4tb/alomana/scratch/'

# 1. building DIAMOND db
#diamondDBbuilder()
#sys.exit()

# 2. define the inputs
foundFiles=os.listdir(fastaFilesDir)
readsFiles=[element for element in foundFiles if '-cells.fasta' in element]

# 3. create launching the SGE calling files
print('launching senders in SGE...')
for sample in readsFiles:

    flag=sample.split('.fasta')[0]
    
    runnerCreator(flag)

    # 2.1. launching
    cmd='qsub {}sgeRunners/nr.{}.sh'.format(scratchDir,flag)
    os.system(cmd)

print('... all done.')
