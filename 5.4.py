
t1 = float(input("Introduza a nota do primeiro teste: "))
t2 = float(input("Introduza a nota do segundo teste: "))
t3 = float(input("Introduza a nota do terceiro teste: "))
t4 = float(input("Introduza a nota do quarto teste: "))
e = float(input("Introduza a nota do exame: "))

nota = 0.075 * (t1+t2+t3+t4) + 0.7 * e
if t1 or t2 or t3 or t4 or e > 20 and t1 or t2 or t3 or t4 or e < 0:
    print("Numero Invalido, escolhe entre 0 a 20")
else:
    if nota >= 14:
        print("Aprovado")
    elif nota < 7:
        print("Reprovado")
    elif 7 >= nota < 14:
        print("Oral")


