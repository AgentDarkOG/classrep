# import random
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

# numbers = list(numbers)
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

# usernames = input("Enter username: ")
# passwords = input("Enter password: ")

# if len(username) < 5:
#     print("Username must be at least 5 characters long")

# elif len(password) < 8:
#     print("Password must be at least 8 characters long")
# elif usernames == username and passwords == password:
#     print("Login successful")
# else:
#     print ("Incorrect username or password")



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


# number= int(input("Enter a number: "))
# if number < 0:
#     print ("Negative")
# elif number>0:
#     print ("Positive")
# else : 
#     print ("Zero")
# if number % 2 == 0:
#     print ("Even")
# else: 
#     print ("Odd")

# number=int(input("Enter a Number: "))
# for i in range (number+1, -1, -1):
#     print (i)

# 
# 
# total = 0
# for i in range(1,101):
#     if i % 3 == 0 or i % 5 == 0:
#         total += i
# print(total)



# number = random.randrange(1,100)
# secret = number
# print("You have 5 attempts to guess the number!!")
# a= 1
# i = 0
# while i < 5 :
#     b = int(input(f"Enter guess {a}: "))
#     if b < secret:
#          print ("Higher than that")
#     elif b> secret:
#         print ("Lower than that")

#     if b == secret:
#         print ("Correct")
#         break 
#     i+=1
#     a+=1
# if i == 5:
#     print ("Game Over")
#     print (secret)


# number = int(input("Enter a number: "))
# prime = True
# for i in range(2, number):
#     if number % i == 0:
#         prime = False
#         # break
        

# if prime:
#     print("Prime Number")
# else:
#     print("Not a Prime Number")


# for number in range(2, 101):
#     prime = True

#     for i in range(2, number):
#         if number % i == 0:
#             prime = False
#             break

#     if prime:
#         print (number, end=", ")

# numbers=[]
# i=0
# while i == 0:
#     number=(int(input("Enter a Number: ")))
#     numbers.append(number)
#     total= sum(numbers)
#     amt_of_numbers= len(numbers)
#     average = total/amt_of_numbers
#     largest = max(numbers)
#     smallest= min(numbers)
#     if number == 0:
#         break
# print ("Total= ", total)
# print ("Amount of numbers= ", amt_of_numbers)
# print("Average:", average)
# print("Largest:", largest)
# print("Smallest:", smallest)

# names ='ade','bola','tade'
# print(len(names))
# item = ('bola',)
# print(type(item))
# number = []
# item = ()
# print(type(item))
# CHANGIN ITEM IN A TUPPLE
# fruits = ('banana','orange','cherry','apple','melon','grape')
# y = list(fruits)
# y[1] = 'kiwi'
# fruits =tuple(y)
# print(fruits)
# print (fruits[:3])
# ADDING ITEM TO A TUPPLE
# names = ('malik','yunus')
# a = list(names)
# a.append ('shade')
# names = tuple(a)
# print(names)
# ADDING TUPPLE TO A TUPPLE
# cities= ('lagos','ibadan','osun')
# d = ('jos',)
# cities +=d
# print(cities)
# subjects = ('math','civic','art','science')
# for subject in subjects:
#     print(subject)

# for i in range(len(subjects)):
#     print(subjects[i])
# i = 0
# while i < len(subjects):
#     print(subjects[i])
#     i+=1
# JOINING TUPPLE
# tupple1 = ('bola','sade','tade')
# tupple2 = (1,3,4)
# tupple3 = tupple1 + tupple2
# print(tupple3)
# names = ('ade','tade','bayo')
# my_tupple = names *2
# print(my_tupple)
# UNPACKING TUPPLE
# names = ('laide','shope','malaika','bande','ope','muslimah')
# (green,*yellow,blue) = names
# print(green)
# print(yellow)
# print(blue)
# SETS
# fruit = {"apple",'lemon','paw paw',1,1,'apple',2}
# for i in fruit:
#     print(i)
# fruit.add('pine-apple')
# print(fruit)
# print("apple"in fruit)
# print('lemon'not in fruit)
# print(len(fruit))

# names = set(('ade','tayo','lawal'))
# print(type(names))
# subjects = {'art','math','civic'}
# science = {'physics','chemistry','biology','art'}
# subjects.update(science)
# print(subjects)
# thisset = {'ade','bola','tade'}
# thisset.remove('lawal') #the remove will raise an error why the discard() will retun the set back
# print(thisset)
# my_list = ['jagaban','ola']
# thisset.update(my_list)
# print(thisset)
# names = {'bola','ade','dayo','shewa'}
# names.clear()
# print(names)
# x = names.pop()
# print(x)
# print(names)

# a= 8
# b = 3 
# c = None
# if a > b :
#     c=b
#     b=a
#     a=c
#     print(a)
#     print(b)

# a = 2
# b = 3
# c = 0
# if a*b*c > 0:
#     print ("Positive")
# elif a*b*c <0:
#     print ("Negative")
# else:
    # print ("Zero")

# a=float(input("Enter first number: "))
# b=float(input("Enter second number: "))
# c=float(input("Enter third number: "))
# if (b>a and b<c) or (b>c and b<a):
#     print (b)
# elif (a>b and a<c) or (a>c and a<b):
#     print (a)
# else:
#     print (c)

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# c = float(input("Enter third number: "))

# if a >= b and a >= c:
#     if b >= c:
#         print(a, b, c)
#     else:
#         print(a, c, b)

# elif b >= a and b >= c:
#     if a >= c:
#         print(b, a, c)
#     else:
#         print(b, c, a)

# else:
#     if a >= b:
#         print(c, a, b)
#     else:
#         print(c, b, a)


# a = float(input("Enter Opposite lenght: "))
# b = float(input("Enter Adjacent lenght: "))
# c = float(input("Enter Hypotenuse lenght: "))
# if c** 2 == a**2 + b**2:
#     print (" Valid triangle ")
# else:
#     print(" Invalid Triangle ")


# N = int(input("Enter a number: "))
# for i in range (1,N+1):
#     print (i)
# for i in range(1, N +1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


# N = int(input("Enter a number: "))
# for i in range(1, N +1):
#     if i % 3 == 0 and i % 5 != 0:
#         print(i)

# limit=(200)
# total = (0)
# while total < limit:
#     b = int(input("Enter a number: "))
#     total+=b
#     if total >= limit or b ==0:
#         print (total)
#         break


# while True:
#     number = int(input("Enter a number: "))

#     if 1 <= number <= 100:
#         break

# print("Valid number:", number)


# N = int(input("Enter N: "))

# found = False

# for number in range(1, N + 1):
#     if number > 20 and number % 7 == 0 and number % 3 != 0:
#         print("First matching number:", number)
#         found = True
#         break

# if not found:
#     print("No matching number found.")






 
