# Alternative Voting Systems Thesis & Simulation
Honors Thesis and Creative Project by Autumn Martin and Jack Summers <br>
Barrett, The Honors College at Arizona State University <br>

This application compares Ranked Voting (Instant Run-off Voting) with the current First-Past-The-Post (plurality) in a simulated Arizona Presidential Election.

## Instructions:##
Download and run the AV_Simulation executable file. 
The application interface and console will open.


# Selecting the Scenario
Pick the "Ranked Voting vs. FPTP: Arizona Presidential Election" scenario. <br>
In the future, more scenarios can be added. <br>

# Entering the Candidates
Here you will enter candidate names and the percentage of the vote they recieved.
1. Click "Create Candidate" once you have entered the information.
2. Continue creating candidates until you have assigned 100% of the vote.
3. Then, click "Done".
The message at the top tells you how much of the vote you have left to assign.

Click the Undo button to delete the last candidate you entered.
Click the Delete button to delete all the candidates entered so far.

The "Use 2016/2020..." buttons will load real candidate information from those election years and use that instead.

# Entering the Ranked Choices
Here you may enter Ranked Choices for the Ranked Voting simulation.
Normally, a voter would rank candidates on their ballot.
But this simulation uses a simplified version where ranking is done at the candidate level.

1. Pick a Candidate for the "Candidate:" drop-down menu.
2. Pick candidates for the 2nd and 3rd choices.
3. Click "Create Choices".
4. If that Candidate is eliminated, their vote percentage will be given to the next choice candidate.
5. Click "Calculate Results" when you are done.

If you want:
You don't have to enter choices for all the candidates.
You can assign a 2nd choice and not assign a 3rd.
You can enter no choices at all and skip this
part by clicking "Calculate Results."

# Viewing the Results
Here you can see the results of both simulated elections.
Each round of the Ranked Voting algorithm:
1. Checks for a winner (> 50%). 
2. If no winner, eliminates the lowest candidate 
and gives their votes to their next choice if possible.