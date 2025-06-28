def reverse_first_k_in_blocks(s, k):
    chars = list(s)

    for start_block in range(0, len(chars), 2 * k):
        left = start_block
        right = min(start_block + k - 1, len(chars) - 1)

        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

    return ''.join(chars)

print(reverse_first_k_in_blocks("abcdefg", 2))
print(reverse_first_k_in_blocks("abcd", 2))
