"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
from tkinter import messagebox, simpledialog, Tk

window = Tk()
window.withdraw()

q1 = simpledialog.askstring(title="1/3", prompt="What is the atomic number for carbon on the Periodic Table?")
q2 = simpledialog.askstring(title="2/3", prompt="How many arms does an octopus have?")
q3 = simpledialog.askstring(title="3/3", prompt="Should you program at the League?")
score = 0

if q1 == '6':
    score +=1
if q2 == '8':
    score +=1
if q3 == 'yes' or q3 == 'Yes' or q3 == 'YES':
    score +=1

messagebox.showinfo(title='4/4', message=score)


