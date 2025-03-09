input_str=input()

dot1 = input_str.find('.')
dot2 = input_str.find('.', dot1 + 1)

a=input_str[:dot1]
b=input_str[dot1+1:dot2]
c=input_str[dot2+1:]

print(c)
print(b)
print(a)