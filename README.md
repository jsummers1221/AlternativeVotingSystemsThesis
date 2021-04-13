# Alternative Voting Systems Simulation
Honors Creative Project by Autumn Martin and Jack Summers <br>
Barrett, The Honors College at Arizona State University <br>

This application compares a Ranked (Instant Run-off) Voting System with the current First-Past-The-Post (plurality) Voting System in a simulated Arizona Presidential Election.


# Instructions:
Download and run the AV_Simulation executable file. This can ONLY be run on WINDOWS OS.
The application and console will open. This may take 15-30 seconds as the file loads. <br>
The console will print out the candidate list when it is updated and will
show you the Ranked Voting rounds in more detail.

To run the source code for the application, install Python 3.9.0 or greater and
install the matplotlib library (we used version 3.3.4). The rest of the libraries
are included in the standard library. Then, run view_controller.py to start the program. <br>
1. Download Python from here: https://www.python.org/downloads/
2. In windows powershell, do the following:
3. Run "pip install matplotlib" to install matplotlib.
4. Navigate to the directory with the python files and run "python .\view_controller.py"

Follow the instructions below to operate the program. Here is an additional video demonstration, too: <br>
https://youtu.be/kJUaOTUTidg <br>

## Select the Scenario
![](/images/pickscenario.png?raw=true) <br>
Pick the "Ranked Voting vs. FPTP: Arizona Presidential Election" scenario. <br>
In the future, more scenarios can be added. <br>

## Entering the Candidates
![](/images/createcandidates.png?raw=true) <br>
Here you will enter candidate names and the percentage of the vote they recieved.
1. Click "Create Candidate" once you have entered the information.
2. Continue creating candidates until you have assigned 100% of the vote.
3. Then, click "Done".
The message at the top tells you how much of the vote you have left to assign. <br>
The green/red status message will describe success or error messages. <br>

Click the Undo button to delete the last candidate you entered.<br>
Click the Delete button to delete all the candidates entered so far.<br>
The "Use 2016/2020..." buttons will load real candidate information from those election years and use that instead.<br>

## Entering the Ranked Choices
![](/images/createchoices.png?raw=true) <br>
Here you may enter Ranked Choices for the Ranked Voting simulation. <br>
Normally, a voter would rank candidates on their ballot,
but this simulation uses a simplified version where ranking is done at the candidate level.
1. Pick a Candidate for the "Candidate:" drop-down menu.
2. Pick candidates for the 2nd and 3rd choices.
3. Click "Create Choices".
4. If that Candidate is eliminated, their vote percentage will be given to the next choice candidate.
5. Click "Calculate Results" when you are done.
The green/red status message will describe success or error messages. <br>

If you want:
* You don't have to enter choices for all the candidates.
* You can assign a 2nd choice and not assign a 3rd by choosing the blank option in the drop-down.
* You can enter no choices at all and skip this
part by clicking "Calculate Results."
* However, not using choices means you will not use the functionality of Ranked Voting.

## Viewing the Results
![](/images/results.png?raw=true) <br>
Here you can see the results of both simulated elections. <br>
The Ranked Voting algorithm requires that a candidate have over 50% of the vote to win.
Each round:
1. Checks for a winner (> 50%). 
2. If no winner, eliminates the lowest candidate 
and gives their votes to their next choice if possible.

The FPTP algorithm simply declares the candidate with the most votes as the winner,
even if they have less than 50% of the vote.

## Running Another Simulation
To simulate another election, close the application and run it again using the instructions above.