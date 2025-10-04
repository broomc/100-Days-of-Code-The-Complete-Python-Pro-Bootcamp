from turtle import Turtle, Screen
from random import randint,choice

tim = Turtle()
screen = Screen()
screen.setup(width=400, height=400)
#screen.tracer(0)
screen.colormode(255)

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
    #tim.clear()
    spiro()
    tim.setheading(-n)
    screen.update()
    screen.getcanvas().postscript(file=f"frame_{n:03d}.ps")

screen.exitonclick()


     
        