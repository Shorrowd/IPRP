import math 

print("Introduza um dos lados do trinagulo")
a = float(input())

print("Introduza outro lado do mesmo triangulo")
b = float(input())

print("Introduza o ultimo lado do triangulo")
c = float(input())

s = ((a+b+c)/2)

area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print("A area do triangulo é de", area)