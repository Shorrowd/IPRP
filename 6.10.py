autor = {"php":"Rasmus Lerdorf","perl":"Larry Wall","tcl":"John Ousterhout","awk":"Brian Kerninghan","java":"James Gosling","parrot":"Simon Cozens","python":"GuidovanRossum","xpto":"zxcv",}
autor2 ={"casa":"home"}
Guido_van_Rossum = {}
x = 0

autor.update(autor2)
print ("Autor update: ", autor)

autor["python"] = "Guido van Rossum"
print("Novo autor: ", autor)

del autor ['xpto']
print ("Sem xpto: ", autor)

for elem in sorted(autor.keys()):
    x += 1
   
print ("Existem ",x, "elementos")

if 'c++'  in autor:
    print("Existe uma entrada")
else:
    print("Não existe uma entrada")
