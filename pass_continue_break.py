numbers = [1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for n in numbers:
    if n == 100:
        print("Error: Found invalid data (100). Aborting!")
        break  # STOP everything
    
    elif n % 2 == 0:
        continue  # SKIP even numbers
        
    elif n == 1:
        pass      # Do NOTHING special for 1, just let it proceed
        
    print(f"odd number: {n}")
  ##output
odd number: 1
odd number: 3
odd number: 5
odd number: 7
odd number: 9
odd number: 11
odd number: 13
odd number: 15
odd number: 17
odd number: 19
