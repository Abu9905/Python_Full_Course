
# ============= Variable and Data Types in Python ============= //
age = 21; # Integer
print(age)

name = "abu"; # String
print(name)

cgpa = 4.55; # float
print(cgpa)


# Rule of defining a variable in python.
# 1.) Variable name must start with a letter (a-z, A-Z) or underscore (_).
# 2.) They can contain letters, numbers (0-9), and underscores (_).
# 3.) Variable names are case-sensitive.(age and Age are different variables)
# 4.) Avoid using Python keywords as variable names.(if, else, for, while, etc.)

# 34age = 34; # This is not a valid variable name because it starts with a number.
# age = 34; # This is a valid variable name because it starts with a letter.
# a$$ge = 34; # This is not a valid variable name because it contains a special character ($).
__age = 34; # This is a valid variable name because it starts with an underscore.
__nice_45 = 34; # This is a valid variable name because it starts with an underscore and contains numbers.
a_B_C_7 = 34; # This is a valid variable name because it starts with a letter and contains underscores and numbers.

# ==== Python supports serveral built-in data types ====
    #  1.) Integer (int): Whole numbers (e.g., 1, 2, 3)
    #  2.) Float (float): Decimal numbers (e.g., 1.5, 2.0, 3.14)
    #  3.) String (str): Text data (e.g., "Hello", 'World')
    #  4.) Boolean (bool): True or False values (e.g., True, False)
#  5.) Lists : Ordered, mutable collections of items (e.g., [1, 2, 3], ["apple", "banana"])
#  6.) Tuples : Ordered, immutable collections of items (e.g., (1, 2, 3), ("apple", "banana"))
#  7.) Sets : Unordered collections of unique items (e.g., {1, 2, 3}, {"apple", "banana"})
#  8.) Dictionaries : Key-value pairs (e.g., {"name": "Alice", "age": 30})

my_Age = 21 # Integer
print(my_Age)
print(type(my_Age)) # Check the data type of my_Age

my_Age = 22.56 # Float
print(my_Age)
print(type(my_Age)) # Check the data type of my_Age
# Reassigning the variable to a different data type

my_name = "Abu" # String
print(my_name)
print(type(my_name)) # Check the data type of my_name
# Reassigning the variable to a different data type

user_Login = True # Boolean
print(user_Login)
print(type(user_Login)) # Check the data type of user_Login
# Reassigning the variable to a different data type

user_Logout = False # Boolean
print(user_Logout)
print(type(user_Logout)) # Check the data type of user_Logout
# Reassigning the variable to a different data type