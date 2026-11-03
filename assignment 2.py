# #16
# numbers = [1, 2, 3, 4, 5]

# k = int(input("Enter k: "))

# k = k % len(numbers)

# for i in range(k):
#     last = numbers.pop()
#     numbers.insert(0, last)

# print(numbers)

# 1. 

# year = int(input("Enter a year: "))

# if year % 400 == 0:
#     print("Leap year")
# elif year % 100 == 0:
#     print("Not a leap year")
# elif year % 4 == 0:
#     print("Leap year")
# else:
#     print("Not a leap year")


# # 2.

# day = int(input("Enter day: "))
# month = int(input("Enter month: "))
# year = int(input("Enter year: "))
# if month <1 or month>12:
#     print("Invalid month")
# else:
#     month == 2
#     if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#             days_in_month = 29
#     else:
#         days_in_month = 28
#         if month == 4 or month == 6 or month == 9 or month == 11:
#             days_in_month = 30
#         else:
#             days_in_month = 31

  
# if day > days_in_month :
#         print ("Invalid day")
# elif day < 1:
#         print ("Invalid day")
# elif day<days_in_month:
#         day + 1
            
    
# else:
#      day = 1

# if month < 12:
#         month = month + 1
# elif month == 12:
#          month = 1
#          year = year + 1

# print(day, month, year)


# # 3.

# day = int(input("Enter day: "))
# month = int(input("Enter month: "))
# year = int(input("Enter year: "))

# if month < 1 or month > 12:
#     print("Invalid month")

# elif year < 1:
#     print("Invalid year")

# else:
#     if month == 2:
#         if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#             days_in_month = 29
#         else:
#             days_in_month = 28

#     elif month == 4 or month == 6 or month == 9 or month == 11:
#         days_in_month = 30

#     else:
#         days_in_month = 31

#     if day < 1 or day > days_in_month:
#         print("Invalid day")

#     else:
#         if day > 1:
#             day = day - 1

#         else:
#             if month > 1:
#                 month = month - 1
#             else:
#                 month = 12
#                 year = year - 1

#             if month == 2:
#                 if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#                     day = 29
#                 else:
#                     day = 28

#             elif month == 4 or month == 6 or month == 9 or month == 11:
#                 day = 30

#             else:
#                 day = 31

#         print(day, month, year)


# # 4.

# hour = int(input("Enter hour: "))
# minute = int(input("Enter minute: "))
# second = int(input("Enter second: "))

# if (hour >= 0 and hour <= 23 and
#     minute >= 0 and minute <= 59 and
#     second >= 0 and second <= 59):
#     print("Valid")
# else:
#     print("Invalid")


# # 5. 

# hour = int(input("Enter hour: "))
# minute = int(input("Enter minute: "))
# second = int(input("Enter second: "))


# if second == 60:
#     second = 0
#     minute = minute + 1

# if minute == 60:
#     minute = 0
#     hour = hour + 1

# if hour == 24:
#     hour = 0

# print(hour, minute, second)


# # 6. 

# def count_occurrences(values, target):

#     count = 0

#     for value in values:
#         if value == target:
#             count = count + 1

#     return count


# values = [2, 5, 2, 7, 2, 9, 5]

# print(count_occurrences(values, 2))
# print(count_occurrences(values, 5))
# print(count_occurrences(values, 10))


# 7.

# def find_first(values, target):

#     for i in range(len(values)):
#         if values[i] == target:
#             return i

#     return -1


# values = [10, 20, 30, 20, 40]

# print(find_first(values, 20))
# print(find_first(values, 40))


# # 8. 

# def find_largest(values):

#     if len(values) == 0:
#         return None

#     largest = values[0]

#     for value in values:
#         if value > largest:
#             largest = value
#     return largest
        


# numbers = [10, 45, 23, 89, 12]

# print(find_largest(numbers))




# # 9. 

# def find_smallest(values):

#     if len(values) == 0:
#         return None

#     smallest = values[0]

#     for value in values:
#         if value < smallest:
#             smallest = value

#     return smallest


# numbers = [10, 45, 23, 89, 12]

# print(find_smallest(numbers))




# # 10.

# def count_categories(values):

#     positive = 0
#     negative = 0
#     zero = 0

#     for value in values:

#         if value > 0:
#             positive = positive + 1
#         elif value < 0:
#             negative = negative + 1
#         else:
#             zero = zero + 1

#     return positive, negative, zero


# numbers = [5, -2, 0, 8, -7, 0, 3]

# positive, negative, zero = count_categories(numbers)

# print("Positive:", positive)
# print("Negative:", negative)
# print("Zeros:", zero)


# 11. 

# smallest = None

# while True:

#     number = int(input("Enter a number (0 to stop): "))

#     if number == 0:
#         break

#     if smallest is None:
#         smallest = number
#     elif number < smallest:
#         smallest = number

#     print("Smallest so far:", smallest)


# # 12.

# correct_password = "python123"

# for attempt in range(3):

#     password = input("Enter password: ")

#     if password == correct_password:
#         print("Access granted")
#         break
#     else:
#         attempt_left = 2-attempt
#         print ("Wrong password")
#         print ("Attempts left: ", attempt_left)



# # 13.

# while True:

#     password = input("Enter a password: ")

#     has_digit = False
#     has_uppercase = False

#     for character in password:

#         if character.isdigit():
#             has_digit = True

#         if character.isupper():
#             has_uppercase = True

#     valid = True

#     if len(password) < 8:
#         print("Password must have at least 8 characters")
#         valid = False

#     if has_digit == False:
#         print("Password must contain at least one digit")
#         valid = False

#     if has_uppercase == False:
#         print("Password must contain at least one uppercase letter")
#         valid = False

#     if valid:
#         print("Password accepted")
#         break


# # 14. 

# correct_username = "admin"
# correct_password = "python123"

# for attempt in range(3):

#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     if username.lower() == correct_username and password.lower() == correct_password:
#         print("Login successful")
#         break
#     else:
#         print("Login failed")

#         if attempt == 2:
#             print("Account locked")
#         else:
#             print("Attempts remaining:", 2 - attempt)


# # 15. 

# while True:

#     command = input("Enter command: ")

#     if command == "start":
#         print("System started")
#     elif command == "stop":
#         print("System stopped")
#     elif command == "pause":
#         print("System paused")
#     elif command == "status":
#         print("System status checked")
#     elif command == "exit":
#         print("Exiting......")
#         break
#     else:
#         print("Unknown command")


# # 16. 

# scores = [45, 82, 37, 91, 56, 28, 74]

# passed = []
# failed = []
# distinction = []

# for score in scores:

#     if score < 40:
#         failed.append(score)
#     elif score <= 69:
#         passed.append(score)
#     else:
#         distinction.append(score)

# print("Passed:", passed)
# print("Failed:", failed)
# print("Distinction:", distinction)


# # 17. 

# students = [
#     ("Aisha", 75, 38),
#     ("David", 91, 88),
#     ("John", 55, 38),
#     ("Mary", 81, 65)
# ]

# for student in students:

#     name = student[0]
#     attendance = student[1]
#     score = student[2]

#     if attendance < 75 or score < 40:
#         print(name)


# # 18. 

# prices = [5000, 12000, 7500, 20000, 3000]

# new_prices = []

# for price in prices:

#     if price < 5000:
#         discount = 0
#     elif price < 10000:
#         discount = 0.05
#     elif price < 20000:
#         discount = 0.10
#     else:
#         discount = 0.15

#     new_price = price - (price * discount)

#     new_prices.append(new_price)

# print("Original prices:", prices)
# print("New prices:", new_prices)


# # 19.
# usernames = [
#     " Mahmudah ",
#     "ADEYEMI",
#     " john",
#     "Sarah "
# ]

# new_usernames = []

# for username in usernames:

#     username = username.strip()
#     username = username.lower()

#     new_usernames.append(username)

# print(new_usernames)

# for username in new_usernames:

#     if len(username) >= 5:
#         print(username, "- At least 5 characters")
#     else:
#         print(username, "- Less than 5 characters")


# # 20.

# products = [
#     ("Laptop", 450000),
#     ("Phone", 250000),
#     ("Tablet", 180000),
#     ("Monitor", 150000)
# ]

# search_name = input("Enter product name: ")

# found = False

# for product in products:

#     name = product[0]
#     price = product[1]

#     if name.lower() == search_name.lower():

#         print("Product:", name)
#         print("Price:", price)

#         found = True
#         break

# if found == False:
#     print("Product not found")
