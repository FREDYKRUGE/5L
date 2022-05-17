count_of_numbers = int(input())
total_sum = 0
for numbers in range(1, count_of_numbers + 1):
    current_num = int(input())
    total_sum += current_num
print(f"{total_sum}")
