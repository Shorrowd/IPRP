import turtle as t

tamanho_lado = int(input("Introduz o tamanho do lado: "))

x = tamanho_lado/2
diferenca1 = (tamanho_lado + (tamanho_lado*0.5))/2
diferenca2 = (tamanho_lado + (tamanho_lado*1))/2
diferenca3 = (tamanho_lado + (tamanho_lado*1.5))/2
diferenca4 = (tamanho_lado + (tamanho_lado*2))/2

def triangulo(tamanho_lado):
    t.penup()
    t.setposition(-tamanho_lado/2,-250)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    for i in range(3):
        t.forward(tamanho_lado)
        t.left(120)
    t.end_fill()
    
def quadrado(diferenca1):
    t.penup()
    t.setposition(-diferenca1 , -250)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    
    for i in range(4):
        t.forward(diferenca1 * 2)
        t.left(90)
        
    t.end_fill()
    
def pentagono(diferenca2):
    t.penup()
    t.setposition(-diferenca2 , -250)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    
    for i in range(5):
        t.forward(diferenca2 * 2)
        t.left(72)
        
    t.end_fill()
    
def hexagono(diferenca3):
    t.penup()
    t.setposition(-diferenca3 , -250)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    
    for i in range(6):
        t.forward(diferenca3 * 2)
        t.left(60)
        
    t.end_fill()
    
def heptagono(diferenca4):
    t.penup()
    t.setposition(-diferenca4 , -250)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    
    for i in range(7):
        t.forward(diferenca4 * 2)
        t.left(51.43)
        
    t.end_fill()
    
heptagono(diferenca4)
hexagono(diferenca3)    
pentagono(diferenca2)
quadrado(diferenca1)
triangulo(tamanho_lado)

t.exitonclick()