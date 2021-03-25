#MODEL
candidates = []
#how to search thru list of objects for an object with an attribute equal to some value
#next((x for x in test_list if x.value == value), None)
#https://stackoverflow.com/questions/7125467/find-object-in-list-that-has-attribute-equal-to-some-value-that-meets-any-condi 


class Candidate:
    candidateName = ""
    percentVote = 0
    secondChoice = ""
    thirdChoice = ""

    def __init__(self, name, percent):
        self.candidateName = name
        self.percentVote = percent

    def setName(self, name):
        self.candidateName = name

    def getName(self):
        return self.candidateName

    def setVotes(self, vote):
        self.percentVote = vote

    def getVotes(self):
        return self.percentVote
    
    def set2ndChoice(self, name):
        self.secondChoice = name

    def get2ndChoice(self):
        return self.secondChoice
    
    def set3rdChoice(self, name):
        self.thirdChoice = name
    
    def get3rdChoice(self):
        return self.thirdChoice

    def print(self):
        info = f"Candidate: {self.candidateName}, Vote Received: {self.percentVote}, 2nd: {self.secondChoice}, 3rd: {self.thirdChoice}"
        print(info)

def getNames():
    names_list = []
    for cand in candidates:
        names_list.append(cand.getName())
    return names_list
    
def getCandidate(name):
    for cand in candidates:
        if cand.getName() == name:
            return cand
    return None

def printCandidates():
    print("Candidates:")
    for cand in candidates:
        cand.print()

def runRankedElection():

    won = False
    losingCandidate = ""
    winningCandidate = ""
    winningCandidateName = ""
    numRounds = 0

    print("Ranked Round: %d" % numRounds)
    printCandidates()

    while won == False:
        numRounds += 1
        #see if there's a winner
        for candidate in candidates:
            if candidate.getVotes() > 50:
                won = True
                winningCandidate = candidate
                return [winningCandidate.candidateName, winningCandidate.getVotes(), numRounds, winningCandidate,]
        
        #remove lowest candidate
        minVote = 100
        for candidate in candidates:
            if candidate.getVotes() < minVote:
                losingCandidate = candidate
                minVote = candidate.getVotes()
    
        #give loser's votes to 2nd or 3rd choice
        #https://stackoverflow.com/questions/598398/searching-a-list-of-objects-in-python
        #search thru a list of objects for an attribute value
        #if any(x for x in candidates if x.getName == losingCandidate.get2ndChoice()):
        #    nextCandidate = getCandidate(losingCandidate.get2ndChoice())
        #   nextCandidate.setVotes(nextCandidate.getVotes() + losingCandidate.getVotes())
        #elif any(x for x in candidates if x.getName == losingCandidate.get3rdChoice()):
        #    nextCandidate = getCandidate(losingCandidate.get3rdChoice())
        #   nextCandidate.setVotes(nextCandidate.getVotes() + losingCandidate.getVotes())
        nextCandidate = getCandidate(losingCandidate.get2ndChoice())
        if nextCandidate is not None:
            nextCandidate.setVotes(nextCandidate.getVotes() + losingCandidate.getVotes())
        else:
            nextCandidate = getCandidate(losingCandidate.get3rdChoice())
            if(nextCandidate):
                nextCandidate.setVotes(nextCandidate.getVotes() + losingCandidate.getVotes())

        if len(candidates) > 1:
            candidates.remove(losingCandidate)
            print("Removed Candidate %s and gave their votes to Candidate %s" % (losingCandidate.getName(), nextCandidate.getName()))
            print("Ranked Round: %d" % numRounds)
            printCandidates()

        else:
            print("Ranked Round: %d" % numRounds)
            printCandidates()
            return "No winner :c. No candidate reached over 50% after all others were eliminated. In this situation, a manual run-off election will have to be held."

    return [winningCandidate.candidateName, winningCandidate.getVotes(), numRounds, winningCandidate,]
    #pass

def runFPTPElection():
    #How AZ Electoral College Elections work:
    #https://www.azcleanelections.gov/how-government-works/electoral-college#:~:text=Arizona%20has%20a%20winner%20take,both%20president%20and%20vice%2Dpresident.
    #Summary: Winner-take-all. Whoever receives the highest number of votes receives all 11 electoral votes.
    maxVote = 0
    maxCandidate = "" #a candidate object
    maxName = ""

    for candidate in candidates:
        if candidate.percentVote > maxVote:
            maxVote = candidate.percentVote
            maxName = candidate.candidateName
            maxCandidate = candidate
    
    return [maxName, maxVote, maxCandidate]





