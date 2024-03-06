# Чтение изначального файла и подсчет пробельных символов
with open('text18-14.txt', 'r', encoding='utf-16') as file:
    content = file.read()
    spaces_count = content.count(' ')

print(content)

print("\nКоличество пробельных символов:", spaces_count)

# Замена символов третьей строки на их ASCII коды
lines = content.splitlines()
if len(lines) > 2:
    ascii_line = ''
    for char in lines[2]:
        ascii_line += str(ord(char)) + ' '
    ascii_line = ascii_line.strip()

    lines[2] = ascii_line

    with open('output.txt', 'w') as file:
        for line in lines:
            file.write(line + '\n')