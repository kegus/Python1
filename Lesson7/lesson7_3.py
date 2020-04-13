# 3. Реализовать программу работы с органическими клетками

class Cell:
    def __init__(self, cell_cnt):
        if cell_cnt < 0:
            print('Не может быть отрицательного количества клеток')
            self.cell_cnt = 0
        else:
            self.cell_cnt = cell_cnt

    def __str__(self):
        return f'клетка состоит из {self.cell_cnt} ячеек'

    def __add__(self, other):
        return Cell(self.cell_cnt + other.cell_cnt)

    def __sub__(self, other):
        if self.cell_cnt < other.cell_cnt:
            print('Не может быть отрицательного количества клеток')
            return Cell(0)
        else:
            return Cell(self.cell_cnt - other.cell_cnt)

    def __mul__(self, other):
        return Cell(self.cell_cnt * other.cell_cnt)

    def __truediv__(self, other):
        if other.cell_cnt > 0:
            return Cell(self.cell_cnt // other.cell_cnt)
        else:
            return Cell(0)

    def make_order(self, cnt_per_row):
        res = ''
        tmp_cell_cnt = self.cell_cnt
        while tmp_cell_cnt > cnt_per_row:
            tmp_cell_cnt -= cnt_per_row
            res += '*' * cnt_per_row + '\n'
        res += '*' * tmp_cell_cnt + '\n'
        return res


cell1 = Cell(17)
cell2 = Cell(3)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell2 - cell1)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell1.make_order(4))
