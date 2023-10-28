import turtle as t
t.bgcolor("lightgreen")

angulo = 0
t.color("red")

def ponteiro(angulo):
    for i in range(12):
        t.setheading(0 + angulo)
        t.penup()
        t.forward(100)
        t.pendown()
        t.forward(30)
        t.penup()
        t.setposition(0,0)
    
        angulo += 30

ponteiro(angulo)    


t.hideturtle()
t.exitonclick()

    