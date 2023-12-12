#Вариант 14
#Дан список А размера N. Сформировать два новых списка В и С: в список
#В записать все положительные элементы список А, в сисок С — все отрицательные
#(сохраняя исходный порядок следования элементов).
#Вывести вначале размер и содержимое списка В,
#а затем — размер и содержимое списка С.
N = int(input("Введите размер списка: "))
A = []
for _ in range(N):
    A.append(int(input("Введите элемент списка: ")))

B = [x for x in A if x > 0]
C = [x for x in A if x < 0]

print(f"Размер списка B: {len(B)}, содержимое: {B}")
print(f"Размер списка C: {len(C)}, содержимое: {C}")
