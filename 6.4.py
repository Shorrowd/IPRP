elem = int(input("Introduz um numero: "))
lista = list(input("Introduz uma lista numerica: "))
numero_menores = 0

def conta_menores(elem,lista, numero_menores):
    for i in range(len(lista)):
        if int(lista[i]) < elem:
            numero_menores += 1

    return numero_menores

print(conta_menores(elem,lista, numero_menores))