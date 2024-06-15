# Сгенерировать словарь вида (0:0, 1:1, 2: 8, 3:27, 4: 64, 5: 125, 6: 216},
# удалить из него первый и последний элементы.
# Отобразить исходный и получившийся словарь. Использовать for, range.


original_dict = {i: i**3 for i in range(7)}
print("Исходный словарь:", original_dict)

new_dict = {key: value for key, value in original_dict.items() if key != 0 and key != 6}
print("Получившийся словарь:", new_dict)

