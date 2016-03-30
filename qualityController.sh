#!/bin/bash

echo 'starting filtering and formatting... '

# Sample_DS-184444
#echo 'working with 184444...'
#cd Sample_DS-184444 
#pearf -1 readsFile1.trimmed.fastq -2 readsFile2.trimmed.fastq
#echo 'converting fastq into fasta...'
#awk 'BEGIN{P=1}{if(P==1||P==2){gsub(/^[@]/,">");print}; if(P==4)P=0; P++}' readsFile1.trimmed.fastq.filtered.fastq > readsFile1.fasta
#awk 'BEGIN{P=1}{if(P==1||P==2){gsub(/^[@]/,">");print}; if(P==4)P=0; P++}' readsFile2.trimmed.fastq.filtered.fastq > readsFile2.fasta
#rm *garbage*
#cd ..
#echo ''

# Sample_DS-184468
#echo 'working with 184468...'
#cd Sample_DS-184468 
#pearf -1 readsFile1.trimmed.fastq -2 readsFile2.trimmed.fastq
#echo 'converting fastq into fasta...'
#awk 'BEGIN{P=1}{if(P==1||P==2){gsub(/^[@]/,">");print}; if(P==4)P=0; P++}' readsFile1.trimmed.fastq.filtered.fastq > readsFile1.fasta
#awk 'BEGIN{P=1}{if(P==1||P==2){gsub(/^[@]/,">");print}; if(P==4)P=0; P++}' readsFile2.trimmed.fastq.filtered.fastq > readsFile2.fasta
#rm *garbage*
#cd ..
#echo ''

# Sample_DS-184469
#echo 'working with 184469...'
#cd Sample_DS-184469 
#pearf -1 readsFile1.trimmed.fastq -2 readsFile2.trimmed.fastq
#echo 'converting fastq into fasta...'
#awk 'BEGIN{P=1}{if(P==1||P==2){gsub(/^[@]/,">");print}; if(P==4)P=0; P++}' readsFile1.trimmed.fastq.filtered.fastq > readsFile1.fasta
#awk 'BEGIN{P=1}{if(P==1||P==2){gsub(/^[@]/,">");print}; if(P==4)P=0; P++}' readsFile2.trimmed.fastq.filtered.fastq > readsFile2.fasta
#rm *garbage*
#cd ..
#echo ''

# Sample_DS-184436
#echo 'working with 184436...'
#cd Sample_DS-184436
#pearf -1 readsFile1.trimmed.fastq -2 readsFile2.trimmed.fastq
#echo 'converting fastq into fasta...'
#awk 'BEGIN{P=1}{if(P==1||P==2){gsub(/^[@]/,">");print}; if(P==4)P=0; P++}' readsFile1.trimmed.fastq.filtered.fastq > readsFile1.fasta
#awk 'BEGIN{P=1}{if(P==1||P==2){gsub(/^[@]/,">");print}; if(P==4)P=0; P++}' readsFile2.trimmed.fastq.filtered.fastq > readsFile2.fasta
#rm *garbage*
#cd ..
#echo ''

# Sample_DS-184460
echo 'working with 184460...'
cd Sample_DS-184460
pearf -1 readsFile1.trimmed.fastq -2 readsFile2.trimmed.fastq
echo 'converting fastq into fasta...'
awk 'BEGIN{P=1}{if(P==1||P==2){gsub(/^[@]/,">");print}; if(P==4)P=0; P++}' readsFile1.trimmed.fastq.filtered.fastq > readsFile1.fasta
awk 'BEGIN{P=1}{if(P==1||P==2){gsub(/^[@]/,">");print}; if(P==4)P=0; P++}' readsFile2.trimmed.fastq.filtered.fastq > readsFile2.fasta
rm *garbage*
cd ..
echo ''

echo '... job completed.'
