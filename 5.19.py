import turtle as t
import random 

t.speed(20)
dimensao = int(input("Introduz uma dimensão:"))
celula = int(input("Introduz a dimensão de cada célula:"))
conta = dimensao/celula
conta_inteira = int(conta)
avanco = conta % 1

def quadrado(dimensao,celula,conta_inteira):
    t.penup()
    t.setposition(-dimensao/2,dimensao/2)
    t.pendown()
    
    for i in range(4):
        t.forward(dimensao)
        t.right(90)

    for i in range(conta_inteira):
        t.forward(celula)
        t.right(90)
        t.forward(dimensao)
        t.back(dimensao)
        t.left(90)

    t.right(90)

    for i in range(conta_inteira):
        t.forward(celula)
        t.right(90)
        t.forward(dimensao)
        t.back(dimensao)
        t.left(90)

if (avanco != 0):
    print("Medidas Erradas")
else:
    quadrado(dimensao,celula,conta_inteira)

t.penup()
t.goto(0,0)
t.pendown()
t.width(1)
t.shape("circle")
t.color("red")
t.stamp()
t.shape("classic")


def passeio():
    num = random.randint(10,30)
    for i in range(num):
        head = random.randint(1,4)
        if head == 1:
            t.setheading(0)
        elif head == 2:
            t.setheading(90)
        elif head == 3:
            t.setheading(180)
        elif head == 4:
            t.setheading(270)
        t.pencolor("red")
        t.forward(dimensao/8)

passeio()

t.end_fill()
t.exitonclick()