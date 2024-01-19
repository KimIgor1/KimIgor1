#Выполнить сортировку словаря d = {'a': 1, 'b': 2, 'c': 3}
d = {'c': 3, 'a': 1, 'b': 2}
d = dict(sorted(d.items(), key=lambda x: x[0]))
print(d)