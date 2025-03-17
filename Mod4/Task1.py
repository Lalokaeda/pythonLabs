def compare_nums(*args):
    unique_nums = set(args)
    if (len(unique_nums)==1):
        print("Все числа равны")
        return
    if (len(unique_nums)==len(args)):
        print("Все числа разные")
        return
    print("Есть равные и неравные числа")

input_str=input().split()

compare_nums(*input_str)