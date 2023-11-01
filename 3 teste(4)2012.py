n = int(input("Introduza uma numero: "))
ciclo = 1

while n != 1:
    if n%2 == 0:
        n = (n/2)
        ciclo += 1
    else:
        n = (n*3 + 1)
        ciclo += 1

print("O tamanho do ciclo é ", ciclo)
