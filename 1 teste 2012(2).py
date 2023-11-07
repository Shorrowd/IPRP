text = input("Introduz um texto: ")
p = int(input("Introduz uma percentagem: "))

remove = int(len(text) * (p/100))

palavra = text[:remove]

print(palavra)

