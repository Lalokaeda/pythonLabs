input_str = input()
phone_number = ''.join(char for char in input_str if char in '+0123456789')
print(phone_number)