import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_choose=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
cpu_choose=random.randint(0,2)
if player_choose >= 3 or player_choose < 0:
    print("You typed an invalid number. You lose!")

#rock
if player_choose==0:
    print(rock)
    print("Computer chose:")
    if cpu_choose==0:
        print(rock)
        print("It's a draw")
    elif cpu_choose==1:
        print(paper)
        print("You lose")
    else:
        print(scissors)
        print("You win!")

#paper
if player_choose==1:
    print(paper)
    print("Computer chose:")
    if cpu_choose==0:
        print(rock)
        print("You win!")
    elif cpu_choose==1:
        print(paper)
        print("It's a draw")
    else:
        print(scissors)
        print("You lose")

#scissors
if player_choose == 2:
    print(scissors)
    print("Computer chose:")
    if cpu_choose == 0:
        print(rock)
        print("You lose")
    elif cpu_choose == 1:
        print(paper)
        print("You win!")
    else:
        print(scissors)
        print("It's a draw")
