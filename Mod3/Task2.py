num = input()

if not num.isdigit() or int(num) <= 0:
    print("Неверный ввод")
else:
    print(bin(int(num))[2:], oct(int(num))[2:], hex(int(num))[2:].upper(), sep=", ")