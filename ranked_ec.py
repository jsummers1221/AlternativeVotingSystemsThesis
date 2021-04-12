#MODEL
candidates = []
rounds_names = dict()
rounds_votes = dict()
rounds_msg = dict()
#how to search thru list of objects for an object with an attribute equal to some value
#next((x for x in test_list if x.value == value), None)
#https://stackoverflow.com/questions/7125467/find-object-in-list-that-has-attribute-equal-to-some-value-that-meets-any-condi 


class Candidate:
    #candidateName = ""
    #percentVote = 0
    #secondChoice = ""
    #thirdChoice = ""

    def __init__(self, name, percent):
        self.candidateName = name
        self.percentVote = percent
        self.secondChoice = ""
        self.thirdChoice = ""

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

def getVotes():
    votes_list = []
    for cand in candidates:
        votes_list.append(cand.getVotes())
    return votes_list
    
def getCandidate(name):
    for cand in candidates:
        if cand.getName() == name:
            return cand
    return None

def printCandidates():
    print("Candidates:")
    for cand in candidates:
        cand.print()

def undoAddCandidate():
    if len(candidates) > 0:
        removed = candidates.pop()
        msg = f"Removed previously added Candidate {removed.getName()} with {removed.getVotes()}% of the vote."
        print(msg)
        printCandidates()
        return [msg, removed.getVotes()]
    else:
        msg = "The candidate list is empty and there is nothing to undo."
        return [msg, 0]

def deleteCandidates():
    if len(candidates) > 0:
        candidates.clear()
        print("Emptied the candidate list.")
        printCandidates()
        return "Emptied the candidate list."
    else:
        return "The candidate list is already empty."

def deleteChoices():
    for cand in candidates:
        cand.set2ndChoice("")
        cand.set3rdChoice("")
    print("Removed all 2nd and 3rd choices from all candidates.")
    printCandidates()
    return "Removed all 2nd and 3rd choices from all candidates."

def runRankedElection():
    #How Ranked Elections Work:
    #https://www.cgpgrey.com/politics-in-the-animal-kingdom
    #https://www.youtube.com/watch?v=3Ez3aEUjRQo&feature=youtu.be 
    won = False
    losingCandidate = ""
    winningCandidate = ""
    winningCandidateName = ""
    numRounds = 0
    #update info for pie charts
    rounds_names[numRounds] = getNames()
    rounds_votes[numRounds] = getVotes()

    print("Initial Candidates:")
    printCandidates()
    

    while won == False:
        numRounds += 1
        #see if there's a winner
        for candidate in candidates:
            if candidate.getVotes() > 50:
                won = True
                winningCandidate = candidate
                print("Ranked Round: %d" % numRounds)
                #update info for the pie charts
                rounds_names[numRounds] = getNames()
                rounds_votes[numRounds] = getVotes()
                return [winningCandidate.candidateName, winningCandidate.getVotes(), numRounds, winningCandidate,]
        
        #remove lowest candidate
        #find candidate to remove
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

        #find loser's 2nd or 3rd choice if they exist & give them the loser's votes
        nextCandidate = getCandidate(losingCandidate.get2ndChoice())
        if nextCandidate is not None:
            nextCandidate.setVotes(nextCandidate.getVotes() + losingCandidate.getVotes())
        else:
            nextCandidate = getCandidate(losingCandidate.get3rdChoice())
            if(nextCandidate):
                nextCandidate.setVotes(nextCandidate.getVotes() + losingCandidate.getVotes())

        #remove the loser unless they are the last one left
        if len(candidates) > 1: 
            candidates.remove(losingCandidate)
            print("Ranked Round: %d" % numRounds)
            if nextCandidate:
                print("Removed Candidate %s and gave their votes to Candidate %s" % (losingCandidate.getName(), nextCandidate.getName()))
                msg = "Removed Candidate %s and gave their votes to Candidate %s" % (losingCandidate.getName(), nextCandidate.getName())
            else:
                print("Removed Candidate %s and gave their votes to no one since they had no next choices." % (losingCandidate.getName()))
                msg = "Removed Candidate %s and gave their votes to no one since they had no next choices." % (losingCandidate.getName())
            printCandidates()
            
            #update info for pie charts
            rounds_names[numRounds] = getNames()
            rounds_votes[numRounds] = getVotes()
            rounds_msg[numRounds] = msg

        else:
            print("Ranked Round: %d" % numRounds)
            printCandidates()
            #update info for pie charts
            rounds_names[numRounds] = getNames()
            rounds_votes[numRounds] = getVotes()
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





