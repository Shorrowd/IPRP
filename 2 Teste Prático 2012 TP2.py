def conta(lista):
    dicio={}
    for palavra in lista:
        dicio[palavra]=dicio.get(palavra,0)+1
    return dicio

print (conta(["um", "dois", "tres", "dois", "dois", "quatro", "um"]))