values=input()
a=float(values[:values.find(", ")])
b=float(values[values.find(", ")+2:])

print(round(a%b))