# lists can store more than 1 datatypes and are mutable
games = ["rdr2", "codm", "minecraft", "valo", 7.88, "rohan"]

print(games[0])

games[0]= "sekiro"
print(games)

#  methods

games.append("kriyan") # adds the string kriyan at the end of the list
print(games)

l1 = [1, 2, 7, 45, 56, 22]
l1.sort() # arranges list numbers in increasing order
l1.reverse() # starts from the end of the list 
l1.insert(3, 9090) # inserts 9090 at index 3
l1.pop(2) # removes the value at index 2 and it will return value at index 2 if you use it in print()
l1.remove(45) # removes 45 from the list
print(l1)

fruits =[]
f1 = input("enter the fruit :")
fruits.append(f1)
f2 = input("enter the fruit :")
fruits.append(f2)
f3 = input("enter the fruit :")
fruits.append(f3)
f4 = input("enter the fruit :")
fruits.append(f4)
f5 = input("enter the fruit :")
fruits.append(f5)
f6 = input("enter the fruit :")
fruits.append(f6)
f7 = input("enter the fruit :")
fruits.append(f7)

print(fruits)