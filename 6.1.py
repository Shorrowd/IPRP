I = [9,10,11,12,13,14,15,16,17,18,19]
numero = len(I)
resultado = I[::-1]
exceto = I[1:10]
soma = 0 
soma2 = 0
print("Numero de idades: ", numero)

print("Inverso: ", resultado)

print("exceto: ", exceto)

print("Maximo e minimo: ", max(I),"e", min(I))

for i in range(numero):
    soma = soma + I[i]

print("A soma dos numero sera: ", soma)

if I.count(17):
    print("Existe um aluno com 17 anos")

referencia = int(input("Escolha um numero da lista: "))
ocurrencias = 0
for i in I:
    if i < referencia :
        ocurrencias += 1

print(ocurrencias)