import math 
print("Introduza um numero de objetos")
n = float(input())

print("Introduza um outro numero de objetos")
m = float(input())

p1 = (n/(n+m))

p2 = (m/(n+m))

d = (-(p1*math.log2(p1))+(p2*math.log2(p2)))

print("A desordem do conjunto é de", d)