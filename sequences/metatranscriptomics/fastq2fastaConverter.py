###
### this script converts in a multithread mode FASTQ files into FASTA files
###

import sys,os
import multiprocessing, multiprocessing.pool

def flexibleConverter(tag):

    '''
    this function uncompress gz files and convert them into FASTA files
    '''
    
    print()

    # f.2. actual conversion into FASTA files
    cmd0="awk 'BEGIN{P=1}{if(P==1||P==2){gsub(/^[@]/,\">\");print}; if(P==4)P=0; P++}'"
    cmd1=' {}{}_R1_001.paired.forward.fastq > {}{}_read.1.fasta'.format(fastqDir,tag,fastaDir,tag)
    cmd2=' {}{}_R2_001.paired.reverse.fastq > {}{}_read.2.fasta'.format(fastqDir,tag,fastaDir,tag)
    cmd3=cmd0+cmd1
    cmd4=cmd0+cmd2
    print(cmd3)
    os.system(cmd3)
    print(cmd4)
    os.system(cmd4)

    # f.4. separation print
    print()
    
    return None


# 0. user defined variables
fastqDir='/Users/alomana/scratch/cleanFASTQ/'
fastaDir='/Users/alomana/scratch/FASTA/'
scratchDir='/Users/alomana/scratch/'

numberOfThreads=4 # this should be 64

# 1. detecting all paired tags
print('detecting samples...')
fastqFiles=os.listdir(fastqDir)
tags=[]
for element in fastqFiles:
    if '_R1_001.paired.' in element:
        tag=element.split('_R1_001.paired.')[0]
        if tag not in tags:
            tags.append(tag)
tags.sort()
print(tags)
print('{} samples detected.'.format(len(tags)))

# 2. iterating over all files
print('parallel conversion of files...')

hydra=multiprocessing.pool.Pool(numberOfThreads)
output=hydra.map(flexibleConverter,tags)

print('... all done.')
