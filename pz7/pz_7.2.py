#Вариант 14
#Дана строка-предложение на русском языке.
#Подсчитать количество содержащихся в строке гласных букв.

def count_vowels(sentence):
    vowels = 'аеёиоуыэюя'
    count = 0
    for char in sentence:
        if char.lower() in vowels:
            count += 1
    return count

sentence = input("Введите строку-предложение на русском языке: ")
print("Количество гласных букв в строке:", count_vowels(sentence))