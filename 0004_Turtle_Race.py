import turtle
import random

print("Turtle race")

turtle.getscreen()
turtle.bgcolor("white")

# Creating a turtle t with random colors of the line created.
t = turtle.Turtle()
randx = random.randrange(0,100,1)/100; randy = random.randrange(0,100,1)/100; randz = random.randrange(0,100,1)/100
t.pen(pencolor=(randx,randy,randz), fillcolor=(randx,randy,randz))

#Creating a turtle 'c' with random colors of the line created.
c = turtle.Turtle()
randx = random.randrange(0,100,1)/100; randy = random.randrange(0,100,1)/100; randz = random.randrange(0,100,1)/100
c.pen(pencolor=(randx,randy,randz), fillcolor=(randx,randy,randz))

t.clear()
c.clear()

t.penup()
c.penup()

t.goto(-300,-50)
c.goto(-300,50)

t.pendown()
c.pendown()

t.speed(2)
c.speed(2)

final_distance = 1200
distance = 0
while final_distance > distance:

    t.fd(random.randrange(0,10,1))
    c.fd(random.randrange(0,10,1))
    distance = distance + 10 
