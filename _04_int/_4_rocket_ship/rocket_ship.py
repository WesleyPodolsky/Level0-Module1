from tkinter import *

window_width = 800
window_height = 800
root = Tk()

canvas = Canvas(root, width=window_width, height=window_height, borderwidth=0, highlightthickness=0, bg="#000050")
canvas.grid()


# This code runs whenever the mouse is clicked on the window
def mouse_pressed(event):
    # Draws a dark blue background
    canvas.create_rectangle(0, 0, window_width, window_height, fill="#000050")

    # x and y will be equal to the mouse pointer's x and y location
    x = event.x
    y = event.y
    
    # This defines the x and y coordinated of all three points
    # of a triangle
    points = [x, y, x - 50, y + 100, x + 50, y + 100]
    canvas.create_polygon(points, fill='maroon', width=2) # draws triangle

    points4 = [x - 50, y + 535, x + 50, y + 425]
    canvas.create_oval(points4, fill='yellow', width=2)

    points = [x-50, y+486, x +50, y+486, x, y + 586]
    canvas.create_polygon(points, fill='yellow', width=2)  # draws triangle

    # 1. Add details to your rocket to make it look better. You can look at
    #    rocket.png for inspiration.
    points2 = [x-50, y+100, x-50, y+300, x+50, y+300, x+50, y+100]
    canvas.create_polygon(points2, fill='gray', width=2)
    # 2. Modify the locations of the shapes above so the rocket will be drawn
    #    where the mouse is clicked

    points3 = [x - 50, y + 300, x - 80, y + 450, x + 80, y + 450, x + 50, y + 300]
    canvas.create_polygon(points3, fill='gray', width=2)


# ====================== DO NOT MODIFY THE CODE BELOW ========================

canvas.bind("<Button-1>", mouse_pressed)

root.mainloop()
