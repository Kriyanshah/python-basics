for i in range(0, 8): # for loop to print 0 to 7. Also can do range(8),its the same
    print(i)


# for loops iterate

l = [1, 2, 45, 56, 67] # for a list 

for i in l:
    print(i) # prints all the elements of list l

t = (1, 2, 3, 4, 5) # for a tuple
for i in t:
    print(i) # prints all the elements of tuple t

s = "Kriyan" # for a string
for i in s:
    print(i) # prints all the characters of string s


# for loops with else

l = [1, 2, 3, 4, 5]

for item in l:
    print(item)

else:
    print("done!") # else block will execute after the for loop is completed