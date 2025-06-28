input_number = input("введите число: ")

digit_counter = {}

for char in input_number:
    if char.isdigit():
        if char in digit_counter:
            digit_counter[char] += 1
        else:
            digit_counter[char] = 1

for digit, count in digit_counter.items():
    print(f"{digit}: {count}")