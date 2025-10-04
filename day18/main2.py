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
    


def spiro():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    n= choice([0,90,180,270])
    #n = randint(-90,90)
    tim.pensize(2)
    tim.speed("fastest")
    tim.color((r,g,b))
    tim.circle(80)



for n in range(0,360,10):
    spiro()
    tim.setheading(-n)

screen.exitonclick()


     
        