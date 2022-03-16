from random import randint
from turtle import Turtle

c = Turtle()
m = Turtle()
s = Turtle()
a = Turtle()
rt = Turtle()


c.color('red')
c.shape('turtle')
c.setpos(0,0)
c.penup()
c.goto(-160, 110)
c.pendown()
c.shapesize(2,2,2)

m.color('blue')
m.shape('turtle')
m.penup()
m.goto(-160, 70)
m.pendown()

s.color('yellow')
s.shape('turtle')
s.penup()
s.goto(-160, 30)
s.pendown()

a.color('black')
a.shape('turtle')
a.penup()
a.goto(-160, -10)
a.pendown()

rt.penup()
rt.goto(100, 130)
rt.down()
rt.fillcolor('black')
rt.forward(20)
rt.right(90)
rt.forward(150)
rt.right(90)
rt.forward(20)
rt.right(90)
rt.forward(150)


for mvt in range(100):
  c.forward(randint(1,2))
  m.forward(randint(1,5))
  s.forward(randint(1,5))
  a.forward(randint(1,5))