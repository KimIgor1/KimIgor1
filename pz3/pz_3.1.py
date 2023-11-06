#Вариант 15
#Даны три целых числа: А, В, С. Проверить истинность высказывания:
#«Ровно одно из чисел А, В, С положительное».
a = input("Введите число А: ")
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print('Ошибка ввода, повторите заново')
        a = input("Введите число A: ")
b = input("Введите число В: ")
while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print('Ошибка ввода, повторите заново')
        b = input("Введите число B: ")
c = input("Введите число С: ")
while type(c) != int:
    try:
        c = int(c)
    except ValueError:
        print('Ошибка ввода, повторите заново')
        c = input("Введите число C: ")

if a > 0 and b <= 0 and c <= 0:
    print("Высказывание истинно")
elif a <= 0 and b > 0 and c <= 0:
    print("Высказывание истинно")
elif a <= 0 and b <= 0 and c > 0:
    print("Высказывание истинно")
else:
    print("Высказывание ложно")