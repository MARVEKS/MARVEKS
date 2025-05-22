class Component:
    def __init__(self, name):
        self.name = name

    def display(self, depth=0):
        pass


class Leaf(Component):
    def display(self, depth=0):
        print("-" * depth + self.name)


class Composite(Component):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, component):
        self.children.append(component)

    def display(self, depth=0):
        print("-" * depth + self.name)
        for child in self.children:
            child.display(depth + 2)

class Computer:
    def turn_on(self):
        print("Комп'ютер увімкнено.")

    def turn_off(self):
        print("Комп'ютер вимкнено.")


class Lights:
    def turn_on(self):
        print("Світло увімкнено.")

    def turn_off(self):
        print("Світло вимкнено.")

class SystemFacade:
    def __init__(self):
        self.menu = self._create_menu()
        self.computer = Computer()
        self.lights = Lights()

    def _create_menu(self):
        root = Composite("Головне Меню")
        root.add(Leaf("Файл"))
        root.add(Leaf("Правка"))
        help_menu = Composite("Допомога")
        help_menu.add(Leaf("Документація"))
        help_menu.add(Leaf("Про програму"))
        root.add(help_menu)
        return root

    def start_system(self):
        print("=== СИСТЕМА ЗАПУСКАЄТЬСЯ ===")
        self.lights.turn_on()
        self.computer.turn_on()
        print("\n== Меню системи ==")
        self.menu.display()

    def shutdown_system(self):
        print("\n=== СИСТЕМА ВИМИКАЄТЬСЯ ===")
        self.computer.turn_off()
        self.lights.turn_off()


if __name__ == "__main__":
    system = SystemFacade()
    system.start_system()
    print("...Система працює...")
    system.shutdown_system()
