#The code specifies the function "primeNumberDigitPrinter", which accepts a string as input and returns an array of single digit prime numbers in the string. Before adding a number to the output array, the method utilizes the helper function "isPrime" to determine if it is prime.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primeNumberDigitPrinter(string):
    result = []
    for char in string:
        if char.isdigit() and int(char) < 10:
            if is_prime(int(char)):
                result.append(int(char))
    return result

print(primeNumberDigitPrinter("abc2134kd31")) # Output: [2,3,3]
