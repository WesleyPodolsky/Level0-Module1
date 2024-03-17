import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    radius = simpledialog.askinteger(title='1/1', prompt='Enter a radius')
    radius = int(radius)

    # Make a new turtle
    import turtle
    # Have your turtle draw a circle with the correct radius
    turtle.circle(radius)

    # Call the turtle .penup() method
    turtle.penup()
    # Move your turtle to a new x,y position using .goto()
    turtle.goto(-100,-300)
    # Calculate the area of your circle and store it in a variable
    # Hint, you can use math.pi
    area = (radius*radius) * math.pi
    # Write the area of your circle using the turtle .write() method
    turtle.write(arg="area = " + str(area), move=True, align='left', font=('Arial',20,'normal'))

    # Hide your turtle
    turtle.hideturtle()
    # Call turtle.done()
    turtle.done()