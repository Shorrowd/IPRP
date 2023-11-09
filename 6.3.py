l1 = [1,2,3]
l2 = ['a','b','c']
lista = []

def alterna(lista,l1,l2):
    for i in range(len(l1)):
        lista.append(l1[i])
        lista.append(l2[i])

    return lista

print(alterna(lista,l1,l2))