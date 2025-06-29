# Banker Roulette

'''
Figure out how to pick a random name from the list of friends.
'''

import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# First way
print(random.choice(friends))

# Second way
pick = random.randint(0,4)
print(friends[pick])