from turtle import Turtle
import os

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0 
        self.highscore = self.get_highscore()
        self.color("white")
        self.penup()
        self.goto(0, 350)
        self.hideturtle()
        self.update_scoreboard()

    def get_highscore(self):
        path = os.path.join(os.path.dirname(__file__), "highscore.txt")
        try:
            with open(path, "r") as file:
                return int(file.read())
        except FileNotFoundError:
            with open(path, "w") as file:
                file.write("0")
            return 0
        
    def save_highscore(self):
        path = os.path.join(os.path.dirname(__file__), "highscore.txt")
        with open(path, "w") as file:
            file.write(str(self.highscore))
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    High score: {self.highscore}", align = "center", font = ("Arial", 24, "normal")) 

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    
    def game_over(self):
        self.clear()
        self.screen.bgcolor("darkred")
        self.goto(0, 0)
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore()
        self.write(f"----------- Game Over ----------- \n\nFinal Score: {self.score} \n\nHigh Score: {self.highscore}", align = "center", font =("Arial", 24, "normal"))
