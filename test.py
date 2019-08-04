for n in range(2,201):
    delitelji = []
    for i in range(2, n):
        if n%i == 0:
            delitelji.append(i)
    if len(delitelji) == 0:
        print(n)

