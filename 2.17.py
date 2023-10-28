import turtle as t 

t.penup()
t.setposition(-100,-100)
t.pendown()
t.fillcolor('yellow')

t.begin_fill()
for i in range(4):
    t.forward(300)
    t.left(90)
t.end_fill()
   
def circulo(cor,x,y):
    t.penup()
    t.setposition(x,y)
    t.pendown()
    t.fillcolor(cor)
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    
circulo('black',50,25)

def semicirculo(cor, a, b, c):
    t.penup()
    t.setposition(50,50)
    t.setheading(c)
    t.pendown()
    t.fillcolor(cor)
    t.begin_fill()
    t.forward(a)
    t.left(90)
    t.circle(a,b)
    t.left(90)
    t.forward(a)
    t.left(180-b)
    t.end_fill()
    
semicirculo('black', 120, 60, 0)
semicirculo('black', 120, 60, 120)
semicirculo('black', 120, 60, -120)

def circulo2(cor,x,y):
    t.penup()
    t.setposition(x,y)
    t.pensize(4)
    t.pendown()
    t.pencolor(cor)
    t.circle(30)
    
circulo2('yellow',25,70)

t.hideturtle()
t.exitonclick()