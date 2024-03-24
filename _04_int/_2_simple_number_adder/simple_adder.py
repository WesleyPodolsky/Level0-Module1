"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""
from tkinter import messagebox, simpledialog, Tk
window = Tk()
window.withdraw

int1 = simpledialog.askstring(title="1/3", prompt="enter a number")
int2 = simpledialog.askstring(title="2/3", prompt="enter another number")
messagebox.showinfo(title="3/3", message=int(int1) + int(int2))
