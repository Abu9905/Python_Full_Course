
# ======== Strings in Python ======== //

name = "abu"
# print(name)  # Output: abu

my_name = "sama"
# print(my_name)  # Output: sama
# Strings can be defined using single or double quotes

user_name = '''Abu shama
      my age is 20'''
# print(user_name)  # Output: Abu shama
# Triple quotes can be used for multi-line strings


# ==== String Indexing ==== //

book_list = "Python"
# print(book_list)  # Output: Python, Java, C++

# print(book_list[0])  # Output: P
# print(book_list[1])  # Output: y
# print(book_list[2])  # Output: t
# print(book_list[-1])  # Output: +

# ==== String Slicing ==== //

my_user_name = "Abushama67236985"
# print(my_user_name[0])  # Output: A
# print(user_name[0:2])  # Output: Abu , goes from 0 to 2-1 ie 0 to 1

# print(user_name[2:-1]) # same as name[2:4]

# print(my_user_name[0:16:1]) # skip n-1 characters, here n=1 so no skip
# print(my_user_name[0:16:2])  # Output: Ahs67285, skips every second character

# print(my_user_name[0:16:3])  # Output: A6m3, skips every third character
# print(my_user_name[:4]) # Replace the first empty with 0 # name[0:4]
# print(my_user_name[1:]) # Replace the second empty with -1 # name[1:16]


# ====== String Methods ======== //
# 1.) Multiple String Methods:-

login_name = "  Abu shama " # String are immutable, so we need to assign the result to a new variable or the same variable

# login_name[0] = "a"  # I can not change the first character of a string, it will give an error

# a = len(login_name)  # Output: 8, gives the length of the string
# print(a)  # Output: 8

# print(login_name.upper())
# print(login_name.lower(), login_name)
# print((login_name.strip()))
# print(login_name.capitalize())

# === Remaoving Spaces === //

# print(login_name.strip())  # Removes leading and trailing spaces
# print(login_name.lstrip())  # Removes leading spaces
# print(login_name.rstrip())  # Removes trailing spaces


# === Sting Formatting === //

template = "Dear {} , Abu , You are awesome. Take this {},10000$ bag"


al = "Jhon"
al1 = 10000
b = "jack"
b1 = 100
c = "sama"
c2 = 2000

s1 = template.format(al, al1) 
# print(s1)  # Output: Dear Jhon , Abu , You are awesome. Take this 10000,10000$ bag

# === F-Strings === //

print(f"Dear {al} , Abu , You are awesome. Take this {al1},10000$ bag")  
# Output: Dear Jhon , Abu , You are awesome. Take this 10000,10000$ bag