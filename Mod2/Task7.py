input_str=input()

comma=input_str.find(", ")

s = input_str[:comma]
i = input_str[comma + 2:]

count=0
for char in s:
            if char == i:
                count += 1
            else:
                break
print(count)