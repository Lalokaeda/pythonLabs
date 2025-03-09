input_str=input()

number=input_str[0:1]

for i in input_str:
    if i.isdigit():
        number+=i

print(number)