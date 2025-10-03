# Functions with input

# Positional Arguments
def greet_with_name(name, greeting):
    print(f"{greeting}, {name}.")

greet_with_name("Shresth", "Howdy") #Output: Howdy, Shresth.


# Keyword Arguments
def greet_with_location(name, location):
    print(f"Hello there, {name}.")
    print(f"How's it like in {location}?")

greet_with_location(name="Shresth", location="Singrauli")