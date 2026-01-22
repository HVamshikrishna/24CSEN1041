a = 9
b = 5


print("Arithmetic Operators")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")  
print(f"{a} % {b} = {a % b}\n")


print("Relational Operators")
print(f"{a} < {b} = {a < b}")
print(f"{a} > {b} = {a > b}")
print(f"{a} == {b} = {a == b}")
print(f"{a} != {b} = {a != b}\n")


print("Logical Operators")
print(f"AND {a} and {b} = {bool(a and b)}")
print(f"OR {a} or {b} = {bool(a or b)}")
print(f"NOT {a} = {not a}\n")


print("Bitwise Operators")
print(f"{a} & {b} = {a & b}")
print(f"{a} | {b} = {a | b}")
print(f"Bitwise XOR {a} ^ {b} = {a ^ b}")
print(f"Left Shift {a} << 2 = {a << 2}")
print(f"Right Shift {a} >> 2 = {a >> 2}")


print("\n" + ("a is greater than b" if a > b else "b is less than a"))

##output
Arithmetic Operators
10 + 99 = 109
10 - 99 = -89
10 * 99 = 990
10 / 99 = 0.10
10 % 99 = 10

Relational Operators
10 < 99 = True
10 > 99 = False
10 == 99 = False
10 != 99 = True

Logical Operators
AND 10 and 99 = True
OR 10 or 99 = True
NOT 10 = False

Bitwise Operators
10 & 99 = 2
10 | 99 = 107
Bitwise XOR 10 ^ 99 = 105
Left Shift 10 << 2 = 40
Right Shift 10 >> 2 = 2

b is less than a
