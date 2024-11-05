
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as file:
    names=file.readlines()

with open("Input/Letters/starting_letter.txt") as file:
    starting_letter=file.read()

for name in names:
    name=name.strip()
    s=starting_letter.replace("[name]", name)
    with open(f"Output/ReadyToSend/letter_for_{name}.docx", "w") as file:
        file.write(s)