lista = [1,2,3]
lista_nova = []
def array(lista,lista_nova):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
        lista_nova.append(soma)

    return lista_nova

print (array(lista,lista_nova))