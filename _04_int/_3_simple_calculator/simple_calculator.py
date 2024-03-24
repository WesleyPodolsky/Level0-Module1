"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""

from tkinter import messagebox, simpledialog, Tk
window = Tk()
window.withdraw

int1 = simpledialog.askstring(title="1/4", prompt="enter a number")
int2 = simpledialog.askstring(title="2/4", prompt="enter another number")
sign = simpledialog.askstring(title="3/4", prompt="type d to divide, m to multiply, a to add, or s to subtract")
int1= int(int1)
int2= int(int2)

finishInt = 0

if sign == 'd':
    finishInt = int1 / int2
if sign == 'm':
    finishInt = int1 * int2
if sign == 'a':
    finishInt = int1 + int2
if sign == 's':
    finishInt = int1 - int2

messagebox.showinfo(title='4/4', message=finishInt)
