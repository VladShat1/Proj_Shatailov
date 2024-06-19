# Создайте базовый класс "Животное" со свойствами "вид", "количество лап", "цвет
# шерсти". От этого класса унаследуйте класс "Собака" и добавьте в него свойства
# "кличка" и "порода".
class Animal:
    def __init__(self, species, num_paws, fur_color):
        self.species = species
        self.num_legs = num_paws
        self.fur_color = fur_color

class Dog(Animal):
    def __init__(self, species, num_paws, fur_color, name, breed):
        super().__init__(species, num_paws, fur_color)
        self.name = name
        self.breed = breed

# Пример использования классов
dog1 = Dog("Собака", 4, "рыжий", "Барон", "Лабрадор")

