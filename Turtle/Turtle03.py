import turtle
from threading import Thread

window = turtle.Screen()
r = 50

eu = turtle.Turtle()
afr = turtle.Turtle()
amer = turtle.Turtle()
asia = turtle.Turtle()
aus = turtle.Turtle()

for i in [eu, afr, amer, asia, aus]:
    i.up()
    i.speed(10)

eu.goto(-2 * r, 2 * r)
afr.goto(0, 2 * r)
amer.goto(2 * r, 2 * r)
asia.goto(-r, r)
aus.goto(r, r)

for i in [eu, afr, amer, asia, aus]:
    i.down()
    i.pensize(4)

eu.color("blue")
afr.color("black")
amer.color("red")
asia.color("yellow")
aus.color("green")

# for i in [eu, afr, amer, asia, aus]:
#    i.circle(r)

# Объявляем потоки
thread1 = Thread(target=eu.circle, args=(r,))
thread2 = Thread(target=afr.circle, args=(r,))
thread3 = Thread(target=amer.circle, args=(r,))
thread4 = Thread(target=asia.circle, args=(r,))
thread5 = Thread(target=aus.circle, args=(r,))

# Запуск потоков
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

window.mainloop()