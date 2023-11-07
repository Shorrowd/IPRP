import turtle as t
import math

def quadrado():
    for i in range(4):
        t.forward(200)
        t.right(90)

quadrado()

n = (math.sqrt((200**2)+(200**2)))/2

def triangulo1(x,y,z):
    t.penup()
    t.setposition(100,-100)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.setheading(x)
    t.forward(n)
    t.setheading(y)
    t.forward(200)
    t.setheading(z)
    t.forward(n)
    t.end_fill()

triangulo1(135,0,225)
triangulo1(225,0,135)

t.hideturtle()
t.exitonclick()