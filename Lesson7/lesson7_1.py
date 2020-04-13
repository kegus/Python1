# 1. Matrix

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        res = ''
        for el in self.matrix:
            res += str(el) + '\n'
        return res

    def __getitem__(self, index):
        return self.matrix[index]

    def __add__(self, other):
        res_x = []
        for i, el1 in enumerate(self.matrix):
            res_y = []
            for j, el2 in enumerate(el1):
                res_y.append(el2 + other[i][j])
            res_x.append(res_y)
        return Matrix(res_x)


input_list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
input_list2 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

matrix1 = Matrix(input_list1)
matrix2 = Matrix(input_list2)
print(matrix1 + matrix2)
