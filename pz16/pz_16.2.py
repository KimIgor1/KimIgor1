import math
class Форма:
    def __init__(self, цвет, тип):
        self.цвет = цвет
        self.тип = тип

class Круг(Форма):
    def __init__(self, цвет, тип, радиус):
        super().__init__(цвет, тип)
        self.радиус = радиус

    def площадь(self):
        return math.pi * self.радиус ** 2

    def периметр(self):
        return 2 * math.pi * self.радиус

круг = Круг('красный', 'круг', 5)
print(f'Площадь круга: {круг.площадь()}')
print(f'Периметр круга: {круг.периметр()}')