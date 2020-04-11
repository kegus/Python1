# 5. Подсчитывать сумму чисел в файле

number_list = [2, 7, 56, 24]
try:
    f = open("number.txt", mode="w")
    f.write(" ".join(map(str, number_list)))
except Exception as e:
    print("Произошла ошибка!", str(e))
finally:
    f.close()

try:
    f = open("number.txt", mode="r")
    new_list = map(int, f.readline().split())
    print(sum(new_list))
except Exception as e:
    print("Произошла ошибка!", str(e))
finally:
    f.close()
