age = int(input("Enter your age: "))

# if elif else ladder
if(age%2==0): # if (condition):
    print("your age is even")

if(age>= 18 and age< 100 ): # if (condition):
    print("you are an adult")
    print("nice for you")           # both the ifs are independent and elif and else depend on 2nd if

elif(age<0 or age>100):   # elif for more than 1 conditon
    print("you are entering a wrong age")

else:     
    print("this place is not for you ")
    print("get lost")    

print("END OF PROGRAM")