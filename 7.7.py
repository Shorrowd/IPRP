import turtle 
import random



with open ("random.txt", "w") as novo:
    for i in range(10):
        numero1 = str(random.randint(1,6))
        numero2 = str(random.randint(1,6))
    par = "\n"+ numero1 + numero2
    novo.write(par)

def desenhar(par):
    turtle.goto(numero1,numero2)   
    