import random

def generate_random_list(n):
    return [random.randint(-100, 100) for _ in range(n)]

def split_list(lst):
    pos = []
    neg = []
    for x in lst:
        if x >= 0:
            pos.append(x)
        else:
            neg.append(x)
    return pos, neg

def count_elements(lst):
    return len(lst)

if __name__ == "__main__":
    n = int(input("Введите количество элементов в последовательности: "))
    lst = generate_random_list(n)
    print("Исходная последовательность:", lst)
    pos, neg = split_list(lst)
    print("Положительные числа:", pos)
    print("Отрицательные числа:", neg)
    print("Количество положительных чисел:", count_elements(pos))
    print("Количество отрицательных чисел:", count_elements(neg))