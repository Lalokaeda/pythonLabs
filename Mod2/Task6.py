input_str=input()

one_count=0
zero_count=0
for i in input_str:
    if i == '1':
        one_count+=1
    elif i == '0':
        zero_count+=1

if one_count==zero_count:
    print("yes")
else:
    print("no")