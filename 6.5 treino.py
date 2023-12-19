import random

def dados():
    soma = 0
    soma_par = 0
    for i in range(5):
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        soma =(dado1 + dado2)

        if (soma%2)== 0:
            soma_par += 1
            percentagem = round((soma_par/5)*100)
        
    return percentagem

print(dados(), "%")