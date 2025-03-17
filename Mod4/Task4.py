def can_form_palindrome(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
    
    return odd_count <= 1

def build_palindrome(s):
    if not can_form_palindrome(s):
        return "Нельзя составить палиндром из этого слова."
    
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    left_half = []
    middle_char = ''
    
    for char, count in char_count.items():
        if count % 2 != 0:
            middle_char = char
        left_half.extend([char] * (count // 2))
    
    palindrome = ''.join(left_half) + middle_char + ''.join(reversed(left_half))
    return palindrome

input_str = input()

result = build_palindrome(input_str)
print(result)