# a= int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# c = None
# if a > b :
#     a,b = b,a
# print(a,b)

# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# c = int(input("Enter a number: ")) 
# # if a*b*c > 0:
# #     print ("Positive")
# # elif a*b*c <0:
# #     print ("Negative")
# # else:
# #     print ("Zero")
# if a==0 or b==0 or c==0:
#     print ("Zero")
# elif(a<0 and b>0 and c>0) or (a>0 and b<0 and c>0) or (a>0 and b>0 and c<0):
#     print ("Negative")
# else:
#     print ("Positive")


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


# a = float(input("Enter first lenght: "))
# b = float(input("Enter second lenght: "))
# c = float(input("Enter third lenght: "))
# if (a+c > b and a+b >c) and (b+c>a):
#     print (" Valid triangle ")
# else:
#     print(" Invalid Triangle ")


# N = int(input("Enter a number: "))
# # for i in range (1,N+1):
# #     print (i)
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

# limit=int(input("Enter limit: "))
# total = (0)
# while total < limit:
#     b = int(input("Enter a number: "))
#     total+=b
#     if total >= limit :
#         print ("Your total has reached or might have exceeded the limit")
#         print ("Total=", total)
#         break
#     elif b == 0:
#         print ("You input '0' as one of your numbers")
#         print ("Total=", total)
#         break

# while True:
#     number = int(input("Enter a number: "))

#     if 1 <= number <= 100:
#         break

# print("Valid number:", number)


# N = int(input("Enter N: "))

# found = False

# for number in range(20, N + 1):
#     if number % 7 == 0 and number % 3 != 0:
#         print("First matching number:", number)
#         found = True
#         break

# if not found:
#     print("No matching number found.")





# numbers = []
# n = int(input("How many numbers? "))
# for i in range(n):
#     number = int(input("Enter number: "))
#     numbers.append(number)
# largest = numbers[0]
# smallest = numbers[0]
# positive = 0
# negative = 0
# zero= 0
# for number in numbers:
#     if number > largest:
#         largest = number

#     if number < smallest:
#         smallest = number

#     if number > 0:
#         positive += 1
#     elif number < 0:
#         negative += 1
#     else:
#         zero += 1
# print("Largest:", largest)
# print("Smallest:", smallest)
# print("Positive:", positive)
# print("Negative:", negative)
# print("Zero:", zero)



# numbers = [5, 3, 8, 3, 9, 5]
# seen = []
# for num in numbers:
#     if num in seen:
#         print("First duplicate:", num)
#         break
#     seen.append(num)
# else:
#     print("No duplicate")



# numbers = [4, 2, 4, 7, 2, 2, 9]
# seen = []
# duplicates = []
# for num in numbers:
#     if num in seen:
#         if num not in duplicates:
#             duplicates.append(num)
#     else:
#         seen.append(num)
# print(duplicates)



# numbers = [2, 2, 2, 5, 5, 3, 3, 3, 3, 1]
# current_value = numbers[0]
# current_length = 1
# longest_value = numbers[0]
# longest_length = 1
# starting_index = 0
# current_start = 0
# for i in range(1, len(numbers)):

#     if numbers[i] == current_value:
#         current_length += 1
#     else:
#         current_value = numbers[i]
#         current_length = 1
#         current_start = i

#     if current_length > longest_length:
#         longest_length = current_length
#         longest_value = current_value
#         starting_index = current_start

# print("Value:", longest_value)
# print("Length:", longest_length)
# print("Starting index:", starting_index)


# a = int(input("Enter first value: "))
# b = int(input("Enter second value: "))
# def compare(a, b):
#     if a > b:
#         return "greater"
#     elif a < b:
#         return "smaller"
#     else:
#         return "equal"

# print(compare(a, b))


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# def get_max(a, b, c):
#     greatest = a

#     if b > greatest:
#         greatest = b

#     if c > greatest:
#         greatest = c

#     return greatest
# print("Greatest:", get_max(a, b, c))


# number = int(input("Enter a number: "))
# def classify_number(n):

#     if n == 0:
#         return "zero"

#     if n > 0:
#         if n % 2 == 0:
#             return "positive even"
#         else:
#             return "positive odd"

#     else:
#         if n % 2 == 0:
#             return "negative even"
#         else:
#             return "negative odd"

# print(classify_number(number))


# def is_leap_year(year):
#     if year % 4 == 0:
#         return True
#     else:
#         return False
    
# def is_valid_date(day, month, year):
#     if month < 1 or month > 12:
#         return False

#     days_in_month = [31, 28, 31, 30, 31, 30,
#                      31, 31, 30, 31, 30, 31]
#     if month == 2 and is_leap_year(year):
#         max_days = 29
#     else:
#         max_days = days_in_month[month - 1]
#     if day >= 1 and day <= max_days:
#         return True
#     else:
#         return False
# while True:
#     date = int(input("Enter the date:"))
#     month = int(input("Enter the month"))
#     year = int(input("Enter the year"))
#     if is_valid_date(date, month, year):
#         print ("Valid Date")
#     else:
#         print("Invalid Date")

    
# numbers =[4,2,7,4,2,9,7,1]
# new_list=[]
# for num in numbers:
#     if num not in new_list:
#         new_list.append(num)
# print (new_list)

 




# def calculate_discount(price, customer_type):

#     if customer_type == "regular":
#         discount = price * 0.05

#     elif customer_type == "premium":
#         discount = price * 0.10

#     elif customer_type == "vip":
#         discount = price * 0.20

#     else:
#         discount = 0

#     return discount


# while True:
#     price = float(input("Enter price: "))
#     customer_type = input("Enter customer type: ")

#     discount = calculate_discount(price, customer_type)
#     final_price = price - discount

#     print("Discount:", discount)
#     print("Final price:", final_price)

#     again = input("Another purchase? (yes/no): ")

#     if again.lower() != "yes":
#         break

