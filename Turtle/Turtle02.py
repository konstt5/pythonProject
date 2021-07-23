import random
import turtle

def drawStar(t, n):
    if n % 2 != 0:
        initangle = random.randint(0, 90)
        t.left(initangle)

        angle = n //2 * 360 / n
        len = random.randint(10, 50)
        for i in range(n):
            t.forward(len)
            t.left(angle)

def drawStarFill(t):
    ver = random.choice([5, 7, 9, 11, 13, 15])
    t.color("yellow")
    t.begin_fill()
    drawStar(t, ver)
    t.end_fill()

def onClick(x, y):
    t.up()
    t.setposition(x, y)
    t.down()

    drawStarFill(t)

def onKey():
    window.reset()
    t.speed(200)
    t.hideturtle()

if __name__ == "__main__":
    t = turtle.Turtle()
    t.speed(200)
    t.hideturtle()

    window = turtle.Screen()
    window.bgcolor("black")
    window.setup(900, 600)
    window.onclick(onClick)
    window.onkey(onKey, "space")
    window.listen()

    turtle.mainloop()
