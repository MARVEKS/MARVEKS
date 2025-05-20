
class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class ReportPrinter:
    def print(self, report: Report):
        print(f"Звіт: {report.title}")
        print(report.content)

class Discount:
    def get_discount(self, amount):
        return amount

class StudentDiscount(Discount):
    def get_discount(self, amount):
        return amount * 0.9  # 10% знижка

class SeniorDiscount(Discount):
    def get_discount(self, amount):
        return amount * 0.85  # 15% знижка

if __name__ == "__main__":
    report = Report("Прогрес студента", "Всі завдання здані вчасно.")
    printer = ReportPrinter()
    printer.print(report)

    print("\n--- Знижки ---")
    amount = 100
    discounts = [StudentDiscount(), SeniorDiscount()]
    for d in discounts:
        print(f"Знижена ціна: {d.get_discount(amount)} грн")
