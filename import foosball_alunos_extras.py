import foosball_alunos_extras

def le_replay(nome_ficheiro):
    lista_tuplos_coordenadas_jogador_azul = []
    lista_tuplos_coordenadas_jogador_vermelho = []
    lista_tuplos_coordenadas_bola = []
    
    ficheiro_replay = open(nome_ficheiro, "r")
    linha_posicoes_bola = ficheiro_replay.readline()
    linha_posicoes_jogador_vermelho = ficheiro_replay.readline()
    linha_posicoes_jogador_azul = ficheiro_replay.readline()
    
    posicoes_bola = linha_posicoes_bola.split(";")    
    posicoes_jogador_vermelho = linha_posicoes_jogador_vermelho.split(";")   
    posicoes_jogador_azul = linha_posicoes_jogador_azul.split(";")   
    
    for i in range(len(posicoes_bola)-1):
        coordenada_posicoes_bola = posicoes_bola[i].split(",")
        x_posicoes_bola = float(coordenada_posicoes_bola[0])
        y_posicoes_bola = float(coordenada_posicoes_bola[1])
        tuplo_coordenadas_bola = tuple([x_posicoes_bola, y_posicoes_bola])
        lista_tuplos_coordenadas_bola += [tuplo_coordenadas_bola]
        
    for i in range(len(posicoes_jogador_vermelho)-1):
        coordenada_posicoes_jogador_vermelho = posicoes_jogador_vermelho[i].split(",")
        x_posicoes_jogador_vermelho = float(coordenada_posicoes_jogador_vermelho[0])
        y_posicoes_jogador_vermelho = float(coordenada_posicoes_jogador_vermelho[1])
        tuplo_coordenadas_jogador_vermelho = tuple([x_posicoes_jogador_vermelho, y_posicoes_jogador_vermelho])
        lista_tuplos_coordenadas_jogador_vermelho += [tuplo_coordenadas_jogador_vermelho]
    
    for i in range(len(posicoes_jogador_azul)-1):
        coordenada_posicoes_jogador_azul = posicoes_jogador_azul[i].split(",")
        x_posicoes_jogador_azul = float(coordenada_posicoes_jogador_azul[0])
        y_posicoes_jogador_azul = float(coordenada_posicoes_jogador_azul[1])
        tuplo_coordenadas_jogador_azul = tuple([x_posicoes_jogador_azul, y_posicoes_jogador_azul])
        lista_tuplos_coordenadas_jogador_azul += [tuplo_coordenadas_jogador_azul]
    
    replay = {"bola": lista_tuplos_coordenadas_bola, "jogador_vermelho": lista_tuplos_coordenadas_jogador_vermelho, "jogador_azul": lista_tuplos_coordenadas_jogador_azul}
    '''
    Função que recebe o nome de um ficheiro contendo um replay, e que deverá 
    retornar um dicionário com as seguintes chaves:
    bola - lista contendo tuplos com as coordenadas xx e yy da bola
    jogador_vermelho - lista contendo tuplos com as coordenadas xx e yy da do jogador\_vermelho
    jogador_azul - lista contendo tuplos com as coordenadas xx e yy da do jogador\_azul
    '''
    return replay
        


def main():
    estado_jogo = foosball_alunos_extras.init_state()
    foosball_alunos_extras.setup(estado_jogo, False)
    replay = le_replay(input("Introduz o nome do ficheiro do replay: "))
    for i in range(len(replay['bola'])):
        estado_jogo['janela'].update()
        estado_jogo['jogador_vermelho'].setpos(replay['jogador_vermelho'][i])
        estado_jogo['jogador_azul'].setpos(replay['jogador_azul'][i])
        estado_jogo['bola']['objecto'].setpos(replay['bola'][i])
    estado_jogo['janela'].exitonclick()

if __name__ == '__main__':
    main()