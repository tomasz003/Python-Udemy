import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password=''
password_list=[]

for i in range (0, nr_letters):
    #x=random.randint(0,len(letters)-1)
    x=random.choice(letters)
    password_list.append(x)

for i in range(0, nr_symbols):
    x=random.choice(symbols)
    password_list.append(x)

for i in range(0, nr_numbers):
    x=random.choice(numbers)
    password_list.append(x)

print(password_list)

#easier - sorted
for i in password_list:
    password+=i
print(f"Your password is {password}")

#harder - not sorted
password=''
# for i in range (0, len(password_list)):
#     x=random.randint(0, len(password_list)-1)
#     password+=password_list.pop(x)
random.shuffle(password_list)
for i in password_list:
    password+=i
print(f"Your password is {password}")
