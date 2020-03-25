# 2. Перевод секунд в hh:mm:ss
cnt_seconds = int(input("Введите количество секунд: "))
cnt_h = cnt_seconds // 3600
cnt_m = (cnt_seconds - cnt_h * 3600) // 60
cnt_s = cnt_seconds - cnt_h * 3600 - cnt_m * 60
if len(str(cnt_h)) < 2:
    cnt_h = '0' + str(cnt_h)
if len(str(cnt_m)) < 2:
    cnt_m = '0' + str(cnt_m)
if len(str(cnt_s)) < 2:
    cnt_s = '0' + str(cnt_s)
print(f'{cnt_h}:{cnt_m}:{cnt_s}')
print(int(cnt_h)*3600, int(cnt_m)*60, int(cnt_s))