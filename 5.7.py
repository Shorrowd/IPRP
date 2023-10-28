pal1 = str(input("Introduz uma palavra:"))
pal2 = str(input("Introduz outra palavra:"))

difere = 0
caracteres = len(pal1)
caracteres2 = len(pal2)

if (caracteres == caracteres2):
    
    for i in range(caracteres):
        if pal1[i] != pal2[i]:
            difere += 1
    if difere/caracteres <0.10:
        print("As palavras são amigas.")
    else:
        print("As palavras não são amigas.")
else:
    print("As palavras não são amigas.")
    
    
    