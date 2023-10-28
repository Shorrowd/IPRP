import random
zona1 = 0
zona2 = 0
zona3 = 0
zona4 = 0

for i in range(10000):
    x = random.uniform(0.0,2.0)
    y = random.uniform(0.0,2.0)
    if x<1 and y>1:
        zona1 += 1
    elif x<1 and x>1:
        zona2 += 1 
    elif x>1 and y<x:
        zona3 += 1
    else:
        zona4 += 1
total = zona1+zona2+zona3+zona4
impar =zona1 + zona3
print(impar/total*100)
        