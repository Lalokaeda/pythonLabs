input_str=input()

domens=reversed(input_str.split("."))

print(*domens, sep="\n")