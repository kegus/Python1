# 1.Список с элементами различных типов
input_list = (2, 'text', [456], 45.3, None, True)

for item in input_list:
    print(type(item))
    if item == None:
        print(item, ' = None')
    if item is None:
        print(item, ' is None')