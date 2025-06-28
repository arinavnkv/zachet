def fibonacci(total_numbers):
    current_number = 0
    next_number = 1
    for index in range(total_numbers):
        yield current_number
        current_number, next_number = next_number, current_number + next_number

for num in fibonacci(6):
    print(num)