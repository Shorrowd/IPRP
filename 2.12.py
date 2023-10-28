import turtle as t 

t.fillcolor("green")
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()
t.penup()
t.left(90)
t.forward(100)
t.setheading(180)
t.pendown()

t.fillcolor("red")
t.begin_fill()
for i in range(3):
    t.right(120)
    t.forward(100)
t.end_fill()

t.fillcolor("black")

t.setheading(0)
t.forward(100)
t.left(120)
t.forward(60)
t.begin_fill()
t.setheading(90)
t.forward(30)
t.left(90)
t.forward(10)
t.left(90)
t.forward(12)
t.setheading(-60)
t.forward(20)
t.end_fill()

t.hideturtle()
t.exitonclick()

