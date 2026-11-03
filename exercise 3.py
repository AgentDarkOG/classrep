#1
# password = input("Enter password: ")

# if len(password) < 8:
#     print("Too short")

# else:
#     upper = False
#     lower = False
#     digit = False

#     for character in password:

#         if character.isupper():
#             upper = True

#         if character.islower():
#             lower = True

#         if character.isdigit():
#             digit = True

#     if upper and lower and digit:
#         print("Stronger")

#     elif upper and lower or digit:
#         print("Stronger")

#     else:
#         print("Weak")

#2
# usersname = "admin"
# passwords = "python123"
# username = input("Enter your username: ")
# password = input("Enter your password: ")
# if username == usersname and password == passwords:
#     print ("Login Successful")
# elif username != usersname:
#     print("Incorrect username")
# else:
#     print ("Incorrect password")


# 3
# balance = float(input("Enter balance: "))
# withdrawal = float(input("Enter withdrawal amount: "))

# if withdrawal <= 0:
#     print("Invalid amount")

# elif withdrawal > balance:
#     print("Insufficient balance")

# elif withdrawal % 500 != 0:
#     print("Withdrawal must be a multiple of 500")

# else:
#     balance = balance - withdrawal
#     print("Remaining balance:", balance)


# # 4
# units = int(input("Enter units consumed: "))

# if units <= 50:
#     bill = units * 10

# elif units <= 150:
#     bill = (50 * 10) + ((units - 50) * 15)

# elif units <= 250:
#     bill = (50 * 10) + (100 * 15) + ((units - 150) * 20)

# else:
#     bill = (50 * 10) + (100 * 15) + (100 * 20) + ((units - 250) * 25)

# print("Electricity bill:", bill)


# # 5
# years = float(input("Enter years of service: "))
# salary = float(input("Enter salary: "))
# rating = float(input("Enter performance rating: "))

# if years < 1:
#     bonus = 0

# elif years <= 3:

#     if rating >= 4:
#         bonus = salary * 0.10

#     else:
#         bonus = salary * 0.05

# else:

#     if rating >= 4:
#         bonus = salary * 0.15

#     elif rating >= 3:
#         bonus = salary * 0.10

#     else:
#         bonus = salary * 0.05

# print("Bonus:", bonus)


# # 6
# state = "stopped"

# while True:

#     command = input("Enter command: ").lower()

#     if command == "exit":
#         break

#     elif command == "start":

#         if state == "stopped":
#             state = "running"

#         else:
#             print("Invalid command")

#     elif command == "pause":

#         if state == "running":
#             state = "paused"

#         else:
#             print("Invalid command")

#     elif command == "stop":

#         if state == "running" or state == "paused":
#             state = "stopped"

#         else:
#             print("Invalid command")

#     elif command == "status":
#         print("Current state:", state)

#     else:
#         print("Invalid command")
    
# # 7
# balance = 100000

# while True:

#     command = input("Enter command: ").lower()

#     if command == "exit":
#         break

#     elif command == "balance":
#         print("Balance:", balance)

#     elif command == "deposit":

#         amount = float(input("Enter amount: "))

#         if amount > 0:
#             balance = balance + amount

#         else:
#             print("Invalid amount")

#     elif command == "withdraw":

#         amount = float(input("Enter amount: "))

#         if amount <= 0:
#             print("Invalid amount")

#         elif amount > balance:
#             print("Insufficient balance")

#         else:
#             balance = balance - amount

#     else:
#         print("Invalid command")


# # 8
# balance = 100000
# transactions = 0

# while transactions < 5:

#     command = input("Enter command: ").lower()

#     if command == "exit":
#         break

#     elif command == "balance":
#         print("Balance:", balance)

#     elif command == "deposit":

#         amount = float(input("Enter amount: "))

#         if amount > 0:
#             balance = balance + amount
#             transactions = transactions + 1

#         else:
#             print("Invalid amount")

#     elif command == "withdraw":

#         amount = float(input("Enter amount: "))

#         if amount <= 0:
#             print("Invalid amount")

#         elif amount > balance:
#             print("Insufficient balance")

#         else:
#             balance = balance - amount
#             transactions = transactions + 1

#     else:
#         print("Invalid command")

# print("Session ended")


# # 9
# readings = 0
# low = 0
# normal = 0
# high = 0

# while True:

#     usage = float(input("Enter electricity usage: "))

#     if usage == -1:
#         break

#     readings = readings + 1

#     if usage < 100:
#         print("Low usage")
#         low = low + 1

#     elif usage <= 300:
#         print("Normal usage")
#         normal = normal + 1

#     else:
#         print("High usage")
#         high = high + 1

# print("Number of readings:", readings)
# print("Low readings:", low)
# print("Normal readings:", normal)
# print("High readings:", high)


# # 10
# highest = None

# while True:

#     temperature = float(input("Enter temperature: "))

#     if temperature == 999:
#         break

#     if highest is None or temperature > highest:
#         highest = temperature

#     if temperature < 18:
#         print("Cold")

#     elif temperature <= 30:
#         print("Normal")

#     else:
#         print("Hot")

# print("Highest temperature:", highest)


# # 11
# products = [
#     ["Laptop", 450000],
#     ["Phone", 250000],
#     ["Tablet", 180000],
#     ["Headphones", 80000]
# ]

# most_expensive = products[0]

# for product in products:

#     if product[1] > most_expensive[1]:
#         most_expensive = product

# print ("Product", product)
# print ("Price", price)


# # 12
# products = [
#     ["Laptop", 450000],
#     ["Phone", 250000],
#     ["Tablet", 180000],
#     ["Headphones", 80000]
# ]

# budget = float(input("Enter maximum budget: "))

# for product in products:

#     if product[1] <= budget:
#         print(product[0], product[1])
 

# # 13
# values = [1, 2, 3, 4, 5]

# reversed_list = []

# for i in range(len(values) - 1, -1, -1):
#     reversed_list.append(values[i])

# print(reversed_list)


# # 14
# values = [1, 2, 3, 2, 1]

# palindrome = True

# for i in range(len(values) // 2):

#     if values[i] != values[len(values) - 1 - i]:
#         palindrome = False

# if palindrome:
#     print("Palindrome")

# else:
#     print("Not palindrome")


# # 15
# values = [5, 8, 2, 8, 3]

# largest = None
# second_largest = None

# for value in values:

#     if largest is None or value > largest:

#         if value != largest:
#             second_largest = largest

#         largest = value

#     elif value != largest:

#         if second_largest is None or value > second_largest:
#             second_largest = value

# if second_largest is None:
#     print("No second distinct value")

# else:
#     print("Second largest:", second_largest)


# # 16
# def calculate_sum(values):

#     total = 0

#     for value in values:
#         total = total + value

#     return total


# def calculate_average(values):

#     total = calculate_sum(values)

#     return total / len(values)


# def find_largest(values):

#     largest = values[0]

#     for value in values:

#         if value > largest:
#             largest = value

#     return largest


# def find_smallest(values):

#     smallest = values[0]

#     for value in values:

#         if value < smallest:
#             smallest = value

#     return smallest


# values = [10, 20, 30, 40, 50]

# print("Sum:", calculate_sum(values))
# print("Average:", calculate_average(values))
# print("Largest:", find_largest(values))
# print("Smallest:", find_smallest(values))


# # 17
# def longest_sequence(values):

#     if len(values) == 0:
#         return None

#     best_value = values[0]
#     best_length = 1
#     best_start = 0

#     current_length = 1

#     for i in range(1, len(values)):

#         if values[i] == values[i - 1]:
#             current_length = current_length + 1

#         else:
#             current_length = 1

#         if current_length > best_length:
#             best_length = current_length
#             best_value = values[i]
#             best_start = i - current_length + 1

#     return best_value, best_length, best_start


# values = [2, 2, 5, 5, 5, 3]

# print(longest_sequence(values))


# # 18
# def is_increasing(values):

#     for i in range(1, len(values)):

#         if values[i] <= values[i - 1]:
#             return False

#     return True


# values = [1, 3, 5, 9]

# print(is_increasing(values))


# # 19
# def remove_duplicates(values):

#     new_list = []

#     for value in values:

#         if value not in new_list:
#             new_list.append(value)

#     return new_list


# values = [1, 2, 2, 3, 1, 4, 3]

# print(remove_duplicates(values))


# 20
# def rotate(values, k):

#     if len(values) == 0:
#         return []

#     k = k % len(values)

#     new_list = []

#     for i in range(len(values) - k, len(values)):
#         new_list.append(values[i])

#     for i in range(0, len(values) - k):
#         new_list.append(values[i])

#     return new_list


# values = [1, 2, 3, 4, 5]

# print(rotate(values, 2))

