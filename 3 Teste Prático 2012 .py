def diferenca_pontos():
    dicionario_equipas = {}
    ficheiro = open("estatisticas.txt","r")
    for i in ficheiro:
        dados = i.split(",")
        nome_equipa = dados[0]
        print(dados)
        pontos_marcados = int(dados[1])
        pontos_sofridos = int(dados[2])

        diferenca = (pontos_marcados - pontos_sofridos)

        dicionario_equipas[nome_equipa] = diferenca

    ficheiro.close()

    ficheiro_adicionar = open("estatisticas.txt", "a")
    ficheiro_adicionar.write("\n")

    if (dicionario_equipas["Olivais"] > dicionario_equipas["Academica"]) and (dicionario_equipas["Olivais"] > dicionario_equipas["Porto"]):
        ficheiro_adicionar.write("Olivais")

    if (dicionario_equipas["Academica"] > dicionario_equipas["Olivais"]) and (dicionario_equipas["Academica"] > dicionario_equipas["Porto"]):
        ficheiro_adicionar.write("Academica")

    if (dicionario_equipas["Porto"] > dicionario_equipas["Academica"]) and (dicionario_equipas["Porto"] > dicionario_equipas["Olivais"]):
        ficheiro_adicionar.write("Porto")

print(diferenca_pontos())