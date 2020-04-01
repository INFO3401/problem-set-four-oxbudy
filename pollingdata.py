import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#5
def normalizeData(dataframe):
    undecidedlist = []
    for i,v in dataframe.iterrows():
        undecidedlist.append((100 - (v[3] + v[4])))

    dataframe["Undecided"] = undecidedlist
    return dataframe

def plotCandidate(candidate, dataframe):
    plt.scatter(y=dataframe[candidate], x=dataframe['Poll'])
    plt.title(candidate + ' Polling')
    plt.ylim(0)
    plt.show()

#8
def statsPerCandidate(candidate, dataframe):
    avg = dataframe[candidate].mean()
    return avg

#10
def cleanSample(dataframe):
    typelist = []
    sizelist = []
    for i in dataframe['Sample']:
        typelist.append(i[-2:])
        sizelist.append(i[:-2])

    dataframe['Sample Type'] = typelist
    dataframe['Sample Size'] = sizelist
    dataframe = dataframe.replace('', None)
    return dataframe

#12
def computePollWeight(poll, dataframe):
    pollsum = 0
    for i,v in dataframe.iterrows():
        #v[0] is the name of the poll
        if v[0] == poll:
            #v[9] is the sample size number
            pollsum += int(v[9])

    weight = pollsum / dataframe['Sample Size'].astype(int).sum()
    return weight

#13
def weightedStatsPerCandidate(candidate, dataframe):
    pollsters = list(dataframe['Poll'].unique())
    results = []
    for i in pollsters:
        dataavg = dataframe.loc[dataframe['Poll'] == i]
        dataavg = dataavg[candidate].mean()
        weightedavg = dataavg * (computePollWeight(i, dataframe))
        results.append(weightedavg)

    return sum(results)

#15
def computeCorrelation(candidate1, candidate2, dataframe):
    return np.corrcoef(dataframe[candidate1], dataframe[candidate2])

#17
def superTuesday(dataframe):
    candidates = ['Bloomberg', 'Warren', 'Klobuchar', 'Buttigieg', 'Steyer']
    #Sanders
    dataframe['SandersST'] = dataframe['Sanders']
    dataframe['BidenST'] = dataframe['Biden']

    for i in candidates:
        bern = computeCorrelation('Sanders', i, dataframe)
        joe = computeCorrelation('Biden', i, dataframe)

        #[0][1] is the correlation coefficient
        if bern[0][1] > joe[0][1]:
            dataframe['SandersST'] = dataframe['SandersST'] + dataframe[i]
        elif joe[0][1] > bern[0][1]:
            dataframe['BidenST'] = dataframe['BidenST'] + dataframe[i]

    return dataframe



#A
