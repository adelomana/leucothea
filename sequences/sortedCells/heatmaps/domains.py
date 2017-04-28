import sys,matplotlib,numpy
from matplotlib import pyplot
import library

# 0. defining user variables and paths
dataDir='/Volumes/omics4tb/alomana/projects/rossSea/results/metagenomics/heatmap/'

# 1.1. defining the columns
samples=[68,44,36,60,65,66,69] # ordered N to S
samplesPositions=['74-.05/.19','74.80','75.46','75.75','75.75','75.76','76-.50/.50/.50']

# 1.2 defining the kingdoms
flotilla=[]
for sample in samples:
    inputFileName=dataDir+'summaryData.%s.txt'%sample
    noahsArk,taxonomy=library.sampleReader(inputFileName)
    flotilla.append([noahsArk,taxonomy])

# 1.3. defining the matrix to plot
# 1.3.1. defining the row names
rowNames=[]
for boat in flotilla:
    noahsArk=boat[0]
    taxonomy=boat[1]
    for taxonA in taxonomy[1]:
        for taxonB in taxonomy[2]:
            tag='root/'+taxonA+'/'+taxonB
            if tag in noahsArk.keys():
                if tag not in rowNames and tag.find('Virus') == -1:
                    rowNames.append(tag)
rowNames.append('root/Viruses')
    
# 1.3.2. defining column names
columnNames=[str(sample) for sample in samples]

# 1.3.3. defining the matrix values
m=[]
for boat in flotilla:
    noahsArk=boat[0]
    taxonomy=boat[1]
    v=[]
    for rowName in rowNames:
        value=noahsArk[rowName]
        print rowName,value
        v.append(value)
    m.append(v)
    print
m=numpy.array(m)
t=numpy.transpose(m)
logT=numpy.log10(t)

# 2. making figure  
matplotlib.pyplot.imshow(logT,interpolation='none',cmap='jet',vmin=3.,vmax=7.) # ,vmin=3.,vmax=7.
matplotlib.pyplot.colorbar(label='log rel. abund.',orientation='horizontal')
matplotlib.pyplot.grid(False)

# 2.1. dealing with column and row names
matplotlib.pyplot.xticks(range(len(columnNames)),samplesPositions,rotation=-22.5)

shortNames=[element.split('/')[-1] for element in rowNames]
matplotlib.pyplot.yticks(range(len(shortNames)),shortNames)

# 2.2. saving the figure
matplotlib.pyplot.savefig('figures/domains.pdf')
            
