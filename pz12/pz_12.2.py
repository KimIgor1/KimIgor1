def digit_generator(string):
    for char in string:
        if char.isdigit():
            yield char

if __name__ == "__main__":
    string = input("Введите строку: ")
    for digit in digit_generator(string):
        print(digit, end='')