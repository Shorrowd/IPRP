print("Introduz uma cadeia de caracteres")
cadeia = input()

vogais = "AEIOUaeiou"

cadeia_nova = ""

for letra in cadeia:
    
    if letra in vogais:
        cadeia_nova = cadeia_nova + " "
    else:
        cadeia_nova = cadeia_nova + letra
        
print(cadeia_nova)    