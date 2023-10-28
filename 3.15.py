print("Introduza uma cadeia de caracteres")
char = str(input())

a = len(char)
i = 0

for i in range(a):
    i_depois = i + a
    char_novo = char[i:i_depois]
    print(char_novo)