from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
print("Welcome to the secret auction program")

end_bid = False
Bid_Collection = {}
while not end_bid:
  
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  Bid_Collection[name] = int(bid)
  anyone = input("Are there any other bidders? Type 'yes' or 'no'").lower()
  if anyone == 'yes':
    clear()
    end_bid = False
  else:
     end_bid = True

# print(Bid_Collection)

max_value = 0
max_name = ""
for item in Bid_Collection:
  value = Bid_Collection[item]
  if value >= max_value:
    max_value = value
    max_name = item


# print(max_value)
# print(max_name)

print(f"\nThe winner is {max_name} with the bid of ${max_value}.")