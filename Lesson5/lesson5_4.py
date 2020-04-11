# 4. Английские числительные должны заменяться на русские

translate_list = ["один", "два", "три", "четыре"]
with open("eng.txt", mode="r", encoding="utf-8") as f_eng, open("rus.txt", mode="w", encoding="utf-8") as f_rus:
    file_lines = f_eng.readlines()
    for i, words in enumerate(file_lines):
        words = words.split()
        words[0] = translate_list[i]
        words = " ".join(words)
        f_rus.write(words + "\n")
    print("rus.txt is created")
