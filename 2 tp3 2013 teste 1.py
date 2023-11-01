import turtle as t

t.speed(100)

dimensao = int(input("Introduz uma dimensão: "))
dimensao2 = dimensao/2

def retangulo(cor):
    t.fillcolor(cor)
    t.begin_fill()
    for i in range(2):
        t.forward(dimensao/2)
        t.left(90)
        t.forward(dimensao)
        t.left(90)
    t.end_fill()
    
def flor(ang,numero):
    for i in range(numero):
        t.penup()
        t.setposition(50,-50)
        t.pendown()
        t.setheading(ang)
        retangulo("red")
        ang += 30

flor(0,20)

t.hideturtle()
t.exitonclick()