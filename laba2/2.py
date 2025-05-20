from abc import ABC, abstractmethod

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class UserRepository:
    def __init__(self):
        self._users = []

    def add_user(self, user):
        self._users.append(user)

    def get_all_users(self):
        return self._users

class UserPrinter:
    def print_users(self, users):
        for user in users:
            print(f"Username: {user.username}, Email: {user.email}")

class NotificationSender(ABC):
    @abstractmethod
    def send(self, user, message):
        pass

class EmailSender(NotificationSender):
    def send(self, user, message):
        print(f"Повідомлення відправлено на {user.email}: {message}")

class SMSSender(NotificationSender):
    def send(self, user, message):
        print(f"СМС відправлено на {user.username}: {message}")

def main():
    user1 = User("Іван_Мартиник", "Ivan@gmail.com")
    user2 = User("Іван_Франко", "Franko@gmail.com")
    repo = UserRepository()
    repo.add_user(user1)
    repo.add_user(user2)

    printer = UserPrinter()
    print("All users:")
    printer.print_users(repo.get_all_users())

    print("\nSending notifications:")
    email_sender = EmailSender()
    sms_sender = SMSSender()

    for user in repo.get_all_users():
        email_sender.send(user, "Привітання!")
        sms_sender.send(user, "Повідомлення про виселення!")

if __name__ == "__main__":
    main()
