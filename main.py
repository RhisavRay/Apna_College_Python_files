# print("Hello World")
# print(25, 33)
# print(25+33)
from os import name
from xmlrpc.client import Boolean

# ------------------------------------------------------------------ Variables in Python
# name = "Rhisav"
# age = 23

# print("My name is : " + name)
# print("I am " + str(age) + " years old.")
# The str(age) is needed as python can't concatenate str to str

# print("I am", age, "years old.")
# The same thing works when we use comma to separate them


# ------------------------------------------------------------------ Data types in Python
# name = "Rhisav"
# age = 23
# price = 16.34
# old = False
# a = None

# print(type(name))
# print(type(age))
# print(type(price))
# print(type(old))
# print(type(a))

# There are 5 data types in Python
# 1. Integer: +ve, -ve, zero
# 2. String: Anything between '', "", or even ''''''. But preferably use "" as that's the common rule of thumb used
# 3. Float: Decimal numbers
# 4. Boolean: True or False. Here the T and F HAVE to be in capital
# 5. None: This is used to represent the absence of a value or a null object reference


# Q---------Sum of variables
# a = 2
# b = 3
# sum = a + b
# print(sum)


# ------------------------------------------------------------------ Expression Execution
# a, b = 2, 3
# txt = "abc"
# print(a*txt*b)
# # When we do multiplication of a number and a string in Python, it just repeats that string for the number of times the integer is

# a, b = 1, 2
# c = a/b
# print(c)
# # Division between 2 integers will result in a float

# a, b = 1, 2
# c = a//b
# print(c)
# # Integer division will result in an integer

# a, b = 5, -2
# c = a%b
# print(c)
# # Remainder is negative when only denominator is negative