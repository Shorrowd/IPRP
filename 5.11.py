print("Introduza uma numero inteiro: ")        
n = int(input())

fatorial_final = 1

def fatorial(n,fatorial_final):
    for i in range(n):   
        fato = n-i
        fatorial_final = fatorial_final * fato
    print(fatorial_final)

fatorial(n,fatorial_final)