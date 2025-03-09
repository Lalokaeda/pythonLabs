values = input() 
space1 = values.find(' ')
space2 = values.find(' ', space1 + 1)

a = int(values[:space1])
b = int(values[space1 + 1:space2])
c = int(values[space2 + 1:])

if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
else:
    if b < c:
        median = b
    elif a > c:
        median = a
    else:
        median = c

print(median)