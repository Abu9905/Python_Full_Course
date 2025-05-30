
# ===== Conditional Statements in Python ===== //
# Conditional statements allow you to execute code based on certain conditions.

#  if , elif , else Statements:-

# age = 11;

# if(age>18):
#     print("You are an adult.")
#     print("You can vote.")
# elif(age==18):
#     print("You are just an adult.")
#     print("You can vote.")
# else:
#     print("You are not an adult.")
#     print("You cannot vote.")
    
# print("End of the program.")

# age = int(input("Enter your age: "))

# if(age>18):
#     print("You are and Adult.")
# elif(age == 18):
#     print("You are just an Adult.")
# else:
#     print("You are not an Adult.")
    
# print("End of the program.")    

age = int(input("Enter your age:"))

if(age>18):
    print("You Can Drive.")
elif(age==18):
    print("You can drive but you need to get a license first.")
elif(age==0):
    print("You are not born yet.")
else:
    print("You cannot drive yet.")