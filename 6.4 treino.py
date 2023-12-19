elem = int(input("Escreva uma elemento numerico: "))
lista = list(input("Escreva uma lista de numeros: "))

def conta_menores(elem,lista):
    numero_menores = 0
    for i in range(len(lista)):
        if elem > (lista[i]):
            numero_menores +=1
    return numero_menores

print (conta_menores(5,[2,8,6,5,3,2]))