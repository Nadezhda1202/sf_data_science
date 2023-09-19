def count_letters(s):

    # Проходимся по каждой букве в строке и увеличиваем счетчик
    for letter in s:
        if letter in letters_count:
            letters_count[letter] += 1
        else:
            letters_count[letter] = 1

    return letters_count

def can_make_word(letters_count):
    # Проверяем, есть ли в строке достаточное количество букв для слова
    count = min(letters_count['s'], letters_count['h'], 
                letters_count['e'], letters_count['r'], 
                letters_count['i'], letters_count['f']//2)

    return count


# Вводим строку
s = input()

# Подсчитываем количество букв в строке
letters_count = {'s':0, 'h':0, 'e':0, 'r':0, 'i':0, 'f':0}
letters_count = count_letters(s)

count = can_make_word(letters_count)
print(count)