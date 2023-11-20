#Вариант 14
#С помощью функций получить вертикальную и горизонтальную линии.
#Линия проводится многократной печатью символа.
#Заключить слово в рамку из полученных линий.

def print_horizontal_line(symbol, length):
    for i in range(length):
        print(symbol, end='')
    print()

def print_vertical_line(symbol, height):
    for i in range(height):
        print(symbol)

def print_word_in_frame(word, frame_symbol):
    word_length = len(word)
    print_horizontal_line(frame_symbol, word_length + 4)
    print_vertical_line(frame_symbol + ' ' * (word_length + 2) + frame_symbol, 1)
    print(f"{frame_symbol} {word} {frame_symbol}")
    print_vertical_line(frame_symbol + ' ' * (word_length + 2) + frame_symbol, 1)
    print_horizontal_line(frame_symbol, word_length + 4)

print_word_in_frame("Good morning", "*")
