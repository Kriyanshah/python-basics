#  Find the greatest of three numbers 

def greatest(a, b, c):
    if a > b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print(f"The greatest number is: {greatest(a, b, c)}")

# Write a program to convert celsius to fahrenheit

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius *9/5)+32
    return fahrenheit

celsius = float(input("Enter the temperature in celsius: "))
print(f"The temperature in fahrenheit is : {celsius_to_fahrenheit(celsius)}")
