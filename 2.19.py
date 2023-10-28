import turtle as t

def circulo(cor,x,y,a,b):
    t.penup()
    t.setposition(x,y)
    t.pendown()
    t.fillcolor(cor)
    t.begin_fill()
    t.circle(a,b)
    t.end_fill()

circulo("black",0,0,10,360)
circulo("black",50,0,10,360)
circulo("black",-50,0,10,360)
circulo("black",-50,50,10,360)
circulo("black",0,50,10,360)
circulo("black",50,50,10,360)
circulo("black",-50,-50,10,360)
circulo("black",0,-50,10,360)
circulo("black",50,-50,10,360)

t.hideturtle()
for i in range(9):
    print("Indique o jogador que pretende jogar 1 ou 2? ")
    jogador = int(input())

    if jogador < 1 or jogador > 2:
         print("Jogador Inválido")

    else:
            print("Indique o número da casa de 1 a 9 em que pretende jogar: ")
            casa = int(input())
            if casa < 1 or casa > 9:
                print("Casa Inválida")
            else:
                if jogador == 1:
                    if casa == 1:
                        loc1 = circulo("red",-50,-50,10,360)
                    elif casa == 2:
                        loc2 = circulo("red",0,-50,10,360)
                    elif casa == 3:
                        loc3 = circulo("red",50,-50,10,360)
                    elif casa == 4:
                        loc4 = circulo("red",-50,0,10,360)
                    elif casa == 5:
                        loc5 = circulo("red",0,0,10,360)
                    elif casa == 6:
                        loc6 = circulo("red",50,0,10,360)
                    elif casa == 7:
                        loc7 = circulo("red",-50,50,10,360)
                    elif casa == 8:
                        loc8 = circulo("red",0,50,10,360)
                    elif casa == 9:
                        loc9 = circulo("red",50,50,10,360)
                elif jogador == 2:
                    if casa == 1:
                        loc1 = circulo("green",-50,-50,10,360)
                    elif casa == 2:
                        loc2 = circulo("green",0,-50,10,360)
                    elif casa == 3:
                        loc3 = circulo("green",50,-50,10,360)
                    elif casa == 4:
                        loc4 = circulo("green",-50,0,10,360)
                    elif casa == 5:
                        loc5 = circulo("green",0,0,10,360)
                    elif casa == 6:
                        loc6 = circulo("green",50,0,10,360)
                    elif casa == 7:
                        loc7 = circulo("green",-50,50,10,360)
                    elif casa == 8:
                        loc8 = circulo("green",0,50,10,360)
                    elif casa == 9:
                        loc9 = circulo("green",50,50,10,360)

t.exitonclick()
t.hideturtle()