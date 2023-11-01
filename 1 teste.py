def vem(n):
    return 1
def volta(x):
    return vem(x) - 1
def vai(x):
    return vem(x) and volta(x)
n = vai(2)
print(n)