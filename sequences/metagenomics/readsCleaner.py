### this script calls Trimmomatic to clean the reads
import os,sys

def trimmomaticCaller(instance):
    '''
    This function deals with the trimming of the reads using Trimmomatic. Recommended options, ILLUMINACLIP:TruSeq3-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36
    '''

    print 'working with file',instance

    logFile=logFilesDir+instance+'.messagesFromTrimming.txt'

    inputFile1=rawReadsDir+instance+'/readsFile1.fastq'
    inputFile2=rawReadsDir+instance+'/readsFile2.fastq'

    outputFile1a=cleanReadsDir+instance+'/readsFile1.trimmed.fastq'
    outputFile1b=cleanReadsDir+instance+'/readsFile1.garbage.fastq'

    outputFile2a=cleanReadsDir+instance+'/readsFile2.trimmed.fastq'
    outputFile2b=cleanReadsDir+instance+'/readsFile2.garbage.fastq'

    cmd='/Library/Internet\ Plug-Ins/JavaAppletPlugin.plugin/Contents/Home/bin/java -jar /Users/alomana/software/Trimmomatic-0.36/trimmomatic-0.36.jar PE -threads 4 -phred33 -trimlog %s %s %s %s %s %s %s ILLUMINACLIP:%s:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36'%(logFile,inputFile1,inputFile2,outputFile1a,outputFile1b,outputFile2a,outputFile2b,path2Adapter)  

    print cmd
    os.system(cmd)
    print
    
    return None

### MAIN

# 0. defining user variables
rawReadsDir='/Volumes/omics4tb/alomana/projects/rossSea/data/metagenomics/fastq/'
cleanReadsDir='/Volumes/omics4tb/alomana/projects/rossSea/data/metagenomics/fasta/'
logFilesDir='/Volumes/omics4tb/alomana/scratch/'

path2Adapter='/Users/alomana/projects/ap/seqs/src/adapters/TruSeq3-PE-2.fa'

# 1. reading the files
foundFolders=os.listdir(rawReadsDir)
readsDirs=[element for element in foundFolders if 'Sample' in element]


allLabels=[]
for readsFile in readsDirs:
    label=readsFile.split('/')[-1]
    allLabels.append(label)
sequencingInstances=list(set(allLabels))

# 2. calling Trimmomatic
for instance in sequencingInstances:
    trimmomaticCaller(instance)
