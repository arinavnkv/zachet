def get_pascal_row(row_index):
    current_row = [0] * (row_index + 1)
    current_row[0] = 1

    for current_row_number in range(1, row_index + 1):
        for position in range(current_row_number, 0, -1):
            current_row[position] = current_row[position] + current_row[position - 1]

    return current_row

print(get_pascal_row(0))
print(get_pascal_row(1))
print(get_pascal_row(3))
