
import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def changing_ace(player_deck):
    for card in player_deck:
        if sum(player_deck) > 21 and card==11:
            player_deck[player_deck.index(card)]=1
    return player_deck

def sum_check(player_deck):
    if sum(player_deck)==21 and len(player_deck)==2:
        return 1
    elif sum(player_deck)>21:
        return -1
    else:
        return 0

def draw_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def winner_check(deck1, deck2):
    if sum_check(deck1)==-1:
        print(f"\tYour final hand: {deck1}, final score: {sum(deck1)}")
        print(f"\tComputer's final hand: {deck2}, final score: {sum(deck2)}")
        print("You went over. You lose 😭")
    else:
        while sum(deck2) < 17:
            deck2.append(draw_card())
            changing_ace(deck2)

        print(f"\tYour final hand: {deck1}, final score: {sum(deck1)}")
        print(f"\tComputer's final hand: {deck2}, final score: {sum(deck2)}")
        if sum_check(deck2)==-1:
            print("Opponent went over. You win 😁")
        else:
            user_sum = sum(deck1)
            computer_sum = sum(deck2)
            if user_sum>computer_sum:
                print("You win 😃")
            elif user_sum<computer_sum:
                print("You lose 😤")
            else:
                print("Draw 🙃")


def blackjack():
    print(logo)

    user_deck=[]
    computer_deck=[]

    user_deck.append(draw_card())
    user_deck.append(draw_card())
    computer_deck.append(draw_card())
    computer_deck.append(draw_card())
    changing_ace(user_deck)
    changing_ace(computer_deck)

    print(f"\tYour cards: {user_deck}, current score: {sum(user_deck)}")

    if sum_check(computer_deck)==1:
        print(f"\tComputer's deck: {computer_deck}")
        print("Lose, opponent has Blackjack 😱")
        return 0

    print(f"\tComputer's first card: {computer_deck[0]}")
    if sum_check(user_deck)==1:
        print("Win with a Blackjack 😎")
        return 0

    while sum_check(user_deck)==0:
        wanna_draw=input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if wanna_draw=='y':
            user_deck.append(draw_card())
            changing_ace(user_deck)
            if sum_check(user_deck)==-1:
                winner_check(user_deck, computer_deck)
                return 0
            print(f"\tYour cards: {user_deck}, current score: {sum(user_deck)}")
            print(f"\tComputer's first card: {computer_deck[0]}")
        else:
            winner_check(user_deck, computer_deck)
            return 0


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()=='y':
    print()
    blackjack()
