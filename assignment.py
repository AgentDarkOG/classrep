# # 1.
# a = int(input("Enter first side: "))
# b = int(input("Enter second side: "))
# c = int(input("Enter third side: "))

# if a + b > c and a + c > b and b + c > a:

#     if a == b and b == c:
#         print("Equilateral")

#     elif a == b or a == c or b == c:
#         print("Isosceles")

#     else:
#         print("Scalene")

# else:
#     print("Invalid triangle")

#2
# a = int(input("Enter first angle: "))
# b = int(input("Enter second angle: "))
# c = int(input("Enter third angle: "))

# if a > 0 and b > 0 and c > 0 and a + b + c == 180:

#     if a == 90 or b == 90 or c == 90:
#         print("Right")

#     elif a > 90 or b > 90 or c > 90:
#         print("Obtuse")

#     else:
#         print("Acute")

# else:
#     print("Invalid triangle")

# #3
# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))
# c = int(input("Enter number 3: "))
# d = int(input("Enter number 4: "))
# e = int(input("Enter number 5: "))

# greatest = a

# if b > greatest:
#     greatest = b

# if c > greatest:
#     greatest = c

# if d > greatest:
#     greatest = d

# if e > greatest:
#     greatest = e

# print("Greatest:", greatest)

# #4
# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))
# c = int(input("Enter number 3: "))
# d = int(input("Enter number 4: "))

# if a > b:
#     largest = a
#     second = b
# else:
#     largest = b
#     second = a

# if c > largest:
#     second = largest
#     largest = c
# elif c > second:
#     second = c

# if d > largest:
#     second = largest
#     largest = d
# elif d > second:
#     second = d

# print("Second largest:", second)

# #5
# day = int(input("Enter day: "))
# month = int(input("Enter month: "))
# year = int(input("Enter year: "))

# valid = False

# if month >= 1 and month <= 12:

#     if month == 2:

#         if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#             if day >= 1 and day <= 29:
#                 valid = True
#         else:
#             if day >= 1 and day <= 28:
#                 valid = True

#     elif month == 4 or month == 6 or month == 9 or month == 11:

#         if day >= 1 and day <= 30:
#             valid = True

#     else:

#         if day >= 1 and day <= 31:
#             valid = True

# if valid:
#     print("Valid")
# else:
#     print("Invalid")

##6
# n = int(input("How many numbers? "))

# positive = 0
# negative = 0
# zero = 0

# for i in range(n):

#     number = int(input("Enter number: "))

#     if number > 0:
#         positive += 1

#     elif number < 0:
#         negative += 1

#     else:
#         zero += 1

# print("Positive:", positive)
# print("Negative:", negative)
# print("Zero:", zero)

##7
# n = int(input("How many numbers? "))

# even_count = 0
# odd_count = 0

# even_sum = 0
# odd_sum = 0

# for i in range(n):

#     number = int(input("Enter number: "))

#     if number % 2 == 0:
#         even_count += 1
#         even_sum += number

#     else:
#         odd_count += 1
#         odd_sum += number

# print("Even count:", even_count)
# print("Odd count:", odd_count)
# print("Even sum:", even_sum)
# print("Odd sum:", odd_sum)

##8
# n = int(input("How many numbers? "))

# number = int(input("Enter number: "))

# largest = number
# smallest = number

# for i in range(n - 1):

#     number = int(input("Enter number: "))

#     if number > largest:
#         largest = number

#     if number < smallest:
#         smallest = number

# print("Largest:", largest)
# print("Smallest:", smallest)

##9
# n = int(input("How many numbers? "))

# numbers = []

# for i in range(n):
#     number = int(input("Enter number: "))
#     numbers.append(number)

# if n < 2:
#     print("There is no second largest value")
# else:
#     largest = numbers[0]
#     second = None

#     for number in numbers:

#         if number > largest:
#             second = largest
#             largest = number

#         elif number < largest:
#             if second is None or number > second:
#                 second = number

#     if second is None:
#         print("There is no second largest value")
#     else:
#         print("Second largest:", second)


##10
# largest = None

# while True:

#     number = int(input("Enter number: "))

#     if number == 0:
#         break

#     if largest is None or number > largest:
#         largest = number

#     print(largest)

##11
# def can_access(role, resource):

#     if role == "admin":
#         return True

#     elif role == "editor":
#         if resource == "posts":
#             return True

#     elif role == "viewer":
#         if resource == "posts":
#             return True

#     return False


# role = input("Enter role: ")
# resource = input("Enter resource: ")

# result = can_access(role, resource)

# print(result)

##12
# def is_valid_password(password):

#     if len(password)>8:
#         return False
    
#     has_uppercase = False
#     has_digit = False

#     for character in password:
#         if character.isupper:
#             has_uppercase = True
#         if password.hasdigit:
#             has_digit = True
#         if has_uppercase and has_digit:
#             return True
#         return False
    
# while True:
#     password=(input("Enter your Password: "))

#     if is_valid_password(password):
#         print ("Valid Password")
#         break

#     else:
#         print("Invalid Password")

        

        
    
##13
# def verify_login(username, password):

#     correct_username = "admin"
#     correct_password = "python123"

#     if username == correct_username and password == correct_password:
#         return True

#     return False


# attempts = 3

# for i in range(attempts):

#     username = input("Username: ")
#     password = input("Password: ")

#     if verify_login(username, password):
#         print("Login successful")
#         break

#     else:
#         print("Incorrect username or password")

# else:
#     print("Too many attempts")

##14
# def classify_result(scores):

#     total = 0

#     for score in scores:

#         if score < 40:
#             return "Fail"

#         total += score

#     average = total / len(scores)

#     if average < 70:
#         return "Pass"

#     else:
#         return "Distinction"


# student1 = [75, 80, 70, 65]
# student2 = [50, 60, 55, 70]
# student3 = [80, 35, 90, 85]

# print("Student 1:", classify_result(student1))
# print("Student 2:", classify_result(student2))
# print("Student 3:", classify_result(student3))

##15
# def validate_transaction(balance, amount, transaction_type):

#     if transaction_type != "deposit" and transaction_type != "withdraw":
#         return "Invalid transaction type"

#     if amount <= 0:
#         return "Invalid amount"

#     if transaction_type == "withdraw":

#         if amount > balance:
#             return "Insufficient balance"

#     return "Valid transaction"


# balance = 10000

# transaction_type = input("Enter transaction type: ")
# amount = float(input("Enter amount: "))

# result = validate_transaction(balance, amount, transaction_type)

# print(result)



##17
# numbers = [0, 5, 0, 3, 8, 0, 2]

# result = []
# zero_count = 0

# for number in numbers:

#     if number == 0:
#         zero_count += 1

#     else:
#         result.append(number)

# for i in range(zero_count):
#     result.append(0)

# print(result)

#18
# numbers = [4, 7, 2, 9, 6, 3, 8]

# even = []
# odd = []

# for number in numbers:

#     if number % 2 == 0:
#         even.append(number)

#     else:
#         odd.append(number)

# print("Even:", even)
# print("Odd:", odd)

##19
# a = [1, 2, 2, 3, 4]
# b = [2, 2, 4, 5, 6]

# both = []
# only_first = []
# only_second = []

# used = []

# for number in a:

#     if number in b and number not in used:
#         both.append(number)
#         used.append(number)

#     elif number not in b:
#         only_first.append(number)

# for number in b:

#     if number not in a:
#         only_second.append(number)

# print("Both:", both)
# print("Only first:", only_first)
# print("Only second:", only_second)

##20
# a = [1, 4, 7, 10]
# b = [2, 3, 8, 9]

# result = []

# i = 0
# j = 0

# while i < len(a) and j < len(b):

#     if a[i] < b[j]:
#         result.append(a[i])
#         i += 1

#     else:
#         result.append(b[j])
#         j += 1


# while i < len(a):
#     result.append(a[i])
#     i += 1


# while j < len(b):
#     result.append(b[j])
#     j += 1

# print(result)


