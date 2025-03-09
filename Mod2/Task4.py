def convert_num(n, syst):
    digits = "0123456789ABCDEF"
    result = ""
    while n>0:
        mod = n%syst
        result=digits[mod]+result
        n=n//syst
    return result

num=input()

if not num.isdigit() or int(num) <= 0:
    print("Неверный ввод")
else:
    n = int(num)
    binary=convert_num(n, 2)
    octal=convert_num(n, 8)
    hexadecimal=convert_num(n, 16)
    print(binary, octal, hexadecimal, sep=", ")
