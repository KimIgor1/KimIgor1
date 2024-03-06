# создание последовательности из целых положительных и отрицательных чисел
nums = ['32 74 48 -35 90 23 69']
f1 = open('file1.txt', 'w')
f1.writelines(nums)
f1.close()

# исходные данные:
f2 = open('file2.txt', 'w')
f2.write('Исходные данные: ')
f2.write('\n')
f2.writelines(nums)
f2.close()

# количество элементов:
f1 = open('file1.txt')
m = f1.read()
m = m.split()
for i in range (len(m)):
    m[i] = int(m[i])
f1.close()

f2 = open('file2.txt', 'a')
f2.write('\n')
print('Количество элементов: ', len(m), file = f2)
f2.close()

# индекс первого минимального элемента:
m = list(map(int, nums[0].split()))
min_index = m.index(min(m))
# запись результатов в файл file2.txt
f2 = open('file2.txt', 'a')
f2.write(f'индекс первого минимального элемента:{min_index}\n')

# умножаем все элементы на минимальный элемент
int_nums = list(map(lambda x: int(x), nums[0].split()))
min_num = min(int_nums)
new_nums = list(map(lambda x: x * min_num, int_nums))
f2 = open('file2.txt', 'a')
f2.write(f'все перемноженные элементы на минимальный элемент:{new_nums}\n')