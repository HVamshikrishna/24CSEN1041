numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = []
odds = []

for n in numbers:
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)

print("Even numbers:", evens)
print("Odd numbers:", odds)
##output
Even numbers: [2, 4, 6, 8, 10]
Odd numbers: [1, 3, 5, 7, 9]
