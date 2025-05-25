from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self._name = name 

    @abstractmethod
    def make_sound(self):
        pass

    def info(self):
        print(f"Ім'я: {self._name}")

class Собака(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.__breed = breed

    def make_sound(self):
        print(f"{self._name} Робить: Гав!")

    def get_breed(self):
        return self.__breed

    def set_breed(self, new_breed):
        self.__breed = new_breed

    def info(self):
        super().info()
        print(f"Порода: {self.__breed}")

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

def main():
    dog1 = Собака("Рекс", "Німецька вівчарка")
    cat1 = Кіт("Тімон", "Білий")

    dog1.set_breed("Німецька вівчарка")
    cat1.set_color("Білий")

    animals = [dog1, cat1]

    for animal in animals:
        animal.info()
        animal.make_sound()
        print("-----")

if __name__ == "__main__":
    main()
