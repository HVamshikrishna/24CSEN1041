def is_prime(num):
    """Checks if a number is prime."""
    if num < 2:
        return False
    # Check for factors from 2 up to num - 1
    for i in range(2, num):
        if (num % i) == 0:
            return False  # Found a factor, not prime
    return True

primes = []
number_to_check = 2  # Start checking from the first prime number

# Keep looping until we have found 10 primes
while len(primes) < 10:
    if is_prime(number_to_check):
        primes.append(number_to_check)
    
    number_to_check += 1

print(f"The first 10 prime numbers are: {primes}")

##output
The first 10 prime numbers are: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
