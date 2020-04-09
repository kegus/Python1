# 6. Учебный предмет и наличие лекционных, практических и лабораторных занятий

reducing_list = ("(л)", "(пр)", "(лаб)")
result = {}
with open("schedule.txt", mode="r", encoding="utf-8") as f:
    file_lines = f.readlines()
    for items in file_lines:
        items = items.split()
        discipline = items[0]
        work_item = []
        for el in items[1:]:
            if el == "—":
                continue
            for check in reducing_list:
                if check in el:
                    el = el.replace(check, "")
                    break
            work_item.append(int(el))
        result[discipline] = sum(work_item)
    print(result)
