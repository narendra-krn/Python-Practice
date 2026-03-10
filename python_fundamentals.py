# writing print statement in python

print("coding practice.....")
print("welcome python_life....")

# Comments
# single lines comments starting with => #
print(10 + 10)
print(10 * 5)
'''
multi line comments are writen in ''' ''',
multi line comments are writen in """ """,
multi line comments are used for long description.
'''

# Variables
# Syntax: var = value

roll_num = 46

"""
roll_num => varible
= => assignment operator
46 => value
"""

# Data Types
"""
Integer, float, complex number      //Numeric
Boolean,
Strings, list, tuple                //sequence type
set,
Dict
"""

# Integer (int)
product_price = 310
chicken_biryani = 350

# Float (float)
mutton_biryani = 499.99
mutton_mundi = 1099.99

# Complex (complex)
equation_value1 = 2-5j
equation_value2 = 3+9j

# Boolean (bool)
text_1 = True
text_2 = False
print(type(text_1))
print(type(text_2))

# String (str)
camel_case = 'studentName'
snake_case = "student'name"
pascal_case = """StudentName"""

print(type(camel_case))
print(type(snake_case))
print(type(pascal_case))

# Type Conversion
'''
Implicit Type Comversion    (Automatic)
Explicit Type Conversion    (Manual)
'''

# Int ==> Float
age = 35
print(age)
print(type(age))

float_conversion = float(age)
print(float_conversion)
print(type(float_conversion))


# Float ==> Int
price = 99.98
print(price)
print(type(price))

int_conversion = int(price)
print(int_conversion)
print(type(int_conversion))


# String ==> Int
room_num = "4321"
print(type(room_num))

int_conversion = int(room_num)
print(int_conversion)
print(type(int_conversion))

# String ==> float
height = "5.6"
print(type(height))
float_conversion = float(height)
print(float_conversion)
print(type(float_conversion))

# Input() - It is used to enter values dynamically(user_inputs).
first_name = input("Enter your First Name: ")
last_name = input("Enter your Last Name: ")

result = first_name + last_name
print(result)
print(type(result))

product1_price = int(input("Enter product 1 value: "))
product2_price = int(input("Enter product 2 value: "))

total_price = product1_price + product2_price

print(total_price)
print(type(total_price))


"""
string * Value  ("546" * 3)         ==>repetations
int * int       (10 * 5)            ==> Multiplication
int1 ** int2      (5 ** 4)          ==> int1 power of int2
"""
# print("546" * 3)
# print(10 * 5)
# print(5 ** 4)


'''
task 6--> practice datatypes ,type conversion and input function
task 7--> Complete the fundamentals task by using input functions only where needed.
'''

"""
1. Print Statement:
Write a program that prints a pattern using multiple print statements.
2. Comments:
Create a Python script for a simple task and add comments to
explain each step.
3. Data Structures & Data Types:
Implement a program that uses a dictionary to store information
about a book (title, author, publication year).
4. String Operations:
Write a python program that takes a string as input ( 35 ) and return
float value.
5. Concatenate Strings:
Write a program to take two names as input and print them together.
6. Type Conversions:
Create a program that takes user input for their age, converts it to
an integer, adds 5, and then prints the result.
7. Simple Input & Output:
Build a calculator program that takes two numbers as input and
performs the arithmetic operation.
"""

# 1
print("*******")
print(" ***** ")
print("  ***  ")
print("   *   ")

# 2
# single line comments started with the "#". Also known as line comments.
# here declaring a variable roll number and assigned a value is 346.
roll_num = 346
emp_id = 600  # here declaring a variable emp id and assigned value is 600.

"""
multiline comments started with triple single quote's(''')/ 
triple double quote's(""" """)
to explain the large / big logic code's.
"""

# 3
book_details = {
    "title": "machanics",
    "author": "carlmars",
    "publication_year": "1896"
}
print(type(book_details))

# 4
# here we need to enter the price value as 35.
product_price = input("Enter the Price: ")
print(float(product_price))


value = input("Enter a number: ")   # Example input: 35
result = float(value)

print(result)
print(type(result))

# 5
first_name = str(input("Enter your First Name : "))
last_name = str(input("Enter your Last Name : "))
full_name = first_name + last_name

print(full_name)

# 6
age = int(input("Enter Age : "))
boy_age = age + 5
print(boy_age)

# 7
value_1 = int(input("Enter the Value 1 : "))
value_2 = int(input("Enter the Value 2 : "))
addition = value_1 + value_2
print(value_1)
print(value_2)
print(addition)
print(type(addition))
