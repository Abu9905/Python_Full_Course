# ==== Match Case ====
# Match case is a powerful feature introduced in Python 3.10 that allows for pattern matching.

# It provides a more readable and expressive way to handle complex conditional logic compared to traditional if-elif-else statements.

a = int(input("Enter a number between 1 and 10: "))

match a:
    case 1:
        print("You won a charger")
    case 3:
        print("You won a power bank")
    case 6:
        print("You won a laptop")
    case _:
        print("You won nothing")
    
# The match case statement checks the value of 'a' against various patterns.