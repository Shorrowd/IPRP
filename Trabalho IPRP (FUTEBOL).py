#código com extras

import turtle as t
import functools
import random

LARGURA_JANELA = 1024
ALTURA_JANELA = 600
DEFAULT_TURTLE_SIZE = 40
DEFAULT_TURTLE_SCALE = 3
RAIO_JOGADOR = DEFAULT_TURTLE_SIZE / DEFAULT_TURTLE_SCALE
RAIO_BOLA = DEFAULT_TURTLE_SIZE / 2
PIXEIS_MOVIMENTO = 90
LADO_MAIOR_AREA = ALTURA_JANELA / 3
LADO_MENOR_AREA = 50
RAIO_MEIO_CAMPO = LADO_MAIOR_AREA / 4
START_POS_BALIZAS = ALTURA_JANELA / 6 #alterei para 100 em vez de 150
BOLA_START_POS = (5,5)


# Funções responsáveis pelo movimento dos jogadores no ambiente. 
# O número de unidades que o jogador se pode movimentar é definida pela constante 
# PIXEIS_MOVIMENTO. As funções recebem um dicionário que contém o estado 
# do jogo e o jogador que se está a movimentar. 

#-----------------------------------------------------------------------------------------------------------------------
def jogador_cima(estado_jogo, jogador):
    estado_jogo[jogador].setheading(90)
    estado_jogo[jogador].forward(PIXEIS_MOVIMENTO)

def jogador_baixo(estado_jogo, jogador):
    estado_jogo[jogador].setheading(270)
    estado_jogo[jogador].forward(PIXEIS_MOVIMENTO)

def jogador_direita(estado_jogo, jogador):
    estado_jogo[jogador].setheading(0)
    estado_jogo[jogador].forward(PIXEIS_MOVIMENTO)

def jogador_esquerda(estado_jogo, jogador):
    estado_jogo[jogador].setheading(180)
    estado_jogo[jogador].forward(PIXEIS_MOVIMENTO)

#funções para dizer o que a turtle vai fazer quando for chamada a respetiva função

#-------------------------------------------------------------------------------------------------------------------------
def verdes(y):
    t.begin_fill()
    t.penup()
    t.goto(-512,y)
    t.setheading(90)
    t.fd(100)
    t.right(90)
    t.fd(1024)
    t.right(90)
    t.fd(100)
    t.right(90)
    t.fd(1024)
    t.pendown()
    t.fillcolor("darkgreen")
    t.end_fill()


def cantos():
    t.width(10)
    t.color("white")
    
    t.penup()
    t.goto(-512,-300) 
    t.pendown()
    t.setheading(0)
    t.fd(30)
    t.setheading(90)
    t.circle(30,90)
    
    t.penup()
    t.goto(-512,300) 
    t.pendown()
    t.setheading(270)
    t.fd(30)
    t.setheading(0)
    t.circle(30,90)
    
    t.penup()
    t.goto(512,300) 
    t.pendown()
    t.setheading(180)
    t.fd(30)
    t.setheading(270)
    t.circle(30,90)
    
    t.penup()
    t.goto(512,-300) 
    t.pendown()
    t.setheading(90)
    t.fd(30)
    t.setheading(180)
    t.circle(30,90)

def linhas_laterais():
    t.penup()
    t.goto(-512,-300) 
    t.width(10)
    t.color("white")
    t.pendown()
    t.goto(-512,300)
    t.goto(512,300)
    t.goto(512,-300)
    t.goto(-512,-300)

def baliza_L():
    t.penup()
    t.goto(-512,START_POS_BALIZAS)
    t.setheading(0)
    t.pendown()
    t.fd(LADO_MENOR_AREA)
    t.right(90)
    t.fd(LADO_MAIOR_AREA)
    t.right(90)
    t.fd(LADO_MENOR_AREA)

def baliza_R():
    t.penup()
    t.goto(512,START_POS_BALIZAS)
    t.setheading(180)
    t.pendown()
    t.fd(LADO_MENOR_AREA)
    t.left(90)
    t.fd(LADO_MAIOR_AREA)
    t.left(90)
    t.fd(LADO_MENOR_AREA)

def linha_central():
    t.penup()
    t.goto(0,300)
    t.pendown()
    t.width(10)
    t.color("white")
    t.setheading(270)
    t.fd(600)

def circulo_central():
    t.penup()
    t.goto(0,115)
    t.setheading(180)
    t.pendown()
    t.width(10)
    t.color("white")
    t.circle(115)
    t.penup()
    t.goto(0,17.5)
    t.pendown()
    t.width(10)
    t.color("white")
    t.fillcolor("white")
    t.begin_fill()
    t.circle(15)
    t.end_fill()

def fora_campo():
    t.penup()
    t.goto(-525,-315) 
    t.width(20)
    t.color("darkgreen")
    t.pendown()
    t.goto(-525,315)
    t.goto(525,315)
    t.goto(525,-315)
    t.goto(-525,-315)

def bancadas():
    t.penup()
    t.goto(-170,-320)
    t.pendown()
    t.setheading(90)
    for i in range(2):
        t.right(90)
        t.fd(150)
        t.right(90)
        t.fd(35)
    t.penup()
    t.goto(170,-320)
    t.pendown()
    t.setheading(90)
    for i in range(2):
        t.left(90)
        t.fd(150)
        t.left(90)
        t.fd(35)
        
def suplentes_red(x):
    t.penup()
    t.color("red")
    t.goto(x,-330)
    t.pendown()
    t.begin_fill()
    t.circle(1)
    t.end_fill()

def suplentes_blue(x):
    t.penup()
    t.color("blue")
    t.goto(x,-330)
    t.pendown()
    t.begin_fill()
    t.circle(1)
    t.end_fill()

def desenha_linhas_campo():
    verdes(-300)
    verdes(-100)
    verdes(100)
    linhas_laterais()
    linha_central()
    circulo_central()
    baliza_L()
    baliza_R()
    cantos()
    bancadas()
    fora_campo()
    suplentes_red(-150)
    suplentes_red(-130)
    suplentes_red(-110)
    suplentes_red(-90)
    suplentes_red(-70)
    suplentes_red(-50)
    suplentes_blue(150)
    suplentes_blue(130)
    suplentes_blue(110)
    suplentes_blue(90)
    suplentes_blue(70)
    suplentes_blue(50)

#desenhar o campo
#---------------------------------------------------------------------------------------------------------------------------------------
def criar_bola():
    bola = t.Turtle()
    bola.penup()
    bola.shape("circle")
    bola.color("black")
    bola.shapesize(DEFAULT_TURTLE_SCALE/2)
    bola.setpos(BOLA_START_POS) #criar o jogador
        
    header = random.randint(0,360) #direção aleatória
    if header <90:
        direcao_x = random.randint(2,7) / 10
        direcao_y = random.randint(2,7) / 10
    elif header <= 180:
        direcao_x = -random.randint(2,7) / 10
        direcao_y = random.randint(2,7) / 10
    elif header < 270:
        direcao_x = -random.randint(2,7) / 10
        direcao_y = -random.randint(2,7) / 10
    elif header <= 360:
        direcao_x = random.randint(2,7) / 10
        direcao_y = -random.randint(2,7) / 10 #dependendo da direção, a direção da bola varia
    
    bola.setheading(header)
    
    Dicionario_bola = {"objecto": bola, "direcao_nos_xx": direcao_x, "direcao_nos_yy": direcao_y, "posicao_anterior_da_bola": None} #devolve o dicionário com os valores
    
    '''
    Função responsável pela criação da bola. 
    Deverá considerar que esta tem uma forma redonda, é de cor preta, 
    começa na posição BOLA_START_POS com uma direção aleatória. 
    Deverá ter em conta que a velocidade da bola deverá ser superior à dos jogadores. 
    A função deverá devolver um dicionário contendo 4 elementos: o objeto bola, 
    a sua direção no eixo dos xx, a sua direção no eixo dos yy, 
    e um elemento inicialmente a None que corresponde à posição anterior da mesma.
    '''
    return Dicionario_bola


#------------------------------------------------------------------------------------------------------------------------


def cria_jogador(x_pos_inicial, y_pos_inicial, cor):
    jogador_bola = t.Turtle()
    jogador_bola.penup()
    jogador_bola.shape("circle")
    jogador_bola.shapesize(DEFAULT_TURTLE_SCALE, DEFAULT_TURTLE_SCALE)
    jogador_bola.color(cor)
    jogador_bola.setposition(x_pos_inicial, y_pos_inicial)
    
    ''' Função responsável por criar e devolver o objeto que corresponde a um jogador (um objecto Turtle). 
    A função recebe 3 argumentos que correspondem às coordenadas da posição inicial 
    em xx e yy, e a cor do jogador. A forma dos jogadores deverá ser um círculo, 
    cujo seu tamanho deverá ser definido através da função shapesize
    do módulo \texttt{turtle}, usando os seguintes parâmetros: 
    stretch_wid=DEFAULT_TURTLE_SCALE, stretch_len=DEFAULT_TURTLE_SCALE. '''
    
    return jogador_bola

#criar o jogador
#------------------------------------------------------------------------------------------------------------------------------------

def init_state():
    estado_jogo = {}
    estado_jogo['bola'] = None
    estado_jogo['jogador_vermelho'] = None
    estado_jogo['jogador_azul'] = None
    estado_jogo['var'] = {
        'bola' : [],
        'jogador_vermelho' : [],
        'jogador_azul' : [],
    }
    estado_jogo['pontuacao_jogador_vermelho'] = 0
    estado_jogo['pontuacao_jogador_azul'] = 0
    return estado_jogo

def cria_janela():
    #create a window and declare a variable called window and call the screen()
    window=t.Screen()
    window.title("Foosball Game")
    window.bgcolor("green")
    window.setup(width = LARGURA_JANELA,height = ALTURA_JANELA)
    window.tracer(0)
    return window

def cria_quadro_resultados():
    #Code for creating pen for scorecard update
    quadro=t.Turtle()
    quadro.speed(0)
    quadro.color("Blue")
    quadro.penup()
    quadro.hideturtle()
    quadro.goto(0,260)
    quadro.write("Player A: 0\t\tPlayer B: 0 ", align="center", font=('Monaco',24,"normal"))
    return quadro

def terminar_jogo(estado_jogo):
    numero_jogos = 1
    ficheiro_historico_resultados = open("historico_resultados.csv","a+")

    ficheiro_historico_resultados.seek(0)
    texto = ficheiro_historico_resultados.readline()

    if (texto == ''):
        ficheiro_historico_resultados.writelines("NJogo, JogadorVermelho, JogadorAzul\n")
    
    for linha in ficheiro_historico_resultados:
        numero_jogos += 1
    ficheiro_historico_resultados.write(str(numero_jogos))
    ficheiro_historico_resultados.write(",")
    ficheiro_historico_resultados.write(str(estado_jogo['pontuacao_jogador_vermelho']))
    ficheiro_historico_resultados.write(",")
    ficheiro_historico_resultados.write(str(estado_jogo['pontuacao_jogador_azul']))
    ficheiro_historico_resultados.write("\n")
    
    '''
     Função responsável por terminar o jogo. Nesta função, deverá atualizar o ficheiro 
     ''historico_resultados.csv'' com o número total de jogos até ao momento, 
     e o resultado final do jogo. Caso o ficheiro não exista, 
     ele deverá ser criado com o seguinte cabeçalho: 
     NJogo,JogadorVermelho,JogadorAzul.
    '''
    print("Adeus")
    estado_jogo['janela'].bye()

#abre o ficheiro "historico_resultados.csv" em modo de ler e adicionar, vai para a primeira linha, se estiver vazia adiciona o cabçalho, escreve o pedido
#-------------------------------------------------------------------------------------------

def setup(estado_jogo, jogar):
    janela = cria_janela()
    #Assign keys to play
    janela.listen()
    if jogar:
        janela.onkeypress(functools.partial(jogador_cima, estado_jogo, 'jogador_vermelho') ,'w') #chama a função jogador_cima, com os parâmetros estado_jogo e "jogador_vermelho" quando a tecla w é pressionada
        janela.onkeypress(functools.partial(jogador_baixo, estado_jogo, 'jogador_vermelho') ,'s')
        janela.onkeypress(functools.partial(jogador_esquerda, estado_jogo, 'jogador_vermelho') ,'a')
        janela.onkeypress(functools.partial(jogador_direita, estado_jogo, 'jogador_vermelho') ,'d')
        janela.onkeypress(functools.partial(jogador_cima, estado_jogo, 'jogador_azul') ,'Up')
        janela.onkeypress(functools.partial(jogador_baixo, estado_jogo, 'jogador_azul') ,'Down')
        janela.onkeypress(functools.partial(jogador_esquerda, estado_jogo, 'jogador_azul') ,'Left')
        janela.onkeypress(functools.partial(jogador_direita, estado_jogo, 'jogador_azul') ,'Right')
        janela.onkeypress(functools.partial(terminar_jogo, estado_jogo) ,'Escape')
        quadro = cria_quadro_resultados()
        estado_jogo['quadro'] = quadro
    desenha_linhas_campo()
    bola = criar_bola()
    jogador_vermelho = cria_jogador(-((ALTURA_JANELA / 2) + LADO_MENOR_AREA), 0, "red")
    jogador_azul = cria_jogador(((ALTURA_JANELA / 2) + LADO_MENOR_AREA), 0, "blue")
    estado_jogo['janela'] = janela
    estado_jogo['bola'] = bola
    estado_jogo['jogador_vermelho'] = jogador_vermelho
    estado_jogo['jogador_azul'] = jogador_azul
    


def update_board(estado_jogo):
    estado_jogo['quadro'].clear()
    estado_jogo['quadro'].write("Player A: {}\t\tPlayer B: {} ".format(estado_jogo['pontuacao_jogador_vermelho'], estado_jogo['pontuacao_jogador_azul']),align="center",font=('Monaco',24,"normal"))

def movimenta_bola(estado_jogo):
    bola = estado_jogo['bola']['objecto']
    avancar_x = estado_jogo['bola']['direcao_nos_xx']
    avancar_y = estado_jogo['bola']['direcao_nos_yy']
    
    guarda_posicoes_para_var(estado_jogo)
    
    x_bola = bola.xcor() + avancar_x
    y_bola = bola.ycor() + avancar_y
    bola.goto(x_bola, y_bola)
    estado_jogo['bola']['posicao_anterior_da_bola'] = bola.position() #atualizar o valor da chave com a nova posicao da bola
    '''
    Função responsável pelo movimento da bola que deverá ser feito tendo em conta a
    posição atual da bola e a direção em xx e yy.
    '''
    return estado_jogo

#vai buscar os valores ao dicionário da bola, guarda a posição da bola com a função, adiciona os valores à posição da bola, desloca a bola e guarda no dicionário da bola
#------------------------------------------------------------------------------------

def verifica_colisoes_ambiente(estado_jogo):
    bola = estado_jogo['bola']['objecto']
    bola.dx = estado_jogo['bola']['direcao_nos_xx']
    bola.dy = estado_jogo['bola']['direcao_nos_yy']
    x_cor = bola.xcor()
    y_cor = bola.ycor() #vai buscar os valores

    # Limites da tela
    limite_horizontal = LARGURA_JANELA / 2
    limite_vertical = ALTURA_JANELA / 2  #define os limites

    # Verificação de colisões com as bordas
    if x_cor > limite_horizontal - RAIO_BOLA or x_cor < -limite_horizontal + RAIO_BOLA:
        estado_jogo['bola']['direcao_nos_xx'] *= -1 #verifica a posição da bola e altera o valor da direção

    if y_cor > limite_vertical - RAIO_BOLA or y_cor < -limite_vertical + RAIO_BOLA:
        estado_jogo['bola']['direcao_nos_yy'] *= -1 #verifica a posição da bola e altera o valor da direção

    # Atualiza a posição da bola
    bola.setx(x_cor + estado_jogo['bola']['direcao_nos_xx']) #define a posição nova
    bola.sety(y_cor + estado_jogo['bola']['direcao_nos_yy']) 


    '''
    Função responsável por verificar se há colisões com os limites do ambiente, 
    atualizando a direção da bola. Não se esqueça de considerar que nas laterais, 
    fora da zona das balizas, a bola deverá inverter a direção onde atingiu o limite.
    '''
    return estado_jogo['bola']['direcao_nos_xx'], estado_jogo['bola']['direcao_nos_yy'] #devolve os valores

#------------------------------------------------------------------------------------


def verifica_golo_jogador_vermelho(estado_jogo):
    bola = estado_jogo['bola']['objecto']
    
    x = bola.xcor() 
    y = bola.ycor() #vai buscar os valores
    
    if x > LARGURA_JANELA/2-LADO_MENOR_AREA and -START_POS_BALIZAS < y < START_POS_BALIZAS: #verifica se está na baliza
        bola.hideturtle() #esconde a bola
        estado_jogo['jogador_azul'].setpos(((ALTURA_JANELA / 2) + LADO_MENOR_AREA), 0)
        estado_jogo['jogador_vermelho'].setpos(-((ALTURA_JANELA / 2) + LADO_MENOR_AREA), 0) #mete os jogadores para as posições iniciais
        estado_jogo['pontuacao_jogador_vermelho'] += 1 #aumenta o resultado
        update_board(estado_jogo) #atualiza a pontuação no ecrã
        
        with open(f"replay_golo_jv_{estado_jogo['pontuacao_jogador_vermelho']}_ja_{estado_jogo['pontuacao_jogador_azul']}.txt", "w") as ficheiro_var: #abre o ficheiro em modo "w"
            for i in range(len(estado_jogo['var']['bola'])): #por cada valor no número do tamanho do estado_jogo['var']['bola']
                posicoes_bola = estado_jogo['var']['bola'][i] #vai buscar o valor no indíce 
                x_posicao_bola = posicoes_bola[0] #dentro do valor, o primeiro vai ser o x e o segundo o y
                y_posicao_bola = posicoes_bola[1]
                
                ficheiro_var.write("%.3f,%.3f;" % (round(x_posicao_bola), round(y_posicao_bola))) #escreve no ficheiro
            ficheiro_var.write("\n")
                
            for i in range(len(estado_jogo['var']['jogador_vermelho'])):
                posicoes_jogador_vermelho = estado_jogo['var']['jogador_vermelho'][i]
                x_posicao_jogador_vermelho = posicoes_jogador_vermelho[0]
                y_posicao_jogador_vermelho = posicoes_jogador_vermelho[1]
                
                ficheiro_var.write("%.3f,%.3f;" % (round(x_posicao_jogador_vermelho), round(y_posicao_jogador_vermelho)))  #o mesmo que a bola
            ficheiro_var.write("\n")
                
            for i in range(len(estado_jogo['var']['jogador_azul'])):
                posicoes_jogador_azul = estado_jogo['var']['jogador_azul'][i]
                x_posicao_jogador_azul = posicoes_jogador_azul[0]
                y_posicao_jogador_azul = posicoes_jogador_azul[1]
                
                ficheiro_var.write("%.3f,%.3f;" % (round(x_posicao_jogador_azul), round(y_posicao_jogador_azul)))    #o mesmo que a bola
            ficheiro_var.write("\n")
            
        
        estado_jogo['var']['bola'].clear()
        estado_jogo['var']['jogador_vermelho'].clear()
        estado_jogo['var']['jogador_azul'].clear() #limpa os valores

            
        estado_jogo['bola'] = criar_bola() #cria uma nova bola
        movimenta_bola(estado_jogo) #movimenta a bola
    
    '''
    Função responsável por verificar se um determinado jogador marcou golo. 
    Para fazer esta verificação poderá fazer uso das constantes: 
    LADO_MAIOR_AREA e 
    START_POS_BALIZAS. 
    Note que sempre que há um golo, deverá atualizar a pontuação do jogador, 
    criar um ficheiro que permita fazer a análise da jogada pelo VAR, 
    e reiniciar o jogo com a bola ao centro. 
    O ficheiro para o VAR deverá conter todas as informações necessárias 
    para repetir a jogada, usando as informações disponíveis no objeto 
    estado_jogo['var']. O ficheiro deverá ter o nome 
    
    replay_golo_jv_[TotalGolosJogadorVermelho]_ja_[TotalGolosJogadorAzul].txt 
    
    onde [TotalGolosJogadorVermelho], [TotalGolosJogadorAzul] 
    deverão ser substituídos pelo número de golos marcados pelo jogador vermelho 
    e azul, respectivamente. Este ficheiro deverá conter 3 linhas, estruturadas 
    da seguinte forma:
    Linha 1 - coordenadas da bola;
    Linha 2 - coordenadas do jogador vermelho;
    Linha 3 - coordenadas do jogador azul;
    
    Em cada linha, os valores de xx e yy das coordenadas são separados por uma 
    ',', e cada coordenada é separada por um ';'.
    '''

def verifica_golo_jogador_azul(estado_jogo):
    bola = estado_jogo['bola']['objecto']
    
    x = bola.xcor()
    y = bola.ycor()
    
    if -LARGURA_JANELA/2+LADO_MENOR_AREA > x and -START_POS_BALIZAS < y < START_POS_BALIZAS:
        bola.hideturtle()       
        estado_jogo['jogador_azul'].setpos(((ALTURA_JANELA / 2) + LADO_MENOR_AREA), 0)
        estado_jogo['jogador_vermelho'].setpos(-((ALTURA_JANELA / 2) + LADO_MENOR_AREA), 0)
        estado_jogo['pontuacao_jogador_azul'] += 1
        update_board(estado_jogo)
        
        with open(f"replay_golo_jv_{estado_jogo['pontuacao_jogador_vermelho']}_ja_{estado_jogo['pontuacao_jogador_azul']}.txt", "w") as ficheiro_var:
            for i in range(len(estado_jogo['var']['bola'])):
                posicoes_bola = estado_jogo['var']['bola'][i]
                x_posicao_bola = posicoes_bola[0]
                y_posicao_bola = posicoes_bola[1]
                
                ficheiro_var.write("%.3f,%.3f;" % (round(x_posicao_bola), round(y_posicao_bola)))
            ficheiro_var.write("\n")
                
            for i in range(len(estado_jogo['var']['jogador_vermelho'])):
                posicoes_jogador_vermelho = estado_jogo['var']['jogador_vermelho'][i]
                x_posicao_jogador_vermelho = posicoes_jogador_vermelho[0]
                y_posicao_jogador_vermelho = posicoes_jogador_vermelho[1]
                
                ficheiro_var.write("%.3f,%.3f;" % (round(x_posicao_jogador_vermelho), round(y_posicao_jogador_vermelho)))
            ficheiro_var.write("\n")
                
            for i in range(len(estado_jogo['var']['jogador_azul'])):
                posicoes_jogador_azul = estado_jogo['var']['jogador_azul'][i]
                x_posicao_jogador_azul = posicoes_jogador_azul[0]
                y_posicao_jogador_azul = posicoes_jogador_azul[1]
                
                ficheiro_var.write("%.3f,%.3f;" % (round(x_posicao_jogador_azul), round(y_posicao_jogador_azul)))    
            ficheiro_var.write("\n")
            
        estado_jogo['var']['bola'].clear()
        estado_jogo['var']['jogador_vermelho'].clear()
        estado_jogo['var']['jogador_azul'].clear()

        estado_jogo['bola'] = criar_bola()
        movimenta_bola(estado_jogo) 
    '''
    Função responsável por verificar se um determinado jogador marcou golo. 
    Para fazer esta verificação poderá fazer uso das constantes: 
    LADO_MAIOR_AREA e 
    START_POS_BALIZAS. 
    Note que sempre que há um golo, deverá atualizar a pontuação do jogador, 
    criar um ficheiro que permita fazer a análise da jogada pelo VAR, 
    e reiniciar o jogo com a bola ao centro. 
    O ficheiro para o VAR deverá conter todas as informações necessárias 
    para repetir a jogada, usando as informações disponíveis no objeto 
    estado_jogo['var']. O ficheiro deverá ter o nome 
    
    replay_golo_jv_[TotalGolosJogadorVermelho]_ja_[TotalGolosJogadorAzul].txt 
    
    onde [TotalGolosJogadorVermelho], [TotalGolosJogadorAzul] 
    deverão ser substituídos pelo número de golos marcados pelo jogador vermelho 
    e azul, respectivamente. Este ficheiro deverá conter 3 linhas, estruturadas 
    da seguinte forma:
    Linha 1 - coordenadas da bola;
    Linha 2 - coordenadas do jogador vermelho;
    Linha 3 - coordenadas do jogador azul;
    
    Em cada linha, os valores de xx e yy das coordenadas são separados por uma 
    ',', e cada coordenada é separada por um ';'.  #o mesmo que o outro
    '''


def verifica_golos(estado_jogo):
    verifica_golo_jogador_vermelho(estado_jogo)
    verifica_golo_jogador_azul(estado_jogo)


def verifica_toque_jogador_azul(estado_jogo):
    '''
    Função responsável por verificar se o jogador tocou na bola. 
    Sempre que um jogador toca na bola, deverá mudar a direção desta.
    '''
    jogador_azul = estado_jogo['jogador_azul']
    bola = estado_jogo['bola']['objecto']  #vai buscar valores
    if jogador_azul.distance(bola) <= RAIO_JOGADOR + RAIO_BOLA + 7.5: #se a distância entre o centro das duas turtles for menor que aquele valor
        bola.setpos(estado_jogo['bola']['posicao_anterior_da_bola']) #mete a bola na posição anterior
        diferenca_x = bola.xcor() - jogador_azul.xcor()
        diferenca_y = bola.ycor() - jogador_azul.ycor()
        if abs(diferenca_x) > abs(diferenca_y):
            estado_jogo['bola']['direcao_nos_xx'] *= -1 #inverte o valor
        else:
            estado_jogo['bola']['direcao_nos_yy'] *= -1 



def verifica_toque_jogador_vermelho(estado_jogo):
    '''
    Função responsável por verificar se o jogador tocou na bola. 
    Sempre que um jogador toca na bola, deverá mudar a direção desta.
    '''
    jogador_vermelho = estado_jogo['jogador_vermelho']
    bola = estado_jogo['bola']['objecto']
    if jogador_vermelho.distance(bola) <= RAIO_JOGADOR + RAIO_BOLA + 7.5:
        bola.setpos(estado_jogo['bola']['posicao_anterior_da_bola'])
        diferenca_x = bola.xcor() - jogador_vermelho.xcor()
        diferenca_y = bola.ycor() - jogador_vermelho.ycor()
        if abs(diferenca_x) > abs(diferenca_y):
            estado_jogo['bola']['direcao_nos_xx'] *= -1 
        else:
            estado_jogo['bola']['direcao_nos_yy'] *= -1 


def guarda_posicoes_para_var(estado_jogo):
    estado_jogo['var']['bola'].append(estado_jogo['bola']['objecto'].pos())
    estado_jogo['var']['jogador_vermelho'].append(estado_jogo['jogador_vermelho'].pos())
    estado_jogo['var']['jogador_azul'].append(estado_jogo['jogador_azul'].pos())

def main():
    estado_jogo = init_state()
    setup(estado_jogo, True)
    while True:
        estado_jogo['janela'].update()
        if estado_jogo['bola'] is not None:
            movimenta_bola(estado_jogo)
        verifica_colisoes_ambiente(estado_jogo)
        verifica_golos(estado_jogo)
        if estado_jogo['jogador_vermelho'] is not None:
            verifica_toque_jogador_azul(estado_jogo)
        if estado_jogo['jogador_azul'] is not None:
            verifica_toque_jogador_vermelho(estado_jogo)

if __name__ == '__main__':
    main()