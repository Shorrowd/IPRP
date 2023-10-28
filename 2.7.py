import turtle

turtle.speed(100)
turtle.circle (100)
turtle.penup()
turtle.setposition(-50,120)
turtle.pendown()
turtle.fillcolor('black')
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.setposition(50,120)
turtle.pendown()
turtle.fillcolor('black')
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.setposition(-40,40)
turtle.right(25)
turtle.pendown()
turtle.circle(100,55)

turtle.exitonclick()
