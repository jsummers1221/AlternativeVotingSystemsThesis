import tkinter as tk
import ranked_ec as ranked
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
 
#https://realpython.com/python-gui-tkinter/ 
#global variables
voteRemaining = 100

#CONTROLLER METHODS
def chooseRanked():
    entry_frame.pack_forget()
    enter_candidate_frame.pack()

def createCandidate():
    #get user input
    global voteRemaining

    #check if a field is empty
    if not candidateEntry.get() or not voteEntry.get():
        error_label.config(text = f"You need to fill out both fields.", bg = "red")
        return

    name = candidateEntry.get()
    candidateEntry.delete(0, tk.END)
    vote = int(voteEntry.get())
    voteEntry.delete(0, tk.END)

    #check for errors
    if vote > voteRemaining: #cannot exceed vote remaining
        error_label.config(text = f"Error: Candidate not created. Vote assigned exceeds % of the vote remaining.", bg = "red")
        return
    
    check = ranked.getCandidate(name) #no duplicate names
    if check:
        error_label.config(text = f"Error: Candidate not created. Candidate {name} already exists.", bg = "red")
        return

    if vote < 0: #vote received cannot be negative
        error_label.config(text = f"Error: The percentage of the vote recieved cannot be less than 0.", bg = "red")
        return


    
    #create new candidate, add to list, and update vote remaining
    newCand = ranked.Candidate(name, vote)
    ranked.candidates.append(newCand)
    voteRemaining -= vote
    error_label.config(text = f"Candidate {newCand.getName()} created with {newCand.getVotes()}% of the vote.", bg = "green")
    vote_remaining_label.config(text = f"You have {voteRemaining}% of the vote left to assign.")

    #print updated candidate list to console
    ranked.printCandidates()


def donewCandidates():
    #user clicks done and transitions to next frame for choosing candidate choices if they have entered 100% of the vote
    #check that user has entered 100% of the vote (set)
    #otherwise prints out error message and does not transistion till the user enters 100% of the vote
    if voteRemaining != 0:
        error_label.config(text = f"You still have some of the vote left to assign!", bg = "red")
        return
    else:
        enter_candidate_frame.pack_forget()

        candidate_options = ranked.getNames()

        candidate_options1 = ranked.getNames()
        candidate_options1.append("")

        #how to make the option menu
        #https://stackoverflow.com/questions/45441885/how-can-i-create-a-dropdown-menu-from-a-list-in-tkinter
        #https://www.askpython.com/python-modules/tkinter/tkinter-listbox-option-menu
        candidate_option_menu = tk.OptionMenu(candidate_choices_gridframe, variable1, *candidate_options)
        candidate_option_menu.config(bg="light steel blue", fg="black")
        candidate_option_menu["menu"].config(bg="light steel blue", fg="black")

        second_choices_option_menu = tk.OptionMenu(candidate_choices_gridframe, variable2, *candidate_options1)
        second_choices_option_menu.config(bg="light steel blue", fg="black")
        second_choices_option_menu["menu"].config(bg="light steel blue", fg="black")

        third_choices_option_menu = tk.OptionMenu(candidate_choices_gridframe, variable3, *candidate_options1)
        third_choices_option_menu.config(bg="light steel blue", fg="black")
        third_choices_option_menu["menu"].config(bg="light steel blue", fg="black")

        candidate.grid(row=0, column=0, padx=5, pady=5)
        candidate_option_menu.grid(row=0, column=1, padx=5, pady=5)
        candidate_second_choice.grid(row=1, column=0, padx=5, pady=5)
        second_choices_option_menu.grid(row=1, column=1, padx=5, pady=5)
        candidate_third_choice.grid(row=2, column=0, padx=5, pady=5)
        third_choices_option_menu.grid(row=2, column=1, padx=5, pady=5)
        create_choice_button.grid(row=3, column=0, padx=5, pady=5)
        calculate_results.grid(row=3, column=1, padx=5, pady=5)
        enter_candidate_choices_frame.pack()


def enterChoices():
    candName = variable1.get()
    secondChoice = variable2.get()
    thirdChoice = variable3.get()

    if (candName == secondChoice) or (candName == thirdChoice) or ((secondChoice == thirdChoice) and (secondChoice != "")):
        choices_error_label.config(text="You cannot select the same candidate in more than one dropdown menu.", bg ="red")
        return
    elif (candName == "Pick a Candidate") or (secondChoice == "Pick a Candidate") or (thirdChoice == "Pick a Candidate"):
        choices_error_label.config(text="You must either select a candidate or select no candidate", bg ="red")
        return
    else:
        candObject = ranked.getCandidate(candName)
        candObject.set2ndChoice(secondChoice)
        candObject.set3rdChoice(thirdChoice)
        choices_error_label.config(text=f"Candidate {candObject.getName()} has second choice {candObject.get2ndChoice()} and third choice {candObject.get3rdChoice()}", bg = "green")
        
        ranked.printCandidates()
        return

def calculateResults():
    enter_candidate_choices_frame.pack_forget()
    #results frame
    results_frame = tk.Frame(window)
    results_gridframe = tk.Frame(results_frame)

    #FPTP results (do this first)
    FPTP_results_frame = tk.Frame(results_gridframe)
    FPTP_results_label = tk.Label(master=FPTP_results_frame, text="FPTP Voting Simulation")
    FPTP_results_label.pack()
    #run the election
    fptpWinner = ranked.runFPTPElection()
    fptp_message = tk.Label(master=FPTP_results_frame, text =f"Winner: Candidate {fptpWinner[0]} with {fptpWinner[1]}% of the votes won Arizona’s 11 EC votes.")
    fptp_message.pack()
    #create pie chart


    #ranked results (do this second)
    ranked_results_frame= tk.Frame(results_gridframe)
    ranked_results_label = tk.Label(master=ranked_results_frame, text="Ranked Voting Simulation")
    ranked_results_label.pack()
    #run the election
    rankedWinner = ranked.runRankedElection()
    if type(rankedWinner) == list:
        ranked_message = tk.Label(master=ranked_results_frame, text = f"Winner: Candidate {rankedWinner[0]} with {rankedWinner[1]}% of the votes after {rankedWinner[2]} rounds won Arizona’s 11 EC votes.")
        ranked_message.pack()
    elif type(rankedWinner) == str:
        ranked_message = tk.Label(master=ranked_results_frame, text = rankedWinner)
        ranked_message.pack()
    #create the graph

    
    #pack both election result frames
    ranked_results_frame.grid(row=0, column=0, padx=5, pady=5)
    FPTP_results_frame.grid(row=0, column=1, padx=5, pady=5)
    results_gridframe.pack()
    return_to_main_menu_button = tk.Button(master=results_frame, text="Return to Main Menu", width=25, height=5, bg="light steel blue", fg="black",command=lambda: mainMenu()) 
    return_to_main_menu_button.pack()
   



    results_frame.pack()

def mainMenu():
    results_frame.pack_forget()
    ranked.candidates.clear()
    entry_frame.pack()
    
#VIEW (GUI)
window = tk.Tk()
window.geometry("500x500")

entry_frame = tk.Frame(window, width=1000, height=450)
#entry_frame.grid(column=0, row=0)

#PICK SCENARIO
label1 = tk.Label(master=entry_frame, text="Pick your scenario:")
label1.pack()

button1 = tk.Button(master=entry_frame, text="Ranked Voting vs. FPTP", width=25, height=5, bg="light steel blue", fg="black", command=lambda: chooseRanked())
#https://stackoverflow.com/questions/6874525/how-to-handle-a-button-click-event
#button1.grid(column=1, row =0)
button1.pack()

entry_frame.pack()

#CANDIDATE ENTRY
enter_candidate_frame = tk.Frame(window)
candidate_gridframe = tk.Frame(enter_candidate_frame)

vote_remaining_label = tk.Label(master=enter_candidate_frame, text=f"You have {voteRemaining}% of the vote left to assign.")
vote_remaining_label.pack()

#https://www.geeksforgeeks.org/how-to-change-the-tkinter-label-text/
candidate_entry_label = tk.Label(master=candidate_gridframe, text="Enter the candidate name (string):")
candidate_entry_label.grid(row=0, column=0, padx=5, pady=5)
candidateEntry = tk.Entry(master=candidate_gridframe)
candidateEntry.grid(row=0, column=1, padx=5, pady=5)

vote_entry_label = tk.Label(master=candidate_gridframe, text="Enter the percentage of the vote recieved (integer):")
vote_entry_label.grid(row=1, column=0, padx=5, pady=5)
voteEntry = tk.Entry(master=candidate_gridframe)
voteEntry.grid(row=1, column=1, padx=5, pady=5)


create_candidate_button = tk.Button(master=candidate_gridframe, text="Create Candidate", width=25, height=5, bg="light steel blue", fg="black", command=lambda: createCandidate()) 
#https://stackoverflow.com/questions/6874525/how-to-handle-a-button-click-event

done_button = tk.Button(master=candidate_gridframe, text="Done", width=25, height=5, bg="light steel blue", fg="black",command=lambda: donewCandidates()) 

create_candidate_button.grid(row=2, column=0, padx=5, pady=5)
done_button.grid(row=2, column=1, padx=5, pady=5)
candidate_gridframe.pack()
error_label = tk.Label(master = enter_candidate_frame, text="")
error_label.pack()

#Candidate Choices entry
enter_candidate_choices_frame = tk.Frame(window)

choices_error_label = tk.Label(master=enter_candidate_choices_frame, text="")

candidate_choices_label = tk.Label(master=enter_candidate_choices_frame, text="Enter the second and third choices for each candidate:")
candidate_choices_label.pack()

candidate_choices_gridframe = tk.Frame(enter_candidate_choices_frame)
create_choice_button = tk.Button(master=candidate_choices_gridframe, text="Create Choices", width=25, height=2, bg="light steel blue", fg="black", command=lambda: enterChoices())
calculate_results = tk.Button(master=candidate_choices_gridframe, text="Calculate Results", width=25, height=2, bg="light steel blue", fg="black", command=lambda: calculateResults())

candidate = tk.Label(master=candidate_choices_gridframe, text="Candidate:")
candidate_second_choice = tk.Label(master=candidate_choices_gridframe, text="Second Choice:")
candidate_third_choice = tk.Label(master=candidate_choices_gridframe, text="Third Choice:")

empty_list = ["empty"]
candidate_option_menu = tk.OptionMenu(candidate_choices_gridframe, empty_list[0], empty_list)
second_choices_option_menu = tk.OptionMenu(candidate_choices_gridframe, empty_list[0], empty_list)
third_choices_option_menu = tk.OptionMenu(candidate_choices_gridframe, empty_list[0], empty_list)

#this is where i made them global
candidate_options = ["Pick a Candidate"]

candidate_options1 = ["Pick a Candidate"]

variable1 = tk.StringVar(window)
variable1.set(candidate_options[0]) #this specifies default value

variable2 = tk.StringVar(window)
variable2.set(candidate_options1[0]) #this specifies default value

variable3 = tk.StringVar(window)
variable3.set(candidate_options1[0]) #this specifies default value

candidate_choices_gridframe.pack()
choices_error_label.pack()

window.mainloop()

