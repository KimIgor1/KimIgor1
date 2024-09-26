import re

with open('hotline1.txt', 'r', encoding='utf-8') as file:
    text = file.read()

pattern = r'8\(\d{3}\)\d{3}-\d{2}-\d{2}'

phones = re.findall(pattern, text)

print(f'Найдено {len(phones)} номеров телефонов.')

new_text = re.sub(r'Горячая линия', 'Горячая линия Министерства образования Ростовской области', text)

with open('hotline2.txt', 'w', encoding='utf-8') as file:
    file.write(new_text)