def sos(t,m):
    k=[]
    for i in range(len(t), -1, -1):
        k += [t[i*2 % len(t)]]
        k += [m[i*2 % len(m)]]
    return k
t = [1,2,3]
m = t[::-1] 
print(sos(t,m))

#Explicar em casa