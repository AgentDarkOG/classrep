# 2.
# class Vehicle:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year
# class Car(Vehicle):
#     def __init__(self, brand, year, number_of_doors):
#         super().__init__(brand, year)
#         self.number_of_doors = number_of_doors
# car = Car("Lambo", "2025", "2")
# print("Car Brand:",car.brand)
# print("Car Year:",car.year)
# print("Number of Car Doors:",car.number_of_doors)

#3
# class Animal:
#     def make_sound(self):
#         print("Animal sound")
# class Dog(Animal):
#     def make_sound(self):
#         print("Woof!")
# class Cat(Animal):
#     def make_sound(self):
#         print("Meow!")
# dog = Dog()
# cat = Cat()
# dog.make_sound()
# cat.make_sound()

#4
# class Animal:
#     def make_sound(self):
#         pass
# class Dog(Animal):
#     def make_sound(self):
#         print("Dog Woofs!")
# class Cat(Animal):
#     def make_sound(self):
#         print("Cat Meows!")
# class Bird(Animal):
#     def make_sound(self):
#         print("Bird Tweets")
# animals = [Dog(), Cat(), Bird()]
# for animal in animals:
    # animal.make_sound()

#5
# class Shape:
#     def calculate_area(self):
#         pass
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def calculate_area(self):
#         return 3.14 * self.radius * self.radius
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def calculate_area(self):
#         return self.length * self.width
# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#     def calculate_area(self):
#         return 0.5 * self.base * self.height
# shapes = [
#     Circle(5),
#     Rectangle(10, 4),
#     Triangle(6, 8)
# ]
# for shape in shapes:
#     print(shape.calculate_area())

#6
# class Student:
#     def __init__(self,name,student_id):
#         self.name = name
#         self.student_id = student_id
#         self.courses = []
#     def add_course(self, course):
#         if course not in self.courses:
#             self.courses.append(course)
#     def remove_course(self, course):
#         if course in self.courses:
#             self.courses.remove(course)
#     def display_courses(self):
#         print(self.courses)
# student = Student("Nathaniel", "ST001")
# student.add_course("Python")
# student.add_course("Maths")
# student.add_course("Python")
# student.display_courses()
# student.remove_course("Python")
# student.display_courses()

#7
# class Product:
#     def __init__(self, name, price, stock):
#         self.name = name
#         self.price = price
#         self.stock = stock
# class Cart:
#     def __init__(self):
#         self.products = []
#     def add_product(self, product):
#         if product.stock > 0:
#             self.products.append(product)
#         else:
#             print("Product is out of stock")
#     def remove_product(self, product):
#         if product in self.products:
#             self.products.remove(product)
#     def calculate_total(self):
#         total = 0
#         for product in self.products:
#             total += product.price
#         return total
# product1 = Product("Laptop", 250000, 2)
# product2 = Product("Mouse", 7000, 3)
# cart = Cart()
# cart.add_product(product1)
# cart.add_product(product2)
# print(cart.calculate_total())

#8
# class Product:
#     def __init__(self, name, price, stock):
#         self.name = name
#         self.price = price
#         self.stock = stock
# class PhysicalProduct(Product):
#     def __init__(self, name, price, stock, weight):
#         super().__init__(name, price, stock)
#         self.weight = weight
#     def calculate_shipping(self):
#         return self.weight * 100
# class DigitalProduct(Product):
#     def __init__(self, name, price, stock, file_size):
#         super().__init__(name, price, stock)
#         self.file_size = file_size

#     def calculate_shipping(self):
#         return 0
# products = [
#     PhysicalProduct("Laptop", 500000, 75, 3),
#     DigitalProduct("Python Course", 750000, 500, 5800)
# ]
# for product in products:
#     print(product.calculate_shipping())

#9
# class Transport:
#     def __init__(self, company, capacity):
#         self.company = company
#         self.capacity = capacity
# class Bus(Transport):
#     def calculate_fare(self, distance):
#         return distance * 50
# class Train(Transport):
#     def calculate_fare(self, distance):
#         return distance * 70
# class Plane(Transport):
#     def calculate_fare(self, distance):
#         return distance * 200
# transports = [
#     Bus("ABC Bus", 50),
#     Train("NRC", 300),
#     Flight("Air Nigeria", 180)
# ]
# distance = 100
# for transport in transports:
#     print(transport.calculate_fare(distance))

#10
# class Staff:
#     def __init__(self, name, staff_id, salary):
#         self.name = name
#         self.staff_id = staff_id
#         self.salary = salary
# class Lecturer(Staff):
#     def __init__(self, name, staff_id, salary, department):
#         super().__init__(name, staff_id, salary)
#         self.department = department
#     def calculate_monthly_pay(self):
#         return self.salary + 50000
# class Administrator(Staff):
#     def __init__(self, name, staff_id, salary, office):
#         super().__init__(name, staff_id, salary)
#         self.office = office
#     def calculate_monthly_pay(self):
#         return self.salary + 30000
# class Technician(Staff):
#     def __init__(self, name, staff_id, salary, skill):
#         super().__init__(name, staff_id, salary)
#         self.skill = skill
#     def calculate_monthly_pay(self):
#         return self.salary + 20000
# staff = [
#     Lecturer("John", "L001", 300000, "Computer Science"),
#     Administrator("Mary", "A001", 200000, "Registry"),
#     Technician("Peter", "T001", 180000, "Networking")
# ]
# for person in staff:
#     print(person.calculate_monthly_pay())

