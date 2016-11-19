import turtle

t = turtle.Turtle()
t.hideturtle()
t.pensize(40)
t.right(90)
颜色 = "#FF0033"
t.pencolor(颜色)
t.circle(80, -180)
t.penup()
t.setposition(200, 0)
t.down()
颜色 = "#FF9900"
t.pencolor(颜色)
t.circle(120, 180)
t.penup()
t.setposition(-80, 0)
t.down()
颜色 = '#FFFF00'
t.pencolor(颜色)
t.circle(160, -180)
t.penup()
t.setposition(280, 0)
t.down()
颜色 = '#00FF00'
t.pencolor(颜色)
t.circle(200, 180)
t.penup()
t.setposition(-160, 0)
t.down()
颜色 = '#2BB3D5'
t.pencolor(颜色)
t.circle(240, -180)
t.penup()
t.setposition(360, 0)
t.down()
颜色 = '#0000FF'
t.pencolor(颜色)
t.circle(280, 180)
t.penup()
t.setposition(-240, 0)
t.down()
颜色 = '#9900FF'
t.pencolor(颜色)
t.circle(320, -180)
t.penup()
t.setposition(0, -280)
t.down()

turtle.done()
