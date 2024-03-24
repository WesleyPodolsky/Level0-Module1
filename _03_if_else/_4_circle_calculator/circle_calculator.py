# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.
import math
import tkinter as tk
from tkinter import simpledialog
root = tk.Tk()
import turtle

radius = simpledialog.askstring(title='1/2', prompt='enter a radius')
choice = simpledialog.askstring(title='2/2', prompt='type c for circumference and a for area')
turtle.circle(int(radius))
if choice == 'c':
    turtle.penup()
    turtle.goto(-200,-100)
    print('circumference is ' + str((2*int(radius) * math.pi)))
    turtle.write(arg='circumference is ' + str((2*int(radius) * math.pi)), move= True, align= 'left', font=('Arial', 50, 'normal'))


elif choice == 'a':
    turtle.penup()
    turtle.goto(-200,-100)
    print('area is ' + str((int(radius)*int(radius) * math.pi)))
    turtle.write(arg='area is ' + str((int(radius)*int(radius) * math.pi)), move= True, align= 'left', font=('Arial', 50, 'normal'))

turtle.done()
