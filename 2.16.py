import turtle as t 

def circulo(cor, x, y) :
    t.penup()
    t.pencolor(cor)
    t.setposition(x,y)
    t.pendown()
    t.pensize(4)
    t.circle(50)
    
circulo('blue', -20, 50)
circulo('black', 90, 50)
circulo('red', 200, 50)
circulo('yellow', 35, 10)
circulo('light green', 145, 10)

t.hideturtle()
t.exitonclick()