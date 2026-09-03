# Function definition
def avg():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    average = (a + b + c) / 3
    print(f"Average of {a}, {b}, and {c} is: {average}")

# Function call
avg()

#Quick quiz
#write  a program to greet user with his name using function
def greet_user():
    name = input("Enter your name: ")
    print("hello", name, ", welcome to the world of python")

greet_user()

# fuunctions with arguments
def goodday(name, ending = "good day"):
    print("Good day", name)
    print(ending)
    return "Function completed"
a= goodday("kriyan", "thank you for using this program")
print(a)
b=goodday('taksh') # if ending is not provided then default value will be used which is "good day"
print(b)