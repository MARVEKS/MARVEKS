import copy

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print(f"Моє ім'я {self.name}, і я {self.species}.")

    def clone(self):
        return copy.deepcopy(self)


def main():
    original_dog = Animal("Рекс", "собака")
    original_dog.speak()

    print("\nКлонування собаки...\n")

    cloned_dog = original_dog.clone()
    cloned_dog.name = "Фінік"

    original_dog.speak()
    cloned_dog.speak()

if __name__ == "__main__":
    main()
