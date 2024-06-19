# для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
# сохранить информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
# Использовать модуль pickle для сериализации и десериализации объектов Python в
# бинарном формате

import pickle
from PZ_16_1 import Callendar

def save_def(circle, filename):
    with open(f'{filename}.bin', 'wb') as file:
        pickle.dump(circle, file)

def load_def(filename):
    with open(f'{filename}.bin', 'rb') as file:
        return pickle.load(file)


c1 = Callendar(1231,9,10)
c2 = Callendar(2006,8,26)
c3 = Callendar(1812,11,9)
save_def(c1,'c1')
save_def(c2,'c2')
save_def(c3,'c3')
load_def('c3')
