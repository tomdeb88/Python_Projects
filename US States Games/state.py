from turtle import Turtle

class State(Turtle):
    def __init__(self,name,x,y):
        super().__init__()
        self.name=name
        self.x=x
        self.y=y
        self.hideturtle()
        self.penup()
        self.goto(self.x, self.y)
        self.show_up()


    def show_up(self):
        i=25

        while i>10:
            if i % 2 == 0:
                color = 'black'
            else:
                color = 'red'
            self.clear()
            self.write(self.name, align='center', font=('Courier', i, 'bold'))
            self.color(color)
            i-=1









