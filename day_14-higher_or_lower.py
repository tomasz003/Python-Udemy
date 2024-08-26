
from game_data(day_14) import data
import random

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

def a_or_an(word):
    vowels = ["a", "e", "i", "o", "u"]
    if word[0].lower() in vowels:
        return "an"
    else:
        return "a"


def check(option_a, option_b, decision):
    if option_a["follower_count"]>option_b["follower_count"] and decision=="A":
        return 1
    elif option_a["follower_count"]<option_b["follower_count"] and decision=="B":
        return True
    else:
        return False

def game(compare_a, compare_b, points):
    prefix_a=a_or_an(compare_a["description"])
    prefix_b=a_or_an(compare_b["description"])

    print(f'Compare A: {compare_a["name"]}, {prefix_a} {compare_a["description"].lower()}, from {compare_a["country"]}.')
    print(vs)
    print(f'Against B: {compare_b["name"]}, {prefix_b} {compare_b["description"].lower()}, from {compare_b["country"]}.')

    choice=input("Who has more followers? Type 'A' or 'B': ").upper()

    if check(compare_a, compare_b, choice):
        points+=1
        print("\n"*20)
        print(f"You're right! Current score: {points}.")
        compare_a=compare_b
        compare_b=random.choice(data)
        while compare_b==compare_a:
            compare_b = random.choice(data)
        game(compare_a, compare_b, points)
    else:
        print(f"Sorry, that's wrong. Final score: {points}")

obj_a = random.choice(data)
obj_b = random.choice(data)
while obj_b==obj_a:
    obj_b = random.choice(data)

print(logo)
game(obj_a, obj_b, 0)
