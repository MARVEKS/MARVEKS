from abc import ABC, abstractmethod

# Абстрактний клас Animal
# Важливо: демонструє використання абстракції (abstract class) та поліморфізму
class Animal(ABC):
    def __init__(self, name):
        self._name = name  # protected атрибут - доступний у спадкоємців

    @abstractmethod
    def make_sound(self):
        pass  # абстрактний метод — змушує нащадків реалізовувати цей метод

    def info(self):
        print(f"Ім'я: {self._name}")

# Клас Собака наслідує Animal
# Важливо: приклад наслідування, поліморфізму, інкапсуляції (через приватний атрибут __breed)
class Собака(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.__breed = breed  # приватний атрибут

    def make_sound(self):
        print(f"{self._name} Робить: Гав!")

    def get_breed(self):
        return self.__breed

    def set_breed(self, new_breed):
        self.__breed = new_breed

    def info(self):
        super().info()
        print(f"Порода: {self.__breed}")

# Клас Кіт також наслідує Animal
# Важливо: реалізує свою версію make_sound і має свій приватний атрибут __color
class Кіт(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.__color = color

    def make_sound(self):
        print(f"{self._name} Робить: М'яв!")

    def get_color(self):
        return self.__color

    def set_color(self, new_color):
        self.__color = new_color

    def info(self):
        super().info()
        print(f"Колір: {self.__color}")

# Основна функція для демонстрації
# Важливо: демонструється поліморфізм — один і той самий інтерфейс (make_sound, info)
# викликається для об'єктів різних типів (Собака, Кіт)
def main():
    dog1 = Собака("Рекс", "Німецька вівчарка")
    cat1 = Кіт("Тімон", "Білий")

    dog1.set_breed("Німецька вівчарка")
    cat1.set_color("Білий")

    animals = [dog1, cat1]  # Список тварин (Animal)

    for animal in animals:
        animal.info()        # поліморфний виклик
        animal.make_sound()  # поліморфний виклик
        print("-----")

if __name__ == "__main__":
    main()
