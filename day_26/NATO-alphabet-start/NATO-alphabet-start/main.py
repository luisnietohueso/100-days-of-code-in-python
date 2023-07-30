
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas as pd

# TODO 1. Create a dictionary in this format:
# Create a dictionary comprehension to map the letter to its corresponding code
data_dictionary = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dictionary = {value.letter: value.code for (letter, value) in data_dictionary.iterrows()}
print(nato_dictionary)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
code = input('Which word do you want to convert into phonetic code words? ')
# Create a dictionary comprehension to map each letter of the word to its corresponding phonetic code
phonetic = {letter: nato_dictionary[letter.upper()] for letter in code if letter.upper() in nato_dictionary}
print(phonetic)
