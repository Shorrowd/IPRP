ficheiro_original = input("Introduz o nome do ficheiro designado: ")
ficheiro_copia = input("Introduza o nome do ficheiro copiado: ")

def copias(ficheiro_original,ficheiro_copia):
    with open(ficheiro_copia, "w") as copia:
        original = open(ficheiro_original, "r")
        for linha in original:
            copia.write(linha)

copias(ficheiro_original,ficheiro_copia)