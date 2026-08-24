# Q.1 write a program to write a table of a number given by user using loops


n = int(input("Enter your number: "))

for i in range(1,11):
    print(f" {n} x {i} = { n * i }")

# Q.2 in the given list greet only the person whose name start with k
        # list = [kriyan, kavy, taksh, prakshin, reet]
 
l = ["Kriyan", "Kavy", "Taksh", "Prakshin", "Reet"]
for i in range(0,5):
    
    if(l[i].startswith("K")):
        print("Greetings ", l[i])
    else:
        print("you are not worthy of greetings, get lost ",l[i])

# Q.3 perform Q.1 using while loop
n= int(input("Enter your number: "))
i=1
while(i<=10):
    print(F"{n} x {i} = {n * i}")
    i +=1

# Q.4 write a program to find the factorial of a no. given by user

n= int(input("Enter the number: "))
i=1
fact=1
while(i<=n):
    fact *= i
    i+=1
print(fact)

# Q.5 write a program to print following star pattern
"""  *  
    ***
   ***** for n = 3 """


n = int(input("enter the nunmber: "))
for i in range(1, n+1):
    print(" "*(n-i), end="")
    print("*"*(2*i-1), end="")
    print(" ")