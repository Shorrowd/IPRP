pal1 = str(input("Introduz uma palavra: "))
pal2 = str(input("Introduz outra palavra: "))

pala1 = len(pal1)
pala2 = len(pal2)
difere = 0

if (pala1 == pala2):
    for i in range(pala1):
        if pal1[i] != pal2[i]:
            difere += 1
    if difere/pala1 < 0.10:
        print("As palavras são amigas.")
    else:
        print("As palavras não são amigas.")
else:
    print("As palavras não são amigas.")