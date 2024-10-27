from turtle import Turtle
import time

class Info(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def move(self):
        time.sleep(.5)
        self.clear()

    def no_state(self):
        self.write('Not such a State', align='center', font=('Roboto', 18, 'bold'))
        self.move()
    def already_exist(self):
        self.write("Already got it!", align='center', font=('Roboto', 18, 'bold'))
        self.move()

    def win(self):
        self.write("You got it! All the States!", align='center', font=('Roboto', 18, 'bold'))