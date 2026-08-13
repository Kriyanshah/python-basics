marks = {
    "kriyan": 100, 
    "aksh": 60,
    "taksh": 33,
}
print(marks.items()) # prints the (key,value) pairs in the form of tuples
print(marks.keys()) # prints the keys of the dictionary
print(marks.values()) # prints the values of the dictionary
marks.update({"taksh": 32, "soumya": 87}) # updates the value of key taksh to 32 and adds a new key soumya with value 87\
print(marks) # prints the updated dictionary


"""print(marks.get("shubham"))  prints none as shubham is not present in the dictionary
print(marks["shubham"])  throws an error as shubham is not present in the dictionary"""