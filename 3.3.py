import math 

print("Introduza uma altura")
altura = float(input())

print("Introduza um angulo em graus")
ang = float(input())

angulo = math.radians(ang)

comp = (altura/angulo)

print("O comprimento da escada é de ", comp)