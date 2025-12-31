def number_system_converter():
    print("--- Number System Converter ---")
    
    try:
        
        decimal_num = int(input("Enter a Decimal Number: "))
        
       
        print("\nChoose a target base:")
        print(" 2 is Binary")
        print(" 8 is Octal")
        print("16 is Hexadecimal")
        base = int(input("Enter Base (2, 8, or 16): "))

        print("-" * 30)

       
        if base == 2:
          
            result = bin(decimal_num)[2:]
            print(f"Decimal {decimal_num} in Binary is: {result}")
            
        elif base == 8:
            
            result = oct(decimal_num)[2:]
            print(f"Decimal {decimal_num} in Octal is: {result}")
            
        elif base == 16:
            
            result = hex(decimal_num)[2:].upper()
            print(f"Decimal {decimal_num} in Hexadecimal is: {result}")
            
        else:
            print("Invalid Base! Please choose 2, 8, or 16.")

    except ValueError:
        print("Error: Please enter valid whole numbers only.")


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
