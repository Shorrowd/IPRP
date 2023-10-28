import turtle as t

t.speed(100)
t.bgcolor('blue')
t.shape("turtle")
t.color('red')
t.shapesize(0.5)
t.penup()

for i in range(48):
    t.forward(5+i)
    t.right(15)
    t.stamp()






turtle.exitonclick()