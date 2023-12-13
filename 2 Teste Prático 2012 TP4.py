amigos = { ' pedro ' :[ ' rui '] , ' rui ' :[ ' joao '] ,' joao ' :[ ' rui ' , ' pedro ' ]}

def verdadeiros(dicio,nome):
    lista=[]
    if nome not in dicio.keys():
        return None
    else:
        amigos=dicio[nome]
        for amigo in amigos:
            if nome in dicio[amigo]:
                lista.append(amigo)
        return lista
    
print (verdadeiros (amigos , 'joao' ))