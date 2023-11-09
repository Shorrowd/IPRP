lista = [[0,1,0],[1,1,1],[0,1,0]]

def trocar(lista):
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j] == 0:
                lista [i][j] = 1
            else:
                lista[i][j] = 0

    return lista

print(trocar(lista))