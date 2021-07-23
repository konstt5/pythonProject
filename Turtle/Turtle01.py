import random
import turtle

def drawSquare(t, a):
    for i in range(4):
        t.forward(a)
        t.left(90)

def drawPolygon(t, n):
    angle = 180 * (n - 2) / n
    for i in range(n):
        t.forward(100)
        t.left(180 - angle)

def drawStar(t, n):
    if n % 2 != 0:
        angle = n //2 * 360 / n
        for i in range(n):
            t.forward(50)
            t.left(angle)

if __name__ == "__main__":
    t = turtle.Turtle()
    t.speed(50)

    window = turtle.Screen()
    window.bgcolor("black")
    window.setup(900, 600)

    colors = ["red", "green", "blue", "brown"]

    # # circle
    # for i in range(60):
    #     t.color(colors[i % 4])
    #     #drawSquare(t, i * 4 + 30)
    #     t.circle(i * 2 + 30)
    #     t.right(10)

    # # polygon
    # for i in range(3, 11):
    #     t.color(colors[i % 4])
    #     drawPolygon(t, i)

    # t.up()
    # t.setposition(100, 0)
    # t.down()

    # star
    for i in range(5, 16, 2):
        t.color("red")
        t.begin_fill()
        drawStar(t, i)
        t.end_fill()

        x = random.randint(-400, 400)
        y = random.randint(-250, 250)

        t.up()
        #t.goto(-(i - 3) * 50, 0)
        t.setposition(x, y)
        t.down()

    turtle.mainloop()
