dic = {'autista1':['autista2','autista3','autista4'],'autista2':['autista1','autista7','autista4'],'autista3':['autista1','autista5']}

def twitaaa(dic):
    new_dic = {}
    for seguidor in dic.keys():
        for seguido in dic[seguidor]:
            new_dic.setdefault(seguido,[])
            new_dic[seguido] += [seguidor]
    numero = 0
    for seguido in new_dic.keys():
        if len(new_dic[seguido])>numero:
            numero=len(new_dic[seguido])
            mais_seguidores=seguido
    return mais_seguidores

print(twitaaa(dic))