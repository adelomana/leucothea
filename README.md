# leucothea
Tools for metagenomic analysis of Ross Sea.

## Maps
Scripts to create figures based on maps.

mapCreator.py | script to create a map of samples.  

## Sequence Analysis

### Metagenomic Analysis

The natural order for the analysis would follow as:  

readsCleaner.py | script to clean reads with Trimmomatic.   
qualityController.sh | shell script to check the quality of the paired reads and convert them into FASTA format.   
diamondCaller.py | script to call DIAMOND and convert FASTA reads into BLAST hits.   
blastCleaner.py | filter to select high confidence hits.   
rmaGenerator.py | script to call MEGAN5 to generate rma files.   
