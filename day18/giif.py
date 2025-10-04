import turtle

# Setup
screen = turtle.Screen()
screen.tracer(0)  # Turn off auto-update for manual frame control

# Your drawing code here
# Example: animate a moving circle
circle = turtle.Turtle()
circle.penup()

for i in range(100):
    circle.clear()
    circle.goto(i, 0)
    circle.dot(20)
    screen.update()
    screen.getcanvas().postscript(file=f"frame_{i:03d}.ps")  # Save frame as .ps