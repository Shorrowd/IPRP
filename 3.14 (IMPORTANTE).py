s = "Monty Python"
tamanho_sub = 3

for i_letra in range(len(s)-(tamanho_sub-1)):
    #print("indice: ", i_letra, " elemento: ",s[i_letra])
    print(s[i_letra:i_letra+tamanho_sub])