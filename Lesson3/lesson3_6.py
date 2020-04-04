# 6. Реализовать функцию int_func
def int_func(input_str):
    result = ''
    for i, char in enumerate(input_str):
        if i == 0:
            char = char.upper()
        else:
            char = char.lower()
        result += char
    return result


def my_title(input_str):
    result = ''
    input_list = input_str.split()
    for item in input_list:
        item = int_func(item) + ' '
        result += item
    return result.strip()

print(int_func(input('Введите слово: ')))
print(my_title(input('Введите предложение: ')))
