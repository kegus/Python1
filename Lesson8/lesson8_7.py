# 7. Операции с комплексными числами

class MyComplex:
    def __init__(self, re, im):
        self.number = (re, im)

    def __str__(self):
        return f'{self.number[0]}+{self.number[1]}i'

    def __add__(self, other):
        return MyComplex(self.number[0] + other.number[0], self.number[1] + other.number[1])

    def __mul__(self, other):
        re = self.number[0] * other.number[0] - self.number[1] * other.number[1]
        im = self.number[0] * other.number[1] + self.number[1] * other.number[0]
        return MyComplex(re, im)


c1 = MyComplex(2, 3)
c2 = MyComplex(4, 7)

print(f'c1+c2 = {c1 + c2}')
print(f'c1*c2 = {c1 * c2}')
