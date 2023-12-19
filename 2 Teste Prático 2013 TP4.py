lista = [96 , 79 , 79 , 96 , 63 , 96 , 45 , 89 , 45 , 79]

def moda(lista):
    ocorrencia = 0
    lista_nova = []
    for i in (lista):
        conta = lista.count(i)
        if conta > ocorrencia:
            ocorrencia = conta
            lista_nova = [i]
        elif conta == ocorrencia:
            lista_nova += [i]
    menor = min(lista_nova)
    return menor,ocorrencia

print (moda(lista))