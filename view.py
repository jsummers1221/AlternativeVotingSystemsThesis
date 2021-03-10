import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
 
def chooseRanked():
    entry_frame.pack_forget()
    enter_candidate_frame.pack()

def createCandidate():
    #creates the candidate object and adds to candidate list
    #updates percentage of vote left
    print()

def donewCandidates():
    #user clicks done and transitions to next frame for choosing candidate choices if they have entered 100% of the vote
    #check that user has entered 100% of the vote (set)
    #otherwise prints out error message and does not transistion till the user enters 100% of the vote
    print()


def enterChoices():
    print()

window = tk.Tk()

entry_frame = tk.Frame(window, width=1000, height=450)
entry_frame.pack()

label1 = tk.Label(master=entry_frame, text="Pick your scenario:")
label1.pack()

button1 = tk.Button(master=entry_frame, text="Ranked Voting vs. FPTP", width=25, height=5, bg="light steel blue", fg="black", command=lambda: chooseRanked()) 
#https://stackoverflow.com/questions/6874525/how-to-handle-a-button-click-event

button1.pack()

enter_candidate_frame = tk.Frame(window, width=1000, height=450)
label2 = tk.Label(master=enter_candidate_frame, text="Enter your candidates")
label2.pack()
entry1 = tk.Entry(master=enter_candidate_frame)
entry1.pack()

label3 = tk.Label(master=enter_candidate_frame, text="Enter the percentage of the vote recieved:")
label3.pack()
entry2 = tk.Entry(master=enter_candidate_frame)
entry2.pack()

create_candidate_button = tk.Button(master=enter_candidate_frame, text="Create Candidate", width=25, height=5, bg="light steel blue", fg="black", command=lambda: createCandidate()) 
#https://stackoverflow.com/questions/6874525/how-to-handle-a-button-click-event

done_button = tk.Button(master=enter_candidate_frame, text="Done", width=25, height=5, bg="light steel blue", fg="black",) 

create_candidate_button.pack()
done_button.pack()

window.mainloop()

