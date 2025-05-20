import copy

class Student:
    def __init__(self, name, group, grades):
        self.name = name
        self.group = group
        self.grades = grades

    def study(self):
        print(f"{self.name} з групи {self.group} вчиться.")

    def show_grades(self):
        print(f"Оцінки {self.name}: {self.grades}")

    def clone(self):
        return copy.deepcopy(self)

# Головна частина програми
if __name__ == "__main__":
    original_student = Student("Іван", "КН-21", [3, 4, 4])
    original_student.study()
    original_student.show_grades()

    # Клонування студента
    cloned_student = original_student.clone()
    cloned_student.name = "Олег"
    cloned_student.group = "КН-22"
    cloned_student.grades[0] = 5

    print("\nПісля клонування:")
    original_student.show_grades()
    cloned_student.show_grades()
