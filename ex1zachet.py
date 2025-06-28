input_phrase = input("введите фразу: ")

word_list = input_phrase.split()

abbreviation_result = ''

for current_word in word_list:
    if current_word[0].isalpha():
        abbreviation_result += current_word[0]

print(abbreviation_result.upper())