text = input("Introduza um texto: ")
palavra = input("Introduza uma palavra: ")

palavra_inveritda = palavra[::-1]

def encontra(text,palavra):
    if palavra in text:
        print("True")
    elif palavra not in text:
        if palavra_inveritda in text:
            print("True")
        else:
            print("False")

encontra(text,palavra)