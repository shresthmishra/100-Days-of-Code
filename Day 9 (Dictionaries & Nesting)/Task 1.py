'''
* A dictionary in Python functions similarly to a dictionary in real life. 
* It's a data structure that allows us to associate a key to a value and pair the two pieces of data together.
* Dictionaries are mutable, meaning we can change them after their creation.
* Dictionaries are defined using curly braces {} with key-value pairs separated by commas.
* Each key is separated from its value by a colon (:).
* Keys must be unique and immutable (like strings, numbers, or tuples), while values can be of any data type and can be duplicated.
* We can access, add, modify, and delete items in a dictionary using their keys.
'''

# Creating a dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving a value from a dictionary
print("Bug's definition is:",programming_dictionary['Bug'])

# Adding more items to a dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Creating an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
