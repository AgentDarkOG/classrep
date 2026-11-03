import random
# lenght = int(input('enter the lenght: '))
# breath = int(input('enter the breath: '))
# area = lenght ** breath
# print(area)

# a = 7 != 5+2
# print(a)

# if 7 > 6 :
#     print('okay')
# else:
#     print('not okay')

# first_number = int(input('enter first number: '))
# second_number = int(input('enter second number: '))
# if first_number > second_number :
#     print ("you can proceed")
# else :
#     print ("you can't proceed")

# number = int(input('enter number'))
# if number % 2 == 0:
#     print('even')
# else :
#     print ('odd')

# my_account_balance = 2000
# transaction_pin = 1234
# transfer_amount = int(input('enter tranfer amount: '))
# if transfer_amount > my_account_balance :
#     print('Insufficient funds.')
# else :
#     int(input('transaction pin: '))
#     if transaction_pin == 1234 :
#         print('Successful')
# a = 4
# b=15
# c = None
# c= a
# a =b
# b = c
# print(a)
# print(b)

# age = int(input('enter your age:')) 
# if age >= 18:
#     print('you are eligible to vote')
# elif age >= 13:
#     print('you are a teenager')
# else:
#     print('you are a child')

# number = int(input('enter number: '))
# if number > 0:
#     print('positive')
# elif number < 0:
#     print('negative')
# else:
#     print('zero')

# number = int(input('enter number'))
# if number % 2 == 0:
#     print('even')
# else :
#     print ('odd')

# a = 5 
# print(a < 0 or a > 10 or a == 5)  

# temperature = int(input('enter temperature: '))
# if temperature > 30:
#     print('it is hot')
# elif temperature > 20:
#     print('it is warm')
# else:
#     print('it is cold') 

# score = int(input('enter your score: '))
# if score >= 50:
#     print('Passed')
# else:
#     print('Failed')

# first_number = int(input('enter first number: '))
# second_number = int(input('enter second number: '))
# if first_number > second_number:
#   print(first_number)  
# else:
#     print(second_number)

# year = int(input('enter year: '))
# if year % 4 == 0:
#      print(year, 'is a leap year')
# else:
#      print(year, 'is not a leap year')


# number = int(input('enter number: '))
# if number == 1:
#     print('Sunday')
# elif number == 2:
#     print('Monday')
# elif number == 3:
#     print('Tuesday')
# elif number == 4:
#     print('Wednesday')
# elif number == 5:
#     print('Thursday')
# elif number == 6:
#     print('Friday')
# elif number == 7:
#     print('Saturday')
# else:
#     print('Invalid')

# my_name = "nathaniel"
# name = input('enter your name: ')
# if name.upper() == my_name :
#     print('That is me!')
# else:
#     print('Hello Stranger!')

# score = int(input('enter your score: '))
# if score >= 90:
#     print('A')
# elif score >= 75:
#     print('B')
# elif score >= 60:
#     print('C')
# elif score < 60:
#     print('F')
# a = 'hello'
# b = "hello"
# sentence = ''' i am a boy
#  i live at abeokuta 
#  i am currently learning phyton language
# '''
# name = ' hellobOlA  '
# # print(name.lower())
# # print(name.upper())
# # print(name.strip())
# # print(name.replace('j', 'h'))
# print(name.split(","))
# String concatenation
# a = 'ade'
# b = 'ola'
# c= a + b
# print(c)
# a = "hello"
# b = 'john'
# c = a + ' ' + b
# print (c)
# age = 4
# print("i am " + age + "years old")
# a = 13
# print(f'i am {a} years old')
# age = 12
# text = f'i am {age} years old'
# print(text)
# age = 21
# name = 'john'
# print(f'my name is {name} and i am {age} years old')
# print(f'i will be {age + 1} years old next year')

# Casting 
# from unicodedata import name


# a = float(5)
# print(a)
# b = int(25433433.867675)
# print(type(b))
# c = int("10")
# print(type(c))
# c = float('3.14')
# d = float('7')
# r = float(3.6)
# print(c, d, r)
# print(type(c), type(d), type(r))
# x = str(1)
# d = str(2.5)
# h = str(True)
# print(x, d, h)
# print(type(x), type(d), type(h))
#  List used to store multiple items in a single variable
# names = ['ade', 'bolu', 'shola', 'tade']
# print(names[-3])
# fruits = ['apple', 'banana', 'orange', 'mango','mango', 'melon','kiwi']
# print(fruits[1:])
# if "banana" in fruits:
#     print("banana is present in fruits list")
# else:
#     print ("does not exist")
# animals = ['cat', 'dog', 'rabbit', 'parrot', 'snake', 'fish', 'tiger', 'lion', 'elephant']
# s = ['asd',1,2.7,True]
# animals.remove('snake')
# animals.pop(2)
# print(len(animals))
# animals.insert(1, 'hamster')
# print(animals)
# animals.append('hamster')
# animals[1] = 'hamster'
# animals[0:4] = ['hamster', 'guinea pig', 'ferret', 'chinchilla']
# print(animals[0:4])
# i=1
# while i > 6:
#     print(i)
#     if i == 4:
#         break
#     i += 1

# m = 1
# while m < 8:
#     m += 1
#     if m == 5:
#         continue
#     print(m)

# i=1
# while i < 6:
    # print(i)
    # i += 1
# else:
    # print("i is no longer less than 6")

# fruits = ["orange", "banana", "pawpaw", "mango"]
# for i in fruits:
#     print(i)

# names = ['ade', 'bola', 'shola', 'tade']
# for i in names:
#     print(i)
#     if i == "mike":
#         break 

# names = ['ade', 'bola', 'shola', 'tade', 'mike', 'john', 'james']
# for i in names:
#     if i == "mike":
#         continue
#     print(i)

# for i in range(6):
#     print(i)

# for i in range(2, 10):
    # print(i)

# for i in range(2, 15, 2):
#     print(i)

# for i in range(2,52,2):
#     print(i)

# for i in range(8):
#     print(i)
# else:
#     print("Finally finished!")

# for i in range(11):
#     if i == 4:
#         break
#     print(i)
# else:
#     print("Finally finished!")

# def my_name():
#     name = input('enter your name: ')
#     print(f'hello {name}')

# def greet(name):
#     print(f'hello {name}')
# greet("john")

# def calculate_area(length, width):
#     area = length * width
#     return area

# calculated_area = calculate_area(2, 5)
# print(f'The area is: {calculated_area}')

# def say_hello():
#     print('Hello World!')
# say_hello()

# temp1 = 20
# celsius = (temp1 - 32) * 5/9
# print(f'{temp1} degrees Fahrenheit is equal to {celsius} degrees Celsius.')

# temp2 = 30
# celsius = (temp2 - 32) * 5/9
# print(f'{temp2} degrees Fahrenheit is equal to {celsius} degrees Celsius.')

# temp3 = 40
# celsius = (temp3 - 32) * 5/9
# print(f'{temp3} degrees Fahrenheit is equal to {celsius} degrees Celsius.')

# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5/9

# print(fahrenheit_to_celsius(77))
# print(fahrenheit_to_celsius(86))
# print(fahrenheit_to_celsius(95))

# def greeting():
#     return "Hello, World!"

#     greeting()


# for i in range(1, 31):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# username = "admin"
# password = "python123"

# for attempt in range(3):
#     user = input("Enter username: ")
#     pw = input("Enter password: ")

#     if user == username and pw == password:
#         print("Login successful")
#         break
#     else:
#         print("Invalid username or password")
# else:
#     print("Account locked")

# number = int(input("Enter a positive number: "))

# while number >= 1:
#     print(number)
#     number -= 1

# print("Done!")

# total = 5

# while True:
#     number = int(input("Enter a number: "))

#     if number == 0:
#         break

#     total += number

# print("Total:", total)

# password = "python123"

# for attempt in range(3):
#     pw = input("Enter password: ")

#     if pw == password:
#         print("Login successful")
#         break
# else:
#     print("Account locked")

# number = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(number, "x", i, "=", number * i)

# N = int(input("Enter a number: "))

# total = 0

# for i in range(1, N + 1 ):
#     total += i

# print("Sum:", total)

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))

# if num1 >= num2 and num1 >= num3:
#     largest = num1
# elif num2 >= num1 and num2 >= num3:
#     largest = num2
# else:
#     largest = num3

# print("Largest:", largest)

# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# Positive = 0
# negative = 0
# zero = 0
# for i in range(5):
#     number = int(input("Enter a number: "))
#     if number > 0:
#         Positive = Positive +1
#     elif number < 0:
#         negative = negative + 1
#     else:
#         zero = zero + 1
# print("Positive numbers:", Positive)
# print("Negative numbers:", negative)
# print("Zero numbers:", zero)

# for i in range (1,101):
#     if i % 2 == 0:
#         print (i)

# a = random.randint(1,101)
# b = random.randint(1,101)
# c = a+b
# d = int(input(f'what is {a} + {b}? '))
# if c == d:
#     print ('Correct!')
# else:
#     print ("Try again!")

# a = random.randint(1,100)
# b = random.randint(1,100)
# c=a+b
# d = int(input(f'what is {a} + {b}? '))
# while d != c:
#     print ("Try again")
#     a = random.randint(1,100)
#     b = random.randint(1,100)
#     d = int(input(f'what is {a} + {b}? '))
#     continue
# if d == c:
#     print ('Correct!')

# correct = 0
# wrong = 0
# a = random.randint(1,100)
# b = random.randint(1,100)
# c = a+b
# d = int(input(f'what is {a} + {b}? '))
# while d == c:
#         correct += 1
#         if (correct)+(wrong)!= 10:
#                          a = random.randint(1,100)
#                          b = random.randint(1,100)
#                          c = a+b
#                          d = int(input(f'what is {a} + {b}? '))
#                          continue
#         if (correct)+(wrong)==10:
#                         break
# while d!=c :
#          wrong += 1     
#          if (correct)+(wrong)!= 10:
#                  a = random.randint(1,100)
#                  b = random.randint(1,100)
#                  c = a+b
#                  d = int(input(f'what is {a} + {b}? '))
#                  continue
#          if (correct)+(wrong)==10:
#                 break
           
# print ("Correct= ", correct)
# print ("Wrong= ", wrong)

# i = 1
# correct = 0
# wrong = 0

# while(i <= 10):
#     a = random.randint(1,100)
#     b = random.randint(1,100)
#     c = a+b
#     d = int(input(f'what is {a} + {b}? '))  
#     if d == c:
#         correct += 1
#     else:
#         wrong +=1
#     i+=1
# print ("Correct", correct)
# print ("Wrong", wrong)

# a=int(input("Enter amount of students: "))
# i =1
# while i<a:
#     b=input(f"Enter name of Student {i}: ")
#     c=input(f"Enter {b}'s result: ")
#     i+=1



# year = int(input("Enter a year: "))
# if year % 4 ==0:
#     print("It is a leap year")
# else:
#     print ("It is not a leap year")



# number = int(input("Enter a number: "))
# for i in range(1, 13):
#     print(number, "x", i, "=", number * i)



# total = 0
# for i in range (10):
#     number = int(input("Enter a Number: "))  
# if number < 0:
#     continue
# total = total + number
# print ("Total= ",total)



# count = 0

# for number in range(2, 101):
#     prime = True

#     for i in range(2, number):
#         if number % i == 0:
#             prime = False
#             break

#     if prime:
#         count = count + 1

# print("Number of prime numbers:", count)



# numbers = []

# for i in range(20):
#     number = int(input("Enter a number: "))
#     numbers.append(number)

# largest = max(numbers)
# smallest = min(numbers)
# total = sum(numbers)
# average = total / 20

# positive_count = 0
# negative_count = 0
# zero_count = 0
# even_count = 0
# odd_count = 0

# for number in numbers:

#     if number > 0:
#         positive_count += 1

#     elif number < 0:
#         negative_count += 1

#     else:
#         zero_count += 1

#     if number % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1

# print("Largest:", largest)
# print("Smallest:", smallest)
# print("Sum:", total)
# print("Average:", average)
# print("Positive count:", positive_count)
# print("Negative count:", negative_count)
# print("Zero count:", zero_count)
# print("Even count:", even_count)
# print("Odd count:", odd_count)
    


# numbers = []

# n = int(input("How many numbers do you want to enter? "))

# for i in range(n):
#     number = int(input("Enter a number: "))
#     numbers.append(number)

# numbers = list(set(numbers))
# numbers.sort()

# if len(numbers) < 2:
#     print("There is no second-largest number")
# else:
#     print("Second-largest number:", numbers[-2])



# number = int(input("Enter a number: "))

# print("Factors of", number, "are:")

# for i in range(1, number + 1):
#     if number % i == 0:
#         print(i)



# username = "admin"
# password = "Python123!"

# username = input("Enter username: ")
# password = input("Enter password: ")

# if len(username) < 5:
#     print("Username must be at least 5 characters long")

# elif len(password) < 8:
#     print("Password must be at least 8 characters long")

# elif username != username:
#     print("Incorrect username")

# elif password != password:
#     print("Incorrect password")

# else:
#     print("Login successful")



# hour = int(input("Enter an hour (0-23): "))

# if hour >= 5 and hour < 12:
#     print("Morning")

# elif hour >= 12 and hour < 17:
#     print("Afternoon")

# elif hour >= 17 and hour < 21:
#     print("Evening")

# elif hour >= 21 or hour < 5:
#     print("Night")

# else:
#     print("Invalid hour")



# number = int(input("Enter a number: "))

# original = number
# digits = len(str(number))
# total = 0

# while number > 0:
#     digit = number % 10
#     total = total + digit ** digits
#     number = number // 10

# if total == original:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")


# def full_name (first, last):
#     return first + " " + last
# full_name("Agent", "Dark")
# print(full_name("Agent", "Dark"))








    








    
    
    









 
         
    



















    






  