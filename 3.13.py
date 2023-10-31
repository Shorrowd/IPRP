print("Introduza varias letras")
tudo = str(input())

vogais = "aeiou"

for char in vogais:
    tudo = tudo.replace(char, " ")
print(tudo)