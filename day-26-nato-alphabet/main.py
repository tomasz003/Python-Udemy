import pandas

alphabet_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict={row.letter:row.code for (index, row) in alphabet_dataframe.iterrows()}

username=input("What's your name?\n").upper()
namelist=[alphabet_dict[letter] for letter in username]
print(namelist)
