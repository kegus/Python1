# 5. Суммирование строки чисел
# def calc_sum(input_list):
#     return sum(input_list)
should_break = False
res_sum = 0
while True:
    input_str = input('Введите сроку чисел через пробел или q для выхода: ').strip()
    if 'q' in input_str:
        should_break = True
        input_str = input_str[:input_str.index('q')].strip()
    try:
        res_sum += (lambda x: sum(x))(map(int, input_str.split()))
        # input_list = map(int, input_str.split())
        # res_sum += calc_sum(input_list)
        print(res_sum)
        if should_break:
            break
    except Exception as e:
        print(str(e))
