def number_system_converter():
    print("--- Number System Converter ---")
    
    try:
        # 1. Ask for the Decimal Number
        decimal_num = int(input("Enter a Decimal Number: "))
        
        # 2. Ask for the Target Base
        print("\nChoose a target base:")
        print(" 2 -> Binary")
        print(" 8 -> Octal")
        print("16 -> Hexadecimal")
        base = int(input("Enter Base (2, 8, or 16): "))

        print("-" * 30)

        # 3. Perform the conversion based on user input
        if base == 2:
            # bin() returns string like '0b101', slice [2:] removes '0b'
            result = bin(decimal_num)[2:]
            print(f"Decimal {decimal_num} in Binary is: {result}")
            
        elif base == 8:
            # oct() returns string like '0o12', slice [2:] removes '0o'
            result = oct(decimal_num)[2:]
            print(f"Decimal {decimal_num} in Octal is: {result}")
            
        elif base == 16:
            # hex() returns string like '0xa', slice [2:] removes '0x'
            result = hex(decimal_num)[2:].upper()
            print(f"Decimal {decimal_num} in Hexadecimal is: {result}")
            
        else:
            print("Invalid Base! Please choose 2, 8, or 16.")

    except ValueError:
        print("Error: Please enter valid whole numbers only.")

# Run the program
if __name__ == "__main__":
    number_system_converter()

#output
Enter a Decimal Number: 2025727457

Choose a target base:
 2 -> Binary
 8 -> Octal
16 -> Hexadecimal
Enter Base (2, 8, or 16): 2

Decimal 2025727457 in Binary is: 1111000101111100010010111100001
Enter a Decimal Number: 2025727457

Choose a target base:
 2 -> Binary
 8 -> Octal
16 -> Hexadecimal
Enter Base (2, 8, or 16): 8
------------------------------
Decimal 2025727457 in Octal is: 17057422741

Enter a Decimal Number: 2025727457

Choose a target base:
 2 -> Binary
 8 -> Octal
16 -> Hexadecimal
Enter Base (2, 8, or 16): 16
------------------------------
Decimal 2025727457 in Hexadecimal is: 78BE25E1
