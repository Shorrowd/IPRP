cadeia = "x22ddd cbba"

def processa(cadeia):
    acum = 0
    lista = []
    for i in range(len(cadeia)):
        if cadeia[i] != cadeia[i-1]:
            car = cadeia[i]
            pos=i
        if i!= len(cadeia)-1:
            if cadeia[i] == cadeia[i+1]:
                acum += 1
            if cadeia[i] != cadeia[i+1]:
                acum = 0
                lista.append((car,pos,acum))
        if i == len(cadeia)-1:
            if cadeia[i] != cadeia[len(cadeia)-2]:
                lista.append((cadeia[i],i,0))
    return lista

print(processa(cadeia))