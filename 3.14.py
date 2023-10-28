print("Introduza uma cadeia de caracteres")
char = str(input())

print("Introduza um numero inteiro postivo abaixo ou igual ao numero de caracteres")
num = int(input())
a = len(char)
i = 0

a_max= a -2

while (i <a_max):
    i_depois = i + num
    char_novo = char[i:i_depois]
    print(char_novo)
    i = i + 1