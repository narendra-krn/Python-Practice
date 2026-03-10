# addition:

# num1 = 10
# num2 = 10
# result = num1 + num2
# print(result)

# Addition:
# num1 = 10
# num2 = 10
# result = num1 - num2  # expression changed by giving -
# print(result)
# the expected result also changed but their is no error in the flow of execution.
# this type of error is called "Logical Error".

# for var in seq:
#       block of code

# for i in range(5):   # here if we forget to place the colun.
#     print(i)
# the above code will be executed with error
# this type of code is called "Syntax Error" or "Identified Error"

# Runtime Errors
# -->Which distrubs the flow of execution(during the execution) also called as exceptions.

# To over come from the above error in python, we will use try and except method.

# num1 = input("Enter the num1 value : ")
# num2 = input("Enter the num2 value : ")
# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)
# print(num1 + num2)
# print(num1 - num2)
# if we enter 10 and 5 => there is no error in the flow of execution.
# But if we enter 10 and 0 ==> we will ggwt the error in the flow of execution.

# num1 = int(input("Enter the num1 value : "))
# num2 = int(input("Enter the num2 value : "))
# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# try:
#     print(num1 / num2)
# except:
#     print("Error occured")
# print(num1 + num2)
# print(num1 - num2)

# Example:
# list_1 = [1, 2, 3, 4, 5]
# print(list_1[4])
# try:
#     print(list_1[6])
# except:
#     print(len(list_1))
#     print("index range below : ", len(list_1))
# print(list_1[0])
# print(list_1[3])

# Exm:
# list_1 = [1, 2, 3, 4, 5]
# try:
#     print(list_1[4])
# except:
#     print(f"index range should be below {len(list_1)}")
# else:   # code to execute if exception is raised
#     print(list_1[0])
#     print(list_1[1])
# finally:    # code to execute ragardless of wheater an exception was raised or not
#     print("regardless block")

# Example:
# try:
#     num_1 = int(input("Enter num_1 value : "))
#     num_2 = int(input("Enter num_2 value : "))
# except ValueError as e:  # here the error will store in the e
#     # the error will be displayed and the given input also displayed due to using of ValueError class
#     print(e)
# else:
#     print(num_1 + num_2)

# Example:
# num_1 = int(input("Enter num_1 value : "))
# num_2 = int(input("Enter num_2 value : "))
# try:
#     print(num_1 / num_2)
# except ZeroDivisionError as e:
#     print(e)

# Example:
try:
    num_1 = int(input("Enter num_1 value : "))
    num_2 = int(input("Enter num_2 value : "))
    print(num_1 / num_2)
except Exception as e:
    print(e)
