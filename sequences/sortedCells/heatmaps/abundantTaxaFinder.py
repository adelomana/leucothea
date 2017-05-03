import sys,matplotlib,numpy,os
import matplotlib,matplotlib.pyplot

sys.path.append(os.path.abspath('../../lib'))
import library

# 0. defining user variables and paths
dataDir='/Volumes/omics4tb/alomana/projects/rossSea/data/sortedCells/hits/genus/'
figureFolder='/Volumes/omics4tb/alomana/projects/rossSea/results/'

# 1.1. defining sample names
sampleNames={}
sampleNames['01']='120 large'
sampleNames['02']='120 small'
sampleNames['03']='124 small'
sampleNames['04a']='124 large'

sampleTags=list(sampleNames.keys())
sampleTags.sort()

# 1.2 reading all data
flotilla=[]
for tag in sampleTags:
    inputFileName=dataDir+'%s.txt'%tag
    noahsArk,taxonomy=library.sampleReader(inputFileName)
    flotilla.append([noahsArk,taxonomy])

# 2.1. defining all relevant taxa
print('defining deep and selected taxa...')
selectedTaxa=[]
deepTaxa=[]

for boat in flotilla:
    noahsArk=boat[0]
    taxonomy=boat[1]

    # working on each "boat" (sample)
    taxa=noahsArk.keys()
    for taxon in taxa:
        if noahsArk[taxon] > 1/2000 and taxon not in selectedTaxa:            
            selectedTaxa.append(taxon)
            
# defining the deep taxa
for taxon in selectedTaxa:
    broken=taxon.split('/')
    depth=len(broken)
    # is there a deeper taxon, then it is not deep enough
    deep=0
    for element in selectedTaxa:
        if element.find(taxon) != -1:
            deep=deep+1
    if deep == 1:
        deepTaxa.append(taxon)
print(len(deepTaxa),'selected taxa found with abundance higher than threshold.')


# 2.2. selecting the 50 most abundant taxa
rank={}
for taxon in deepTaxa:
    abundances=[]
    for boat in flotilla:
        noahsArk=boat[0]
        if taxon in noahsArk.keys():
            localAbundance=noahsArk[taxon]
        else:
            localAbundance=0
        abundances.append(localAbundance)
    rank[taxon]=sum(abundances)

kings=sorted(rank,key=rank.get,reverse=True)

for king in kings:
    for i in range(len(sampleTags)):
        freq=0
        try:
            freq=flotilla[i][0][king]
        except:
            pass
        print(king,sampleTags[i],freq)
    print('')
        

sys.exit()
