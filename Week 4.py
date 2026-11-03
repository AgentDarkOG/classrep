#1
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#     def total_value(self):
#         return self.price * self.quantity

# product1 = Product("Pen",200, 2)
# product2 = Product("Book", 1000, 12)
# product3 = Product ("Pencil", 150, 2)

# print(product1.total_value())
# print(product2.total_value())
# print(product3.total_value())

#2
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def total_value(self):
#              return self.price * self.quantity
   
#     def apply_discount(self, percent):
#         if percent > 0 and percent < 100:
#             self.price = self.price - (self.price * percent/100)


# product1 = Product("Pen",200, 2)
# product2 = Product("Book", 1000, 12)
# product3 = Product ("Pencil", 150, 2)

# product1.apply_discount(10)
# product2.apply_discount(40)
# product3.apply_discount(15)

# print(product1.total_value())
# print(product2.total_value())
# print(product3.total_value())

# 3. 
# class Temperature:
#     def __init__(self, celsius):
#         self.celsius = celsius

#     def to_fahrenheit(self):
#         return (self.celsius * 9 / 5) + 32

#     def is_freezing(self):
#         return self.celsius <= 0

#     def is_hot(self):
#         return self.celsius > 30


# temperature1 = Temperature(35)

# print(temperature1.to_fahrenheit())
# print(temperature1.is_freezing())
# print(temperature1.is_hot())


# 4. 
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def is_adult(self):
#         return self.age >= 18

#     def birthday(self):
#         self.age = self.age + 1


# person1 = Person("John", 17)

# print(person1.is_adult())

# person1.birthday()

# print(person1.age)
# print(person1.is_adult())


 # 5. 
# class Student:
#     def __init__(self, name, scores):
#         self.name = name
#         self.scores = scores

#     def average(self):
#         return sum(self.scores) / len(self.scores)

#     def result(self):
#         for score in self.scores:
#             if score < 40:
#                 return "Fail"

#         if self.average() < 70:
#             return "Pass"
#         else:
#             return "Distinction"

# student1 = Student("John", [70, 75, 80, 65])

# print(student1.average())
# print(student1.result())



# 7. 
# class InventoryItem:
#     def __init__(self, name, quantity):
#         self.name = name
#         self.quantity = quantity

#     def add_stock(self, amount):
#         if amount > 0:
#             self.quantity = self.quantity + amount

#     def remove_stock(self, amount):
#         if amount > 0 and amount <= self.quantity:
#             self.quantity = self.quantity - amount

#     def is_available(self):
#         return self.quantity >= 1


# item1 = InventoryItem("Shoes", 10)

# item1.add_stock(5)
# print(item1.quantity)

# item1.remove_stock(3)
# print(item1.quantity)

# print(item1.is_available())


# 8. 
# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance = self.balance + amount

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance = self.balance - amount
#         else:
#             print("Insufficient balance")

#     def show_balance(self):
#         print("Balance:", self.balance)


# account = BankAccount(10000)

# while True:
#     command = input("Enter command (deposit, withdraw, balance, exit): ")

#     if command == "deposit":
#         amount = float(input("Enter amount: "))
#         account.deposit(amount)

#     elif command == "withdraw":
#         amount = float(input("Enter amount: "))
#         account.withdraw(amount)

#     elif command == "balance":
#         account.show_balance()

#     elif command == "exit":
#         break

#     else:
#         print("Invalid command")


# 9. 
# class CartItem:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def total(self):
#         return self.price * self.quantity
# total = 0

# while True:
#     name = input("Enter product name or done: ")

#     if name == "done":
#         break

#     price = float(input("Enter price: "))
#     quantity = int(input("Enter quantity: "))
#     item = CartItem(name, price, quantity)

#     total = total + item.total()
# print("Final total:", total)

# 6. User Account

# class User:
#     def __init__(self, username, password, is_active):
#         self.username = username
#         self.password = password
#         self.is_active = is_active

#     def login(self, password):
#         if password == self.password:
#             self.is_active = True
#             return "Login Successful"
#         return "Invalid password"
#     def logout(self):
#         self.is_active = False
#         print("Logged out")


# user1 = User("John", "1234", True)
# user2 = User("Peter", "5678", True)

# user1.login("1234")
# print(user1.is_active)

# user1.logout()
# print(user1.is_active)

# user2.login("wrong")
# print(user2.is_active)


# 10. 

class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

def add_score(self, score):
    if score >= 0 and score <= 100:
        self.scores.append(score)
    else:
        print("Invalid score"def average(self):

        return sum(self.scores) / len(self.scores)


    def highest_score(self):

        return max(self.scores)


    def lowest_score(self):

     return min(self.scores)



student1 = Student("John")


student1.add_score(80)

student1.add_score(65)

student1.add_score(90)

student1.add_score(75)

student1.add_score(70)


print("Average:", student1.average())

print("Highest:", student1.highest_score())

print("Lowest:", student1.lowest_score())