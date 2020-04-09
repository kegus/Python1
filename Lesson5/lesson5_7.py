# 7. Текстовый файл, содержащий данные о фирмах

result = []
n = 0
profit = 0
with open("firms.txt", mode="r", encoding="utf-8") as f:
    file_line = f.readline()
    while file_line:
        res_firm = {}
        firm = file_line.split()
        firm_profit = int(firm[2]) - int(firm[3])
        res_firm[firm[0]] = firm_profit
        result.append(res_firm)
        if firm_profit > 0:
            profit += firm_profit
            n += 1
        file_line = f.readline()

res_firm = {}
res_firm["average_profit"] = profit / n
result.append(res_firm)
print(result)
