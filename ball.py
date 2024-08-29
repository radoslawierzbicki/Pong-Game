from turtle import Turtle


class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.goto(position)
        self.x_move = 1
        self.y_move = 1
        self.move_speed = 0.01

    def move(self):
        """Ruch piłki od górnej i dolnej ścianki się odbija, od bocznych się zatrzymuje"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        if new_y >= 285:
            #self.x_move = 0.10
            self.y_move *= -1
        elif new_y <= -285:
            self.y_move *= -1

    def bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.01
        self.bounce()

