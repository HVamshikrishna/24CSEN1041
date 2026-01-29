x = 10
y = 3

# 1. Arithmetic Operators
print(" Arithmetic Operators ")
print(x, "+", y, "=", x + y)     # Addition
print(x, "-", y, "=", x - y)     # Subtraction
print(x, "*", y, "=", x * y)     # Multiplication
# We use round() here to limit decimals to 2 places
print(x, "/", y, "=", round(x / y, 2))  # Division
print(x, "//", y, "=", x // y)   # Floor Division
print(x, "%", y, "=", x % y)     # Modulus
print(x, "**", y, "=", x ** y)   # Exponent
print("\n") # Prints a blank line

# 2. Assignment Operators
print(" Assignment Operators ")
a = 5
print("Start: a =", a)

a += 2
print("After a += 2:", a)

a *= 3
print("After a *= 3:", a)
print("\n")

# 3. Logical Operators
print(" Logical Operators ")
p = True
q = False

print("True and False =", p and q)
print("True or False  =", p or q)
print("not True       =", not p)
print("\n")

##output
Arithmetic Operators 
10 + 3 = 13
10 - 3 = 7
10 * 3 = 30
10 / 3 = 3.33
10 // 3 = 3
10 % 3 = 1
10 ** 3 = 1000


 Assignment Operators 
Start: a = 5
After a += 2: 7
After a *= 3: 21


 Logical Operators 
True and False = False
True or False  = True
not True       = False
