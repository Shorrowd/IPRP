def publicacoes_conjuntas(ficheiro,nome):
    lista = []
    ficheiro_nomes = open(ficheiro, "r")
    for nome in ficheiro_nomes:
        print(nome)


print(publicacoes_conjuntas("ficheiro.txt","Pinto"))