import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
import turtle
    # Ask the user what shape they want to draw and store it in a variable
simpleShape = simpledialog.askstring(title='1/1', prompt='want to draw a triangle, square, or circle? Write t for triangle, s for square, or c for circle!')
    # Draw the shape requested by the user using if-elif-else statements
if simpleShape == "s":
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
elif simpleShape == 't':
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)
elif simpleShape == 'c':
    turtle.circle(100)

    # Call the turtle .done() method
turtle.done()
