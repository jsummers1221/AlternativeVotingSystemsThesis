import ranked_ec as ranked

cand1 = ranked.Candidate("A", 50)
cand2 = ranked.Candidate("B", 50)
#cand3 = ranked.Candidate("C", 25)

cand1.set2ndChoice("B")
cand1.set3rdChoice("C")

cand2.set2ndChoice("C")
cand2.set3rdChoice("A")

#cand3.set2ndChoice("B")
#cand3.set3rdChoice("A")

ranked.candidates.append(cand1)
ranked.candidates.append(cand2)
#ranked.candidates.append(cand3)

fptpWinner = ranked.runFPTPElection()
print(f"FPTP Winner: Candidate {fptpWinner[0]} with {fptpWinner[1]}% of the votes won Arizona’s 11 EC votes.")

rankedWinner = ranked.runRankedElection()
if type(rankedWinner) == list:
       print(f"Ranked Winner: Candidate {rankedWinner[0]} with {rankedWinner[1]}% of the votes after {rankedWinner[2]} rounds won Arizona’s 11 EC votes.")
elif type(rankedWinner) == str:
    print(rankedWinner)