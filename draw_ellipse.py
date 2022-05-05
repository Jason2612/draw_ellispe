from random import random
import turtle
t = turtle.Turtle()
rad = 100

count = 0
while count < 3:
    t.circle(rad, 90)
    t.circle(rad//2, 90)
    count += 1


    
turtle.done()