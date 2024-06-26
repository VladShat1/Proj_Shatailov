# 2. Из предложенного текстового файла (text18-29.txt)
# вывести на экран его содержимое. количество символов в тексте.
# Сформировать новый файл,
# в который поместить текст в стихотворной форме предварительно поставив последнюю строку между второй и третьей
# Чтение содержимого файла и вывод на экран
with open('text18-29.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)

# Получение количества символов в тексте
num_chars = len(content)
print(f"Количество символов в тексте: {num_chars}")

# Разделение текста на строки
lines = content.split('\n')

# Формирование нового текста в стихотворной форме
poem = "\n".join(lines[:2]) + "\n" + lines[-1] + "\n" + "\n".join(lines[2:-1])

# Запись нового текста в файл
with open('poem.txt', 'w') as file:
    file.write(poem)
