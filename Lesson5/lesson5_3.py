# 3. Вывести фамилии этих сотрудников из salary.txt

with open("salary.txt", mode="r", encoding="utf-8") as f:
    file_lines = f.readlines()
    sum_salary = 0.0
    i = 1
    for n, words in enumerate(file_lines, 1):
        words = words.split()
        salary = float(words[1])
        if salary > 20000:
            print(f"{i}. {words[0]}. ЗП: {salary}")
            i += 1
        sum_salary += salary
    print(f"Средняя ЗП: {(sum_salary / n):9.2f}")
