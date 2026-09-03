"""
factorial of 0 = 1
factorial of 1 = 1
factorial of 2 = 2x1
factorial of 3 = 3x2x1
factorial of 4 = 4x3x2x1
factorial of 5 = 5x4x3x2x1


factorial of n = n x (n-1) x (n-2) x (n-3) x .......... x 1
factorial of n = n x factorial of (n-1)
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
n = int(input("Enter your number: "))
print("The factorial of the number is :", factorial(n))