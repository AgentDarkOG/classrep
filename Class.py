numbers = []
n = int(input("Ho many numbers do you ant to enter? "))
for i in range(n):
    number = int(input("Enter a number: "))
    numbers.append(number)

# Calculate Mean
total = 0

for number in numbers:
    total = total + number

mean = total / n
# Calc