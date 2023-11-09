import random

soma = 0 
vezes = 0
soma_par = 0

def jogo(soma, soma_par, vezes):
    lancamentos = random.randint(1,10)
    
    for i in range(lancamentos):
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        soma = (dado1 + dado2)%2
        
        if soma == 0:
            soma_par += 1

        vezes = round((soma_par / lancamentos) * 100)
        
    return vezes

print(jogo(soma, soma_par, vezes),"%")