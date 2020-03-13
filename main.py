from utils import *
from poll import Poll

df = loadAndCleanData("2020_democratic_presidential_nomination-6730.csv")

# Create a list of poll objects from my dataframe
pollNames = pd.unique(df["Poll"])
print(pollNames)

polls = []
for name in pollNames:
    poll = Poll(name, df)
    polls.append(poll)
    print(poll.outlet)
    print(poll.getMostRecentPoll())
    print("Number of polls: " + str(poll.countPoll()))
    print("Change in poll for Sanders " + str(poll.changeInPoll("Sanders")))
    print("Average in poll for Sanders " + str(poll.avgInPoll("Gabbard")))

#print(polls)
