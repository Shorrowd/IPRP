print("Introduza um pH de uma solução quimica: ")
ph = float(input())

if 0 > ph > 14:
    print("pH inválido")
else:
    if ph > 7:
        print("A solução é Básica.")
    elif ph == 7:
        print("A solução é Neutra.")
    elif ph < 7:
        print("A solução é Ácida.")