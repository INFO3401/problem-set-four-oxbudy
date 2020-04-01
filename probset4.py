from utils import *
from pollingdata import *
import matplotlib.pyplot as py

candidates = ['Sanders', 'Biden', 'Gabbard', 'Undecided']

#4
rcpdf = loadAndCleanData('/Users/joshua.baker/Documents/Github/problem-set-four-oxbudy/2020demnom.csv')

#6
rcpdf = normalizeData(rcpdf)
#print(rcpdf)

#7
"""
plotCandidate('Sanders', rcpdf)
plotCandidate('Biden', rcpdf)
plotCandidate('Gabbard', rcpdf)
"""
"""
These numbers indicate to me that Biden is the favored candidate.
He has multiple polls reaching 60 range, while Sanders doesn't have a single
poll for himself above 40.
"""

#9
#Undecided has a huge average because all of the candidates that had dropped
#by the time I downloaded the data were excluded entirely from it
for i in candidates:
    print(i + ' polling average: ' + str(statsPerCandidate(i, rcpdf)))

#11
rcpdf = cleanSample(rcpdf)

#12
print('Test weight ABC News: ' + str(computePollWeight('ABC News/Wash PostABC/WP', rcpdf)))

#14
for i in candidates:
    print(i + ' weighted polling average: ' + str(weightedStatsPerCandidate(i, rcpdf)))
#There wasn't much change in the results when the averages were weighted.
#Biden and Sanders are still basically tied when all of the data is factored in.
#I still believe Biden will win, as this function takes all of the data since
#January and doesn't weigh by recency of the poll. Biden's recent leads have
#been much more substantial

#16
computeCorrelation('Sanders', 'Biden', rcpdf)
#Sanders and Biden are slightly positively correlated.
#Biden has a very strong negative correlation with the undecideds.
#Both Sanders and Biden have almost no correlation with Gabbard's numbers

#18
#I ended up needing to use an old dataset from one of the lecture samples, as
#the dataset I downloaded didn't include anyone but Sanders, Biden, and Gabbard.
olddata = loadAndCleanData('/Users/joshua.baker/Documents/Github/problem-set-four-oxbudy/demnomOLD.csv')
olddata = normalizeData(olddata)
olddata = cleanSample(olddata)

olddatanew = superTuesday(olddata)

print('Sanders super tuesday polling avg: ' + str(statsPerCandidate('SandersST', olddatanew)))
print('Biden super tuesday polling avg: ' + str(statsPerCandidate('BidenST', olddatanew)))

#These are working weird. I presume it has to do with switching up the dataframe for this question
print(weightedStatsPerCandidate('SandersST', olddatanew))
print(weightedStatsPerCandidate('BidenST', olddatanew))

#This data would lead one to believe that Sanders would have a slight polling
#advantage after the candidates dropped from super tuesday.


#19
print(getConfidenceIntervals('Sanders', olddatanew))
print(getConfidenceIntervals('SandersST', olddatanew))
print(getConfidenceIntervals('Biden', olddatanew))
print(getConfidenceIntervals('BidenST', olddatanew))

#20
print(runTTest('Sanders', 'Biden', olddatanew))
print(runTTest('SandersST', 'BidenST', olddatanew))

#22
posttuesday = loadAndCleanData('/Users/joshua.baker/Documents/Github/problem-set-four-oxbudy/2020demnomNEW.csv')
posttuesday = normalizeData(posttuesday)
posttuesday = cleanSample(posttuesday)

print('Sanders post super tuesday polling avg: ' + str(statsPerCandidate('Sanders', posttuesday)))
print('Biden post super tuesday polling avg: ' + str(statsPerCandidate('Biden', posttuesday)))
#Weird issues with the weighted averages
#print(weightedStatsPerCandidate('Sanders', posttuesday))
#print(weightedStatsPerCandidate('Biden', posttuesday))
print(getConfidenceIntervals('Sanders', posttuesday))
print(getConfidenceIntervals('Biden', posttuesday))
print(runTTest('Sanders', 'Biden', posttuesday))

#The actual post-super tuesday results were radically different from what was
#expected in problem 17. Polling now indicates that Biden has taken command of the primary
#with a consistent lead over Sanders in basically all regards.
#It demonstrates that statistics and correlation can't perfectly model all
#of the factors within such a complicated topic.
