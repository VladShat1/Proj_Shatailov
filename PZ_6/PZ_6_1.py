#Дан список А размера N и целое число К (1 < K <N).
# Преобразовать список, увеличив каждый его элемент на исходное значение элемента Ак-

try:
    a = [2,1,2,3]
    k = int(input('введите число k '))
    s = a[k]
    for i in range(len(a)):
        a[i] +=s
    print(a)
except:
    print('Ошибка')

