array = [1,2,3]

def soma_comulativa(array):
    soma = 0
    resultado = []
    for i in range(len(array)):
        soma += array[i]
        resultado.append(soma)
    return resultado

print(soma_comulativa(array))
