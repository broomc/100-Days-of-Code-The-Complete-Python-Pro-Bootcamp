from turtle import Turtle
ALIGNMENT = "center"
FONT = ('courier',24,'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0,250)
        self.hideturtle()
        self.write(f"Score = {self.score}", True, align=ALIGNMENT, font=FONT)
        
        #self.update_score()
        
        
    def update_score(self):
        self.clear()
        self.goto(0,250)
        self.score += 1
        self.write(f"Score = {self.score}", True, align=ALIGNMENT, font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER...", align=ALIGNMENT, font=FONT)

        