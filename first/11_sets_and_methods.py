s = {1, 3, 5, 7, 5, "harry", 5, 9} # a set

empty_set = set() # empty set, dont use e={} as it will create an empty dictionary

print(s, type(s)) # prints the set and its type


# METHODS
s.add(11) # adds 11 to the set s
print(s) # prints the updated set
'''s.clear() # clears the set s
print(s)'''


"""sets are mutable and unordered, they store data in unique values
    it is unindexed (cannot be accessed by index) and
     cannot contain duplicate values and the values cant be changed"""

# operations on sets

print(len(s)) # length of the set
s.remove("harry") # removes harry from the set
# s.pop() # removes a random element from the set

# union and intersection

s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 7, 8}

print(s1.union(s2)) # the union of both sets
print(s1.intersection(s2)) # the intersection of both the sets
# and other methods of sets








