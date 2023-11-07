texto = input("Introduza um texto: ")
letra_substituir = input("Introduza uma letra: ")

def subs_por_occur(texto, letra_substituir):
    contador = 1
    resultado = ""

    for letra in texto:
        if letra == letra_substituir:
            resultado += str(contador)
            contador += 1
        else:
            resultado += letra

    return resultado

nova_palavra = subs_por_occur(texto, letra_substituir)
print(nova_palavra)