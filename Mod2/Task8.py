input_str=input()

string = ""
for i in range(len(input_str)-1):
    if input_str[i:i+1] == " ":
        string+=input_str[i-1:i]
string+=input_str[-1:]
print(string)