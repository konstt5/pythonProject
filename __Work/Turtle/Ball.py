import turtle, random

class Ball:
    def __init__(self):
        self.Balls = []
        self.t = turtle.Turtle()
        self.window = turtle.Screen()
        self.running = False
        self.trace = False

        self.setParameters()
        self.drawRect()

        turtle.mainloop()

    def setParameters(self):
        self.t.speed(0)
        self.t.color("red")
        self.t.hideturtle()
        self.t.up()
        self.window.bgcolor("black")
        self.window.tracer(1.5)
        self.window.onclick(self.OnCkick)

    def drawRect(self):
        self.t.goto(-self.window.canvwidth - 5, -self.window.canvheight - 5)
        self.t.down()
        self.t.goto(self.window.canvwidth + 5, -self.window.canvheight - 5)
        self.t.goto(self.window.canvwidth + 5, self.window.canvheight + 5)
        self.t.goto(-self.window.canvwidth - 5, self.window.canvheight + 5)
        self.t.goto(-self.window.canvwidth - 5, -self.window.canvheight - 5)
        self.t.up()

    def newBall(self, x, y):
        Ball = turtle.Turtle(shape="circle")
        Ball.speed(0)
        Ball.hideturtle()
        Ball.up()
        r = random.random()
        g = random.random()
        b = random.random()
        Ball.color(r, g, b)
        Ball.vx = random.randint(1, 10)
        Ball.vy = random.randint(1, 10)
        Ball.grav = 0.5
        Ball.goto(x - 5, y - 5)
        Ball.showturtle()
        self.Balls.append(Ball)
        self.window.tracer(len(self.Balls) // 5 + 1)

    def OnCkick(self, x, y):
        # self.t.reset()
        # self.setParameters()
        # self.drawRect()
        self.newBall(x, y)

        if not self.running:
            self.start()

    def start(self):
       self.window.update()
       self.running = True

       while self.running:
            for Ball in self.Balls:
                Ball.vy = Ball.vy - Ball.grav
                Ball.goto(Ball.xcor() + Ball.vx, Ball.ycor() + Ball.vy)

                if abs(Ball.xcor()) >= (self.window.canvwidth):
                    Ball.vx = -Ball.vx

                if abs(Ball.ycor()) >= (self.window.canvheight):
                    Ball.vy = -Ball.vy + Ball.grav

                if self.trace:
                    Ball.down()
                    Ball.circle(10)
                    Ball.up()
                    Ball.showturtle()

if __name__ == "__main__":
    b = Ball()