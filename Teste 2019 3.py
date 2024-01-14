lista_carga=[('arroz',40,100),('alface',60,200),('batata',80,200),('cenoura',120,250)]

def melhor_carga(lista_carga,peso_max):
    possibilidades = []
    for elemento1 in lista_carga:
        for elemento2 in lista_carga:
            if elemento1[1] + elemento2[1] <= peso_max:
                possibilidades.append([elemento1[0], elemento2[0], elemento1[2]+elemento2[2]])
    margem_de_lucro = 0

    for i in range(len(possibilidades)):
        if possibilidades[i][2] > margem_de_lucro:
            margem_de_lucro = possibilidades[i][2]
            
    print("(",possibilidades[i][0],",",possibilidades[i][1],")")

melhor_carga(lista_carga,200)