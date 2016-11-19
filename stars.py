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


def B(q, w, color_2, e):
    t.up()
    t.goto(q, w)
    t.down()
    t.color(color_2)
    t.begin_fill()
    t.circle(e)
    t.end_fill()


def C(x, y, color, w, height):
    t.up()
    t.color(color)
    t.begin_fill()
    t.goto(x, y)
    t.down()
    t.goto(x + w, y)
    t.goto(x + w, y - height)
    t.goto(x, y - height)
    t.goto(x, y)
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


red = "#FF0000"
white = "#FFFFFF"
q = 0
while q < 13:
    if q % 2 == 0:
        C(0, 0 - q * 200 / 13, red, 400, 200 / 13)
    else:
        C(0, 0 - q * 200 / 13, white, 400, 200 / 13)
    q += 1
C(0, 0, "#0000FF", 130, 80)

a = [(5, -15), (15, -30), (5, -45), (15, -60), (5, -75)]
for x, y in a:
    i = 0
    while i < 6:
        five_star(x + 20 * i, y, "#FFFFFF", 6)
        i = i + 1

turtle.done()
