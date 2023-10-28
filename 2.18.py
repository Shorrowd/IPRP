import turtle as t 

t.speed(20)

t.penup()
t.setposition(150,50)
t.pendown()
t.fillcolor('white')
t.setheading(90)
t.begin_fill()
t.circle(200,180)
t.end_fill()
t.fillcolor('black')
t.penup()
t.setposition(-250,50)
t.setheading(-90)
t.pendown()
t.begin_fill()
t.circle(200,180)
t.end_fill()


def semi(cor,x,y,a,b,cort):
    t.penup()
    t.setposition(a,b)
    t.pendown()
    t.pencolor(cort)
    t.setheading(y)
    t.fillcolor(cor)
    t.begin_fill()
    t.left(90)
    t.circle(x)
    t.end_fill()
    
semi('black',100,0,-50,50,'black')
semi('white',100,180,-50,50,'white')
semi('white',20,0,-135,50,'black')
semi('black',20,0,75,50,'black')

t.penup()
t.setposition(150,50)
t.pendown()
t.circle(200)

t.hideturtle()
t.exitonclick()