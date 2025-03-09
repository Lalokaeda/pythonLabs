square_length=float(input())

perimeter=square_length*4
area=square_length**2
diagonal=(square_length**2*2)**0.5

print(round(perimeter, 2), round(area, 2), round(diagonal, 2), sep=", ")