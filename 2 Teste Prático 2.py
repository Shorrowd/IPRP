#lista = {'ST': ['Cristiano Ronaldo', 'Gocalo Ramos', 'Joao Felix'],'DC': ['Pepe', 'Ruben Dias'], 'GK': ['Diogo Costa'], 'DR': ['Diogo Dallot', 'Joao Cancelo'], 'MC': ['Joao Palhinha', 'William Carvalho']}
lista_ST = []
lista_DC = []
lista_GK = []
lista_DR = []
lista_MC = []


def convert_to_dict(lista):
    for i in range(len(lista)):
        posicao_jog = lista[i]
        nome_jog = posicao_jog[0]
        jog_posicao = posicao_jog[1]
        if (jog_posicao == 'ST'):
            lista_ST.append(nome_jog)
        elif(jog_posicao == 'DC'):
            lista_DC.append(nome_jog)
        elif(jog_posicao == 'GK'):
            lista_GK.append(nome_jog)
        elif(jog_posicao == 'DR'):
            lista_DR.append(nome_jog)
        elif(jog_posicao == 'MC'):
            lista_MC.append(nome_jog)

    lista_jogadores = {'ST': lista_ST, 'DC': lista_DC, 'GK': lista_GK, 'DR': lista_DR, 'MC': lista_MC}

    return lista_jogadores


print(convert_to_dict([("Cristiano Ronaldo","ST"), ("Pepe","DC"), ("Diogo Costa", "GK"), ("Ruben Dias", "DC"), ("Diogo Dallot", "DR"), ("Goncalo Ramos", "ST"), ("Joao Felix", "ST"), ("Joao Cancelo", "DR"), ("Joao Palhinha", "MC"), ("William Carvalho", "MC")]))