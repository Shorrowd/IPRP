import random 

sorteio = random.randint(5,10)

print("Serão jogados", sorteio, "vezes.")

par = 0

for i in range(sorteio):
    face = random.randint(1,6)
    if face%2 == 0:
        par += 1

percentagem = (par/sorteio)*100

print(percentagem)