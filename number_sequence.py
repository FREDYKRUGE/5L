import sys

number = int(input())
max_number = -sys.maxsize
min_number = sys.maxsize
for num in range(number):
    numbers = int(input())
    if numbers > max_number:
        max_number = numbers
    if numbers < min_number:
        min_number = numbers
print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
