
class MenuComponent:
    def show(self, indent=0):
        pass


class MenuItem(MenuComponent):
    def __init__(self, name):
        self.name = name

    def show(self, indent=0):
        print("  " * indent + f"- {self.name}")


class Menu(MenuComponent):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, component):
        self.items.append(component)

    def show(self, indent=0):
        print("  " * indent + f"[{self.name}]")
        for item in self.items:
            item.show(indent + 1)

class MenuSystem:
    def __init__(self):
        self.main_menu = Menu("Головне меню")
        self.setup()

    def setup(self):
        file_menu = Menu("Файл")
        file_menu.add(MenuItem("Новий"))
        file_menu.add(MenuItem("Відкрити"))

        edit_menu = Menu("Редагувати")
        edit_menu.add(MenuItem("Копіювати"))
        edit_menu.add(MenuItem("Вставити"))

        self.main_menu.add(file_menu)
        self.main_menu.add(edit_menu)

    def show_menu(self):
        self.main_menu.show()

if __name__ == "__main__":
    menu = MenuSystem()
    menu.show_menu()
