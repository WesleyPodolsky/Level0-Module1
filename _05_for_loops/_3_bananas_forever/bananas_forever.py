"""
 * Write a python program that prints the word 'banana' one thousand (1,000) times
"""
import turtle
number = 0
turtle.penup()
sigma=-350
turtle.goto(400, -350)
for i in range(1000):
    turtle.speed(0)
    turtle.write('erm, what the sigma?')
    number = number + 1
    turtle.left(90)
    turtle.forward(7)
    sigma = sigma + 7
    turtle.right(90)
    if sigma > 350:
        turtle.right(90)
        turtle.forward(600)
        sigma = -350
        turtle.right(270)
        turtle.forward(-79.3)
        turtle.sety(-350)

turtle.done()