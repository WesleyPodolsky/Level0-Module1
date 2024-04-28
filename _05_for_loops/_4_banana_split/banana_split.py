"""
* 1. Look at the image bananasplit.png

* 2. Your mission is to create a python program that recreates that image
     using the create_text function
     
* 3. The catch is, you can only type the create_text function ONE TIME ONLY
     into your program. Using a loop and if-statements, you must figure out
     how to vary the text and the positioning so that you can read all four
     separate lines.
"""

from tkinter import *
import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=200, height=200, bg="#FF00FF");
canvas.grid()

'''
Text Rendering Example:
                    x    y                                                       

'''
# Put your code below
canvas.create_text(100, 50, text="sprinkles", font=("Arial", 16))
canvas.create_text(100, 75, text="chocolate syrup", font=("Arial", 16))
canvas.create_text(100, 100, text="icecream scoop x3", font=("Arial", 16))
canvas.create_text(100, 125, text="banana", font=("Arial", 16))

root.mainloop()
