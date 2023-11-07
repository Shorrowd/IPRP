import random
pontos_inicais = int(input("Introduza o numero de pontos iniciais: "))

dado = random.randint(1,6)

numero_de_jogadas = 1

pontos = pontos_inicais


if pontos > 0:
    if dado == 6:
        pontos += 14 
    else:
        pontos = pontos - dado
    numero_de_jogadas += 1

print(pontos)
print("Foram precisas ", numero_de_jogadas, " jogadas para o jogador perder ", pontos, " pontos.")