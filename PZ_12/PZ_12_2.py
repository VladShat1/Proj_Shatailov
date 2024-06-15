# сформировать генератор (yield), который преобразует все буквенные
# символы в строчные
from string import ascii_uppercase
def fu(s):
    yield from [i.lower() if i in ascii_uppercase else i for i in s]
b =fu(input('Введите строку: '))
s = ''
s += ''.join(b)
print(s)