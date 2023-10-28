import turtle

turtle.speed(100)
turtle.setposition(0,0)
a = 10


for i in range (50):
    turtle.forward(100 + a)
    turtle.right(144)
    a += 10
    

turtle.exitonclick()
