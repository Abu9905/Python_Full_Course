# ===== Loops In Python =====  // Loops are used to execute a block of code repeatedly until a certain condition is met.
# There are two main types of loops in Python: for loops and while loops.
# For loops are used to iterate over a sequence (like a list, tuple, or string) or any iterable object.


# === For Loop === //
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)

# Now Using Loop :-

# for i in range(1, 6): # range Function goes 1 to (6-1) i.e 5 in this case.
    # print(i)
      
# for i in range(1,11):
#     print("5 X ", i, " = ", 5*(i))


# ===== While Loop ===== //

# print("1")
# print("2")
# print("3")
# print("4")
# print("5")

# count = 0;

# while count <= 5:
#     print(count)
#     # count += 1  # Increment the count by 1 each time the loop runs
    
#     count = count + 1  # Another way to increment the count by 1 each time the loop runs
    
    
# ===== Breack and Continue ===== //

for i in range(1 , 11):
    if i == 5:
        continue  # Skip the rest of the loop when i is 5
    print(i)
    
for i in range(1 , 11):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)  
    
#  Pass Statement
for i in range(1, 11):
    if i == 5:
        pass  # Do nothing when i is 5, just continue the loop
    print(i)