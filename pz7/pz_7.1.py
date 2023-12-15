#Вариант 14
#Дана строка. Подсчитать количество содержащихся в ней прописных латинских букв.
def count_uppercase_letters(string):
    count = 0
    for char in string:
        if char.isupper():
            count += 1
    return count

string = input("Введите строку-предложение: ")
print("Количество прописных латинских букв в строке: ", count_uppercase_letters(string))