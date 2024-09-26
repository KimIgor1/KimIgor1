import pickle

class Машина:
    def __init__(self, марка, модель, год_выпуска):
        self.марка = марка
        self.модель = модель
        self.год_выпуска = год_выпуска

    def __str__(self):
        return f'Марка: {self.марка}, Модель: {self.модель}, Год выпуска: {self.год_выпуска}'

def save_def(objects, filename):
    with open(filename, 'wb') as f:
        pickle.dump(objects, f)

def load_def(filename):
    with open(filename, 'rb') as f:
        objects = pickle.load(f)
    return objects

машины = [
    Машина('BMW', 'M5', 2021),
    Машина('Mercedes-Benz', 'S-Class', 2022),
    Машина('Audi', 'A8', 2023),
]

save_def(машины, 'машины.dat')

загруженные_машины = load_def('машины.dat')

for машина in загруженные_машины:
    print(машина)