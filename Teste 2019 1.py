l_lista = [[1,2],[3,4]]

def mist(l_lista):
    aux_1 = list()
    for i in range(len(l_lista)):
        aux_2 = list()
        for j in range(len(l_lista[i])):
            aux_2 += [l_lista[i][j]]
        aux_1 += [aux_2]
    return aux_1

print(mist(l_lista))

#Dentro da lista temos o indice 0 [1,2] e o indice 1 [3,4] iremos verificar o range para os 2 indices e dentro de cada indice iremos fazer mais uma for j in range dentro do indice 0 
#para verificar o indice 0 e 1 dentro do indice 0 anterior como temos um for ira nos dar dois valores logo o 1 e o 2 dentro de uma lista separada pois aux1 += [aux_2] se nao tivesse
#parentisses retos seria [1,2,3,4]