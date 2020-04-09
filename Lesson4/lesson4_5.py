# 5. Чётные числа от 100 до 1000
from functools import reduce

new_list = [val for val in range(100, 1001, 2)]
print(new_list)
print(reduce((lambda x, y: x * y), new_list))
