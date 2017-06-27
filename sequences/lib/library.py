import sys,numpy

def entropyCalculator(a):

    '''
    this function computes the entropy of the distribution of a taxon over samples
    '''

    lowerBound=-6
    if min(a) < lowerBound:
        print(a)
        print('error. lower bound exceeded. exiting...')
        sys.exit()

    v=numpy.array(a)
    n,bins=numpy.histogram(v,bins=abs(lowerBound),range=(lowerBound,0))

    s=float(sum(n))
    y=n/s

    h=0
    for element in y:
        if element != 0.0:
            term=-element*numpy.log2(element)
            h=h+term

    return h

def sampleReader(inputFileName,frequencyTaxon):

    noahsArk={}
    taxonomy=[]
    computing=False

    with open(inputFileName,'r') as f:
        for line in f:
            vector=line.split('  ')
            cleanVector=[]
            for element in vector:
                element=element.replace('\n','')
                elements=element.split(': ')
                for item in elements:
                    cleanVector.append(item)

            # choose which lines to read based on defining relative number of total reads
            if len(cleanVector) > 2:
                if cleanVector[-2] == frequencyTaxon:
                    totalReads=int(cleanVector[-1])
                    computing=True
            if cleanVector[0][:5] == '+++++':
                computing=False
                
            # filling up Noah's ark. Building a dictionary with unique names and number of reads and a list for the structure of the taxonomy
            
            # dealing with the taxonomy
            taxonomyDepth=len(cleanVector)-1
            for i in range(taxonomyDepth):
                putative=cleanVector[i]
                # creating a list if it is a new taxon level
                if putative != '':
                    if len(taxonomy) < i+1:
                        taxonomy.append([])
                    # adding the taxon if it does not exists
                    if putative not in taxonomy[i]:
                        taxonomy[i].append(putative)

            # adding the number of reads to the taxon
            if computing == True:
                numberOfReads=int(cleanVector[-1])
                if numberOfReads > 1e2:
                    relativeAbundance=numberOfReads/totalReads
                    verboseTaxon=[taxonomy[taxon][-1] for taxon in range(taxonomyDepth)]
                    tag='/'.join(verboseTaxon)
                    noahsArk[tag]=relativeAbundance

                    #print(tag,numberOfReads,relativeAbundance)

    return noahsArk,taxonomy
