nums=input().split()

has_duplicates = len(nums) != len(set(nums))

print(has_duplicates)