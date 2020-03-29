# 4.Запрос строки, каждое слово выводить с новой строки, пронумеровать и обрезать до 10 слов
max_chars = 10
input_string = input('Введите предложение: ')
input_list = tuple(input_string.split(' '))

for n, word in enumerate(input_list, 1):
    if len(word) > max_chars:
        word = word[:10]
    print(f'{n}. {word}')
