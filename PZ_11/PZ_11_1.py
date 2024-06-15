# 1. Средствами языка Python сформировать два текстовых файла (.txt),
# содержащих по одной последовательности из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Элементы первого и второго файлов:
# Количество элементов первого и второго файлов: Количество элементов, общих для двух файлов:
# Количество четных элементов первого файла:
# Количество нечетных элементов второго файла:

# Создаем два текстовых файла и записываем в них последовательности чисел
with open('file1.txt', 'w') as file1:
    file1.write('1 2 3 4 5 6 7 8 9 10')

with open('file2.txt', 'w') as file2:
    file2.write('-1 -2 -3 -4 -5 -6 -7 -8 -9 -10')

# Читаем последовательности чисел из файлов
with open('file1.txt', 'r') as file1:
    sequence1 = list(map(int, file1.read().split()))

with open('file2.txt', 'r') as file2:
    sequence2 = list(map(int, file2.read().split()))

# Создаем новый текстовый файл и записываем результаты обработки элементов
with open('result.txt', 'w') as result_file:
    result_file.write(f"Элементы первого файла: {sequence1}\n")
    result_file.write(f"Элементы второго файла: {sequence2}\n")
    result_file.write(f"Количество элементов первого файла: {len(sequence1)}\n")
    result_file.write(f"Количество элементов второго файла: {len(sequence2)}\n")
    result_file.write(f"Количество четных элементов первого файла: {len([x for x in sequence1 if x % 2 == 0])}\n")
    result_file.write(f"Количество нечетных элементов второго файла: {len([x for x in sequence2 if x % 2 != 0])}\n")
