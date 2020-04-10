# 2. Road

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self, m_depth, depth):
        #                                    переводим в тонны
        return self._length * self._width * m_depth / 1000 * depth


length, width = map(int, input("Введите длину и ширину (м): ").split())
road = Road(length, width)
m_depth, depth = map(int, input("Введите массу (кг) и глубину (см): ").split())
print(f"Нужно {road.calc_mass(m_depth, depth)} тонн")
