lst = [1,4,7,9,3,2,8,5,6]

def pares_impares(lst):
    soma_pares= 0
    soma_impares = 0

    for i in range(len(lst)):
        if (lst[i] % 2 == 0):
            soma_pares = soma_pares + lst[i]
        else: 
            soma_impares = soma_impares + lst[i]
    return soma_pares, soma_impares

print(pares_impares(lst))