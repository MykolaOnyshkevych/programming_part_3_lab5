def rabin_karp(text_to_find, text, prime_number, number_of_characters=256):
    length_of_pattern = len(text_to_find)
    length_of_text = len(text)
    pattern_hash = 0
    text_hash = 0
    pattern_indexes = []

    for i in range(length_of_pattern):
        pattern_hash = (number_of_characters * pattern_hash + ord(text_to_find[i])) % prime_number
        text_hash = (number_of_characters * text_hash + ord(text[i])) % prime_number
    for i in range(length_of_text - length_of_pattern + 1):
        if pattern_hash == text_hash:
            pattern_indexes.append("Pattern " + text_to_find + " found at index "
                                   + str(i) + "-" + str(i + len(text_to_find) - 1))
        if i < length_of_text - length_of_pattern:
            text_hash = (number_of_characters * (text_hash - ord(text[i]) *
                                                 pow(number_of_characters, length_of_pattern - 1)) +
                         ord(text[i + length_of_pattern])) % prime_number
    return pattern_indexes


if __name__ == '__main__':
    test_prime_number = 101
    with open('Input.txt', 'r') as input_file:
        text_from_input, pattern_from_input = [line.rstrip() for line in input_file]
    result = rabin_karp(pattern_from_input, text_from_input, test_prime_number)
    print(result)
    with open('Result.txt', 'w') as file:
        file.write(str(result))
