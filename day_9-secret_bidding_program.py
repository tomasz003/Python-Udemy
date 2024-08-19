
from art import logo
print(logo)

auction_over=False
all_bids={}

while auction_over==False:
    name=input("What is your name?: ")
    bid=int(input("What is your bid?: $"))
    all_bids[name]=bid

    want_more_bids=input("Are there any other bidders? Type 'yes or 'no'. ").lower()
    if want_more_bids=='no':
        auction_over=True

    print("\n" * 20)


max_bid=0
winner=''

for person in all_bids:
    if all_bids[person]>max_bid:
        max_bid=all_bids[person]
        winner=person
#winner=max(all_bids, key=all_bids.get)

print(f"The winner is {winner} with a bid of ${max_bid}")
