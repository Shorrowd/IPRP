import turtle as t

t.speed(100)
dimensao = int(input("Introduz uma dimensão:"))
celula = int(input("Introduz a dimensão de cada célula:"))
conta = dimensao/celula
conta_inteira = int(conta)
avanco = conta % 1 


if (avanco != 0):
        print("Medidas Erradas")

else:
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
        

t.hideturtle()
t.exitonclick()
