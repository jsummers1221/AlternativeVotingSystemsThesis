import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
 
#https://realpython.com/python-gui-tkinter/ 

def chooseRanked():
    entry_frame.pack_forget()
    enter_candidate_frame.pack()

def createCandidate():
    #creates the candidate object and adds to candidate list
    #updates percentage of vote left
    vote_remaining_label.config(text = "You have 50% of the vote left to assign.")


def donewCandidates():
    #user clicks done and transitions to next frame for choosing candidate choices if they have entered 100% of the vote
    #check that user has entered 100% of the vote (set)
    #otherwise prints out error message and does not transistion till the user enters 100% of the vote
    pass


def enterChoices():
    pass

window = tk.Tk()
window.geometry("500x500")

entry_frame = tk.Frame(window, width=1000, height=450)
#entry_frame.grid(column=0, row=0)

label1 = tk.Label(master=entry_frame, text="Pick your scenario:")
label1.pack()

button1 = tk.Button(master=entry_frame, text="Ranked Voting vs. FPTP", width=25, height=5, bg="light steel blue", fg="black", command=lambda: chooseRanked())
#https://stackoverflow.com/questions/6874525/how-to-handle-a-button-click-event
#button1.grid(column=1, row =0)
button1.pack()

entry_frame.pack()

enter_candidate_frame = tk.Frame(window)
candidate_gridframe = tk.Frame(enter_candidate_frame)
vote_remaining_label = tk.Label(master=enter_candidate_frame, text="You have 100% of the vote left to assign.")
vote_remaining_label.pack()

#https://www.geeksforgeeks.org/how-to-change-the-tkinter-label-text/
candidate_entry_label = tk.Label(master=candidate_gridframe, text="Enter your candidates:")
candidate_entry_label.grid(row=0, column=0, padx=5, pady=5)
candidateEntry = tk.Entry(master=candidate_gridframe)
candidateEntry.grid(row=0, column=1, padx=5, pady=5)

vote_entry_label = tk.Label(master=candidate_gridframe, text="Enter the percentage of the vote recieved:")
vote_entry_label.grid(row=1, column=0, padx=5, pady=5)
voteEntry = tk.Entry(master=candidate_gridframe)
voteEntry.grid(row=1, column=1, padx=5, pady=5)

create_candidate_button = tk.Button(master=candidate_gridframe, text="Create Candidate", width=25, height=5, bg="light steel blue", fg="black", command=lambda: createCandidate()) 
#https://stackoverflow.com/questions/6874525/how-to-handle-a-button-click-event

done_button = tk.Button(master=candidate_gridframe, text="Done", width=25, height=5, bg="light steel blue", fg="black",) 

create_candidate_button.grid(row=2, column=0, padx=5, pady=5)
done_button.grid(row=2, column=1, padx=5, pady=5)
candidate_gridframe.pack()

window.mainloop()

