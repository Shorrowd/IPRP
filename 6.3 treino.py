l1 = [1,2,3]
l2 = ["a","b","c"]

def alterna(l1,l2):
    l3 = []
    for i in range(len(l1)):
        l3.append(l1[i])
        l3.append(l2[i])

    return l3

print (alterna(l1,l2))