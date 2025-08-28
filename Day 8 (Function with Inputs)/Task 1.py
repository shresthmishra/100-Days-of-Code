'''
# Task 1
Create a function called greet().
Write 3 print statements inside the function.
Call the greet() function and run your code.

# Inputs
By adding a variable name inside the parentheses when we create (define) a new function, it allows that function to take inputs when called.

That means we can modify how the function behaves each time by passing in different inputs.

# Creating the function
def myFunction(input):
    print(f"Hey! {input}")

# Using the function
myFunction("Tommy") 

# Will output "Hey! Tommy"

Inputs are Variables
When you create a function with inputs, you are defining a variable name that will be given to the data that is passed in.

The name of the input variable, e.g. name in this code here: def greet(name): is called the parameter.

The value of the value of the input variable, e.g. Angela when you call the previous greet function: greet("Angela") is called the argument.
'''

def greeting(name):
    print("Hello there!")
    print(f"It's nice to meet you, {name}!")
    print("See you later!")

greeting("Shresth")