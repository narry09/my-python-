import math
def primes_count(num):
    if num < 2:
        return 0  # No primes less than 2

    primes = [2]  # Start with 2 as the first prime number
    x = 3  # Start checking from 3 (since 2 is already in primes)

    while x <= num:
        for y in range(3,x,2):  # Check divisibility up to sqrt(x)
            if x % y == 0:  # If divisible, it's not a prime
                break
        else:
            primes.append(x)  # If no divisors found, x is prime, append it to the list

        x += 2  # Increment by 2 (only odd numbers after 2)

    print(primes)
    return len(primes)  # Return the count of prime numbers

# Test the function
  # Should return 25
print(primes_count(25))
