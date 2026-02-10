# Write a shell script that takes a list of numbers as input, identifies all the prime numbers in the list, and outputs the prime numbers in ascending order. 

# Additionally, the script should:

# Handle input validation to ensure only numbers are processed.

# Allow the user to enter the numbers separated by spaces.

# input:
# 23 45 17 4 20 29 11 3

# output:

# Prime numbers in ascending order:
# 3 11 17 23 29



#num = [23, 45, 17, 4, 20, 29, 11, 3]
num = [int(x) for x in input("Enter the numbers ").split() ]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [x for x in sorted(num) if is_prime(x)]
print("prime numbers: ", primes)
     