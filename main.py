
def rabin_karp(pattern_to_find, text, prime_number, number_of_characters=256):
    length_of_pattern = len(pattern_to_find)
    length_of_text = len(text)
    pattern_hash = 0
    text_hash = 0
    pattern_indexes = []
    '''
    Обраховуємо хеш шаблону, який потрібно знайти а також перший хеш стрічки, довжиною шаблону
    Складність таких обрахунків - довжина М шаблону
    '''
    for i in range(length_of_pattern):
        pattern_hash = (number_of_characters * pattern_hash + ord(pattern_to_find[i])) % prime_number
        text_hash = (number_of_characters * text_hash + ord(text[i])) % prime_number

    rest_of_string = length_of_text - length_of_pattern
    '''
      Перевіряємо чи співпадає хеш стрічки з хешем шаблону якщо так - додаємо значення індекса, на якому його знайшли -
       в масив, а самі ітеруємось далі по стрічці.  При цьому міняємо хеш, віднімаючи перший і додаючи наступний
        (ітерація +довжина шаблону) символи. На вихід повертаємо масив з усіма збігами
    '''
    for i in range(rest_of_string + 1):
        if pattern_hash == text_hash:
            pattern_indexes.append("Pattern " + pattern_to_find + " found at index "
                                   + str(i) + "-" + str(i + len(pattern_to_find) - 1))
        if i < rest_of_string:
            text_hash = (number_of_characters * text_hash - ord(text[i]) * pow(number_of_characters, length_of_pattern)
                         + ord(text[i + length_of_pattern])) % prime_number

    return pattern_indexes


if __name__ == '__main__':
    test_prime_number = 997
    with open('in_out/Input.txt', 'r') as input_file:
            text_from_input, pattern_from_input = [line.rstrip() for line in input_file]
    result = rabin_karp(pattern_from_input, text_from_input, test_prime_number)
    print(result)
    with open('in_out/Result.txt', 'w') as file:
        file.write(str(result))
