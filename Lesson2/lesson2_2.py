# 2. Обмен значений соседних элементов списка
input_list = [2, 'text', [456], (12, 34), 45.3, None, True]
print('Введиите список или <Enter> для списка по умолчанию: \n')
read_list = input()
if read_list:
    input_list = read_list.split(',')
for i in range(len(input_list) // 2):
    tmp_var = input_list[i*2]
    input_list[i*2] = input_list[i*2+1]
    input_list[i*2 + 1] = tmp_var

print(input_list)