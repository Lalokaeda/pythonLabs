def nod(a, b):
    if b == 0:
        return a
    return nod(b, a % b)

a, b = map(int, input().split())

result = nod(a, b)
print(result)