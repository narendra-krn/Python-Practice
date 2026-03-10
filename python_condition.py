"""

8. BMI Calculator:
Write a program that calculates the Body Mass Index (BMI) using the
formula: BMI = weight (kg) / (height (m))^2. The program should take
weight and height as input.
"""

'''
1. Vowel Checker:
Write a Python program that takes a character as input and checks whether
it is a vowel or not. Use the
if-else statement.
'''
# char = input("Enter any Character : ")
# if char in "aeiouAEIOU":
#     print("It is a Vowel....")
# else:
#     print("it is a Consonent.....")

'''
2. Age Group Classification
Write a program that takes an age as input and classifies the person into
one of the following age groups:
Child: 0-12 years
Teenager: 13-17 years
Adult: 18-64 years
Senior: 65 years and older
'''
# age_group = int(input("enter a number : "))
# if age_group >= 100 and age_group >= 0:
#     print("invalid number")
# elif age_group <= 12:
#     print("your age catagery is Child.....")
# elif age_group <= 17:
#     print("your age catagery is Teenager.....")
# elif age_group <= 64:
#     print("your age catagery is Adult.....")
# elif age_group >= 65:
#     print("your age catagery is senior......")
# else:
#     print("invalid number 2")

'''
Number Classifier:
Write a program that takes an integer as input and classifies it as positive,
negative, or zero. Use the
if-elif-else statement.
'''
# number = int(input("Enter any Number : "))
# if number > 0:
#     print("The number is positive.....")
# elif number < 0:
#     print("The number is negative.....")
# else:
#     print("The number is 0(zero)")

'''
Create a program that checks whether a given year is a leap year or not. A
leap year is divisible by 4, but not by 100 unless it is divisible by 400.
'''
# year = int(input("Enter the year : "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("It is a Leap Year")
# else:
#     print("It is NOT a Leap Year")

'''
Build a simple calculator program that takes two numbers and an operator
(+, -, *, /) as input and performs the corresponding operation.
'''
# num1 = float(input("Enter first number: "))
# operator = input("Enter operator (+, -, *, /): ")
# num2 = float(input("Enter second number: "))

# if operator == "+":
#     print("Result:", num1 + num2)
# elif operator == "-":
#     print("Result:", num1 - num2)
# elif operator == "*":
#     print("Result:", num1 * num2)
# elif operator == "/":
#     if num2 != 0:
#         print("Result:", num1 / num2)
#     else:
#         print("Error! Division by zero is not allowed.")
# else:
#     print("Invalid operator")

'''
Rewrite the following code using the short-hand
if statement:
x = 8
if x % 2 == 0: result = "Even"
else: result = "Odd"
'''
# x = 8
# result = "Even" if x % 2 == 0 else "Odd"

# print(result)


'''
Create a program that calculates the final price after applying a discount.
The program should take the original price and the discount percentage as
input.
'''
# original_price = float(input("Enter the original price: "))
# discount_percent = float(input("Enter the discount percentage: "))

# discount_amount = (original_price * discount_percent) / 100

# final_price = original_price - discount_amount

# print("Final price after discount:", final_price)


'''
Write a program that calculates the Body Mass Index (BMI) using the
formula: BMI = weight (kg) / (height (m))^2. The program should take
weight and height as input.
'''
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")
