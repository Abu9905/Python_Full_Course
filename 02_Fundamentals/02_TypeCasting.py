# =========== Type Casting =========== //

a = 31;

b = "34"; # String

d = 45645;

print(b)
print(type(b)) # Check the data type of b


print(a)
print(type(a)) # Check the data type of a

#  Convert b to an integer
c = int(b)
print(c)
print(type(c)) # Check the data type of c

# Convert Number to String

e = str(d)
print((e))

# Example:-

# ==== Converting String to Integer ==== //
num_str = "123";
print(num_str)
print(type(num_str))

num_str = int(num_str)  # Convert string to integer
print(num_str)
print(type(num_str))  # Check the data type after conversion

# ==== Converting Integer to String ==== //
num = 23;
print(num)
print(type(num))

num = str(num)  # Convert integer to string
print(num)
print(type(num))  # Check the data type after conversion

# ==== Converting Float to Integer ==== //
num_float = 34.56;
print(num_float)
print(type(num_float))

num_float = int(num_float)  # Convert float to integer
print(num_float)
print(type(num_float))  # Check the data type after conversion