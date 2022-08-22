from replit import clear
from art import logo
## Get bid price and name
print(logo)
print("Welcome to the secret auction")
bids = {}
bidding_finished = False
while not bidding_finished:
  name = input("Whats your name?\n")
  price = int(input("Whats your bid?\n $"))
  bids[name] = price
  other_users = input("Are there any other bidders? 'yes' or 'no'.\n")
  if other_users == 'yes':
    clear()
    bidding_finished = False
  elif other_users == 'no':
    highest_bid = max(bids, key=bids.get)
    max_bid = max(dict.values(bids))
    print("The highest bidder was " + highest_bid + f" with {max_bid}$")
    bidding_finished = True
  else:
    print("Error please make sure you right correctly")
