numero = 0 
quadrado = 0 

linhas = int(input("Introduz o numero de linhas que pretendes que o quadro tenha: "))

print('%s    %s' % ('Numero', 'Quadrado'))

for i in range(1, linhas + 1):
    numero += 1
    quadrado = numero ** 2
    print('%6d %11d' % (numero, quadrado))