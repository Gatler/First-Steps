import turtle

t = turtle.Turtle()
t.hideturtle()
turtle.tracer(1, 0.1)


def A(color_1):
    t.up()
    t.goto(0, 0)
    t.down()
    t.fillcolor(color_1)
    t.begin_fill()
    t.goto(400, 0)
    t.goto(400, -200)
    t.goto(0, -200)
    t.goto(0, 0)
    t.end_fill()


def five_star(x, y, color_3, z):
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(54)
    t.color(color_3)
    t.begin_fill()
    t.right(198)
    n = 1
    while n < 11:
        t.right(144)
        t.forward(z)
        t.left(72)
        t.forward(z)
        n += 1
    t.end_fill()


A("#ff0000")
five_star(10, -30, "#FFFF00", 10)
five_star(50, -18, "#FFFF00", 6)
five_star(45, -38, "#FFFF00", 6)
five_star(33, -55, "#FFFF00", 6)
five_star(10, -60, "#FFFF00", 6)

turtle.done()
