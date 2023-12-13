lista_ST = []
lista_DC = []
lista_GK = []
lista_DR = []
lista_MC = []

def convert_to_dict(lista):
    for i in range (len(lista)):
        jog_lista = lista[i]
        nome_jog = jog_lista[0]
        posicao_jog = jog_lista[1]
        if posicao_jog == "ST":
            lista_ST.append(nome_jog)
        elif posicao_jog == "DC":
            lista_DC.append(nome_jog)
        elif posicao_jog == "GK":
            lista_GK.append(nome_jog)
        elif posicao_jog == "DR":
            lista_DR.append(nome_jog)
        elif posicao_jog == "MC":
            lista_MC.append(nome_jog)    

    lista_jogadores = {'ST': lista_ST, 'DC': lista_DC, 'GK': lista_GK, 'DR': lista_DR, 'MC': lista_MC}

    return lista_jogadores

print(convert_to_dict([("Cristiano Ronaldo","ST"), ("Pepe","DC"), ("Diogo Costa", "GK"), ("Ruben Dias", "DC"), ("Diogo Dallot", "DR"), ("Goncalo Ramos", "ST"), ("Joao Felix", "ST"), ("Joao Cancelo", "DR"), ("Joao Palhinha", "MC"), ("William Carvalho", "MC")]))