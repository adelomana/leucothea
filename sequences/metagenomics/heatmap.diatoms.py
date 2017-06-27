import sys,numpy,copy
import matplotlib,matplotlib.pyplot

sys.path.append('../lib/')
import library

# 0. defining user variables and paths
dataDir='/Volumes/omics4tb/alomana/projects/rossSea/results/metagenomics/heatmap/'

# 1.1. defining the columns
samples=[68,44,36,60,65,66,69] # ordered N to S
samplesPositions=['74-.05/.19','74.80','75.46','75.75','75.75','75.76','76-.50/.50/.50']

# 1.2 defining the set of conditions
frequencyThreshold=1e-3
flotilla=[]
for sample in samples:
    inputFileName=dataDir+'summaryData.%s.txt'%sample
    print(inputFileName)
    noahsArk,taxonomy=library.sampleReader(inputFileName,'Bacillariophyta')
    flotilla.append([noahsArk,taxonomy])

# 1.3. defining the matrix to plot
# 1.3.1. defining the row names
print('defining the row names...')
bacteriaTaxa=[]
deepTaxa=[]
rowNames=[]
for boat in flotilla:
    noahsArk=boat[0]
    taxonomy=boat[1]
    # working for each boat, selecting only genera
    taxa=noahsArk.keys()
    for taxon in taxa:
        if taxon.find('Bacillariophyta') != -1 and noahsArk[taxon] > frequencyThreshold and taxon not in bacteriaTaxa:
            bacteriaTaxa.append(taxon)

# defining the deep taxa: only genera (depth = 10)
for taxon in bacteriaTaxa:
    depth=len(taxon.split('/'))
    if depth == 10:
        deepTaxa.append(taxon)
print(len(deepTaxa),'Bacillariophyta taxa found with abundance higher than threshold.')

# selecting the n best, based only on abundance
relevances={}
n=50
finalCount=min([n,len(deepTaxa)])

for i in range(finalCount):
    genera=deepTaxa[i]
    sumFreq=0
    for boat in flotilla:
        try:
            value=boat[0][genera]
        except:
            value=0
        sumFreq=sumFreq+value
    average=numpy.log10(sumFreq/len(flotilla))
    relevances[genera]=average
rowNames=sorted(relevances,key=relevances.get,reverse=True)

print('')
print(len(rowNames),'selected taxa for plotting.')
for element in rowNames:
    print(element,relevances[element])


# 1.3.2. defining column names
columnNames=[str(sample) for sample in samples]

# 1.3.3. defining the matrix values
accumulated={}
m=[]
for boat in flotilla:
    noahsArk=boat[0]
    taxonomy=boat[1]
    v=[]
    for rowName in rowNames:
        if rowName in noahsArk:
            value=numpy.log10(noahsArk[rowName])
        else:
            value=numpy.log10(frequencyThreshold)-1    
        v.append(value)
    m.append(v)
m=numpy.array(m)
t=numpy.transpose(m)

print(numpy.max(t),numpy.min(t))

# 2. making figure
print('plotting...')
matplotlib.pyplot.imshow(t,interpolation='none',cmap='viridis',vmin=-1,vmax=-3.5) # ,vmin=3.,vmax=7.
matplotlib.pyplot.colorbar(label='log$_{10}$ rel. abund.',orientation='vertical',fraction=0.01)
matplotlib.pyplot.grid(False)

# 2.1. dealing with column and row names
matplotlib.pyplot.xticks(range(len(columnNames)),samplesPositions,size=8,rotation=90)

shortNames=[element.split('/')[-1] for element in rowNames]
matplotlib.pyplot.yticks(range(len(shortNames)),shortNames,size=8)

# 2.2. saving the figure
matplotlib.pyplot.tight_layout()
matplotlib.pyplot.savefig('figures/bacillariophyta.png')
            
