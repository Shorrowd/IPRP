import turtle as t 

a = 0
b = 0

for i in range(5):
    t.penup()
    t.setposition(-100+a,100-a)
    t.pendown()
    t.setheading(-90)
    a += 20
    for i in range(4):
        t.forward(200-b)
        t.left(90)
    b += 40

t.exitonclick()


    

