import copy

# Клас Animal з властивостями name та species
# Важливо: простий клас для демонстрації шаблону проектування Prototype
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # Метод speak виводить інформацію про тварину
    def speak(self):
        print(f"Моє ім'я {self.name}, і я {self.species}.")

    # Метод clone реалізує глибоке копіювання об'єкта
    # Важливо: це і є реалізація шаблону Prototype
    def clone(self):
        return copy.deepcopy(self)

# Основна функція
# Важливо: демонструє роботу патерну Prototype на практиці
# Клонований об'єкт змінюється незалежно від оригіналу

def main():
    original_dog = Animal("Рекс", "собака")
    original_dog.speak()

    print("\nКлонування собаки...\n")

    cloned_dog = original_dog.clone()  # створення копії (прототипу)
    cloned_dog.name = "Фінік"  # зміна ім'я клонованої тварини

    # Оригінал не змінюється — важливо для шаблону Prototype
    original_dog.speak()
    cloned_dog.speak()

if __name__ == "__main__":
    main()
