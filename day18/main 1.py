from turtle import Turtle, Screen
from random import randint,choice

tim = Turtle()
screen = Screen()
screen.colormode(255)

def random_walk():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    n= choice([0,90,180,270])
    #n = randint(-90,90)
    tim.pensize(5)
    tim.speed("fastest")
    tim.color((r,g,b))
    tim.forward(20)
    tim.setheading(n)
    

for w in range(1,1000):
    random_walk()

def square():
    for l in range(4):
        tim.forward(100)
        tim.left(90) 

""" for l in range(20):
    tim.pendown()
    tim.forward(5)
    tim.penup()
    tim.forward(5) """

def polygon(n):
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    tim.color((r,g,b))
    angle = 360/n
    for l in range(n):
        tim.forward(100)
        tim.left(angle)
        
        
""" for n in range(3,12):
    polygon(n)
 """


screen.exitonclick()


     
        