import turtle as t
import random 

t.speed(50)
t.bgcolor("black")

dimensao = int(input("Introduz uma dimensão:"))
conta = dimensao / 8
conta_inteira = int(conta)
avanco = conta % 1

def quadrado(dimensao,conta):
    t.color("white")
    t.penup()
    t.setposition(-dimensao/2,dimensao/2)
    t.pendown()

    for i in range(4):
        t.forward(dimensao)
        t.right(90)

    for i in range(8):
        t.forward(conta)
        t.right(90)
        t.forward(dimensao)
        t.back(dimensao)
        t.left(90)

    t.right(90)

    for i in range(8):
        t.forward(conta)
        t.right(90)
        t.forward(dimensao)
        t.back(dimensao)
        t.left(90)

if (avanco != 0):
    print("Medidas Erradas")
else:
    quadrado(dimensao,conta)

t.penup()
t.goto(0,0)
t.pendown()
t.shape("circle")
t.color("red")
t.stamp()
t.shape("classic")

def passeio():
    num = random.randint(50,100)
    for i in range(num):
        head = random.randint(1,4)
        if (head == 1):
            t.setheading(0)
        elif (head == 2):
            t.setheading(90)
        elif (head == 3):
            t.setheading(180)
        elif (head == 4):
            t.setheading(270)

        t.forward(conta)

passeio()

if t.xcor() >= dimensao/2:
    head = random.randint(1,3)
    if (head == 1):
            t.setheading(90)
            t.fd(conta)
    elif (head == 2):
            t.setheading(180)
            t.fd(conta)
    elif (head == 3):
            t.setheading(270)
            t.fd(conta)
    print("Passou da Grelha. ")
elif t.xcor() <= -dimensao/2:
    head = random.randint(1,3)
    if (head == 1):
            t.setheading(90)
            t.fd(conta)
    elif (head == 2):
            t.setheading(270)
            t.fd(conta)
    elif (head == 3):
            t.setheading(0)
            t.fd(conta)
    print("Passou da Grelha. ")
elif t.ycor() <= -dimensao/2:
    head = random.randint(1,3)
    if (head == 1):
            t.setheading(90)
            t.fd(conta)
    elif (head == 2):
            t.setheading(180)
            t.fd(conta)
    elif (head == 3):
            t.setheading(0)
            t.fd(conta)
    print("Passou da Grelha. ")
elif t.ycor() >= dimensao/2:
    head = random.randint(1,3)
    if (head == 1):
            t.setheading(270)
            t.fd(conta)
    elif (head == 2):
            t.setheading(180)
            t.fd(conta)
    elif (head == 3):
            t.setheading(0)
            t.fd(conta)
    print("Passou da Grelha. ")

t.exitonclick()