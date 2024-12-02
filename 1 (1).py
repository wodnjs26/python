class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print("title : ", self.title)
        print("author : ", self.author)
        print("price : ", self.price)

    def __eq__(self, other):
        if isinstance(other, Book):
            if self.price == other.price:
                return True
            else:
                return False


# ------------------------------------------------------------------
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("특정금액이 없어서 입금을 못함.")

    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= amount
        else:
            print("출금할 수 없음")

    def display_balance(self):
        print("Balance : ", self.balance)


# ----------------------------------------------------------------
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print("Name : ", self.name)
        print("Salary : ", self.salary)


class Manager:
    def __init__(self):  # 추가할꺼면 self 뒤에 안 붙여도 된다. (아마도)
        self.team_members = []

    def add_team_member(self, team_member):
        self.team_members.append(team_member)

    def display_team(self):
        print("Team Members : ", self.team_members)
