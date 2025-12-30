import art

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

print(art.logo)
print("Welcome to the Secret Auction!")
biddersLeft = True
bids = {}
while biddersLeft:
    name = input("What is your name? ")
    bid = int(input("What amount will you bid? $"))
    bids[name] = bid
    decider = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if decider == 'no':
        biddersLeft = False
    else:
        print("\n" * 10)
print(f"{max(bids)} has the greatest bid of amount ${bids[max(bids)]}.")
