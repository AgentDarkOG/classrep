# 1. 
class Student:
    def __init__(self, name):
        self.name = name
        self.subjects = {}

    def add_subject(self, name, score):
        if score < 0 or score > 100:
            print("Invalid score")
        else:
            self.subjects[name] = score

    def remove_subject(self, name):
        if name in self.subjects:
            del self.subjects[name]
        else:
            print("Subject does not exist")

    def get_score(self, name):
        if name in self.subjects:
            return self.subjects[name]
        else:
            print("Subject does not exist")

    def average(self):
        if len(self.subjects) == 0:
            return 0
        return sum(self.subjects.values()) / len(self.subjects)


student = Student("John")
student.add_subject("Mathematics", 75)
student.add_subject("English", 82)
student.add_subject("Computer Science", 91)

print(student.get_score("Mathematics"))
print(student.average())


# 2. 
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append("Deposited " + str(amount))
        else:
            print("Invalid deposit")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append("Withdrew " + str(amount))
        else:
            print("Withdrawal failed")

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions


account = BankAccount("John", 1000)
account.deposit(500)
account.withdraw(200)

print(account.get_balance())
print(account.get_transactions())


# 3.

class Order:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items
        self.status = "pending"

    def confirm(self):
        if self.status == "pending":
            self.status = "confirmed"
        else:
            print("Invalid status change")

    def ship(self):
        if self.status == "confirmed":
            self.status = "shipped"
        else:
            print("Invalid status change")

    def deliver(self):
        if self.status == "shipped":
            self.status = "delivered"
        else:
            print("Invalid status change")

    def cancel(self):
        if self.status in ["pending", "confirmed"]:
            self.status = "cancelled"
        else:
            print("Cannot cancel this order")


order = Order("John", ["Laptop", "Mouse"])
order.confirm()
order.ship()
order.deliver()

print(order.status)


# 4. 

class Exam:
    def __init__(self, subject, passing_score):
        self.subject = subject
        self.questions = []
        self.passing_score = passing_score

    def add_question(self, question, correct_answer):
        self.questions.append({
            "question": question,
            "answer": correct_answer
        })

    def calculate_score(self, answers):
        score = 0

        for i in range(len(self.questions)):
            if answers[i] == self.questions[i]["answer"]:
                score += 1

        return score

    def is_passed(self, score):
        return score >= self.passing_score


exam = Exam("Computer Science", 2)

exam.add_question("2 + 2?", "4")
exam.add_question("Capital of Nigeria?", "Abuja")
exam.add_question("Python is a programming language?", "Yes")

answers = ["4", "Abuja", "Yes"]

score = exam.calculate_score(answers)

print("Score:", score)
print("Passed:", exam.is_passed(score))


# 5.

class BankAccount2:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def has_more_money_than(self, other_account):
        return self.balance > other_account.balance

    def transfer_to(self, other_account, amount):
        if amount <= 0:
            print("Invalid amount")
            return

        if amount > self.balance:
            print("Insufficient funds")
            return

        self.balance -= amount
        other_account.balance += amount


account1 = BankAccount2("John", 1000)
account2 = BankAccount2("Mike", 500)

print(account1.has_more_money_than(account2))

account1.transfer_to(account2, 300)

print(account1.balance)
print(account2.balance)


# 6.

class Wallet:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Balance cannot be negative")

    def add_money(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Invalid amount")

    def remove_money(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
        else:
            print("Cannot remove this amount")


wallet = Wallet("John", 500)
wallet.add_money(200)
wallet.remove_money(100)

print(wallet.balance)


# 7. 

class Student2:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name


student = Student2("John", "Smith")

print(student.full_name)

student.first_name = "Mike"

print(student.full_name)





# 9. 

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            print("Temperature cannot be below absolute zero")
        else:
            self._celsius = value

    @property
    def fahrenheit(self):
        return (self.celsius * 9 / 5) + 32


temperature = Temperature(25)

print(temperature.celsius)
print(temperature.fahrenheit)

temperature.celsius = 30

print(temperature.fahrenheit)


# 10.

class SecureBankAccount:
    def __init__(self, owner, balance, pin):
        self.owner = owner
        self._balance = balance
        self._pin = pin

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Invalid deposit")

    def withdraw(self, amount, pin):
        if pin != self._pin:
            print("Incorrect PIN")
        elif amount <= 0:
            print("Amount must be positive")
        elif amount > self._balance:
            print("Insufficient funds")
        else:
            self._balance -= amount


secure_account = SecureBankAccount("John", 1000, 1234)

secure_account.deposit(500)
secure_account.withdraw(200, 1234)

print(secure_account.balance)


# 11. 

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
        else:
            print("Product not found")

    def find_product(self, name):
        for product in self.products:
            if product.name == name:
                return product

        return None

    @property
    def total_value(self):
        total = 0

        for product in self.products:
            total += product.total_value

        return total


inventory = Inventory()

product1 = Product1("Laptop", 500000, 2)
product2 = Product1("Mouse", 10000, 5)

inventory.add_product(product1)
inventory.add_product(product2)


print(inventory.total_value)
print(inventory.find_product("Laptop").name)




# 13. 

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            print("Age cannot be negative")

    @property
    def can_register(self):
        return self.age >= 18


user1 = User("John", 20)
user2 = User("Mike", 15)

print(user1.can_register)
print(user2.can_register)


# 14. Student Attendance

class StudentAttendance:
    def __init__(self, name, attendance):
        self.name = name
        self.attendance = attendance

    @property
    def attendance(self):
        return self._attendance

    @attendance.setter
    def attendance(self, value):
        if 0 <= value <= 100:
            self._attendance = value
        else:
            print("Attendance must be between 0 and 100")

    @property
    def eligible_for_exam(self):
        return self.attendance >= 75


student1 = StudentAttendance("John", 80)
student2 = StudentAttendance("Mike", 60)

print(student1.eligible_for_exam)
print(student2.eligible_for_exam)


