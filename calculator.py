def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("--- Python Command Line Calculator ---")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    while True:
        choice = input("\nEnter choice (1/2/3/4) or 'q' to quit: ")

        if choice.lower() == 'q':
            print("Exiting calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid Input. Please choose a valid operation.")

if __name__ == "__main__":
    calculator()

#output
Select operation:
1. Add (+)
2. Subtract (-)
3. Multiply (*)
4. Divide (/)

Enter choice (1/2/3/4) or 'q' to quit:1
Enter first number: 10
Enter second number: 45
10.0 + 45.0 = 55.0

Enter choice (1/2/3/4) or 'q' to quit:2
Enter first number: 10
Enter second number: 66
10.0 - 66.0 = -56.0

Enter choice (1/2/3/4) or 'q' to quit: 3
Enter first number: 2
Enter second number: 8
2.0 * 8.0 = 16.0

Enter choice (1/2/3/4) or 'q' to quit: 4
Enter first number: 10
Enter second number: 10
10.0 / 10.0 = 1.0
