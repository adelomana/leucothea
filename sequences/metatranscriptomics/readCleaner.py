###
### this script calls Trimmomatic to clean raw reads
###

import os,sys,time

def proceedChecker():

    '''
    this function checks that time is not between 10 to 18 h
    '''

    proceed=False
    while proceed == False:
        currentHour=int(time.localtime().tm_hour)
        if currentHour < 9 or currentHour > 18:
            proceed=True
        else:
            print('current hour is {}. Waiting...'.format(currentHour))
            time.sleep(10*60) # 10*60 is 10 min

    return None
    
def trimmomaticCaller(instance):
    
    '''
    this function deals with the trimming of the reads using Trimmomatic. Recommended options, ILLUMINACLIP:path2AdaptersFile:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36
    '''

    print('working with file {}'.format(instance))

    logFile=logFilesDir+instance+'.messagesFromTrimming.txt'

    inputFile1=rawReadsDir+instance+'_R1_001.fastq'
    inputFile2=rawReadsDir+instance+'_R2_001.fastq'

    outputFile1a=cleanReadsDir+instance+'_R1_001.paired.forward.fastq'
    outputFile1b=cleanReadsDir+instance+'_R1_001.unpaired.forward.fastq'

    outputFile2a=cleanReadsDir+instance+'_R2_001.paired.reverse.fastq'
    outputFile2b=cleanReadsDir+instance+'_R2_001.unpaired.reverse.fastq'

    cmd='time '+javaPath+' -jar '+trimmomaticPath+' PE -threads 4 -phred33 -trimlog %s %s %s %s %s %s %s ILLUMINACLIP:%s:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36'%(logFile,inputFile1,inputFile2,outputFile1a,outputFile1b,outputFile2a,outputFile2b,path2Adapter)

    #proceedChecker()

    print(cmd)
    os.system(cmd)
    print()
        
    
    return None

### MAIN

# 0. defining user variables
rawReadsDir='/Users/alomana/scratch/FASTQ/'
cleanReadsDir='/Users/alomana/scratch/cleanFASTQ/'
logFilesDir='/Users/alomana/scratch/trimmomaticLogs/'
path2Adapter='/Users/alomana/software/Trimmomatic-0.36/adapters/TruSeq3-PE-2.fa'

javaPath='/Library/Internet\ Plug-Ins/JavaAppletPlugin.plugin/Contents/Home/bin/java'
trimmomaticPath='/Users/alomana/software/Trimmomatic-0.36/trimmomatic-0.36.jar'

# 1. reading the files
tag='_R1_001.fastq'
fastqFiles=os.listdir(rawReadsDir)
readFiles=[element for element in fastqFiles if tag in element]

# 2. calling Trimmomatic
for readFile in readFiles:
    instance=readFile.split(tag)[0]
    trimmomaticCaller(instance)
