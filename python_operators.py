"""
1. Exercise: Create a program that takes user input for their name and age.
Use formatted strings (f-strings) to print a message welcoming the user and
stating their age.
2. Create a list called numbers that contains integers from 1 to 10.
Check if the number 5 is in the list.
Check if the number 15 is not in the list.
"""
# 1
user_name = str(input("enter the your name : "))
user_age = int(input("enter the your age : "))
print(f"welcome {user_name}, you are {user_age} years old.")

# 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(5 in numbers)
print(15 not in numbers)

"""
Exercise 1:
Write a Python program to calculate the area of a rectangle using the given
formula: area = length * width . Take the values of length and width as inputs from
the user.
Exercise 2:
Write a Python program to demonstrate incrementing and decrementing a variable
Exercise 3:
Write a Python program to convert temperature from Celsius to Fahrenheit. The
formula for conversion is: F = (C * 9/5) + 32 . Take the temperature in Celsius as
input from the user.
Exercise 4:
Write a Python program to calculate the simple interest given the principal
amount, rate, and time (in years).
Exercise 5:
Write a Python program to concatenate two strings and display the result. The
strings should be taken as input from the user.
Exercise 6:
Write a Python program to convert a distance from kilometers to miles.
"""
# Exe:1
length = int(input("Enter the value of Length: "))
width = int(input("Enter the value of width: "))
area = length * width
print(f"The total area is {area}")

# Exe: 2
product_cost = int(input("Enter the product cost: "))
cost_incriment = product_cost + 150
product_cost -= 50

print(cost_incriment)
print(product_cost)

# Exe: 3
celsius = int(input("Enter the temparature in celsius : "))
Fahrenheit = (celsius * (9/5)) + 32
print(f"The temparatue is {Fahrenheit}")

# Exe: 4
principle = 100000
time = 2
rate_interest = 10
total_amount = ((principle * time * rate_interest) / 100)
print(f"The total amount is {total_amount + principle}")

# Exe: 5
first_name = str(input('Enter your First Name: '))
last_name = str(input('Enter your Last Name: '))
full_name = first_name + last_name
print(first_name)
print(last_name)
print(f"My Full Name is {full_name}")

# Exe:6
kilometers = float(input("Enter kilometers : "))
miles = kilometers * 0.621
print(f"The total distance in {miles} miles.")
