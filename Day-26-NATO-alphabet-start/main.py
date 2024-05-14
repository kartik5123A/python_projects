import pandas


#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# print(data.to_dict())

data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

output_list = []   

def NATO_phonetic_alphabet():

    #TODO 2. Create a list of the phonetic code words from a word that the user inputs.

    input_word = input("Enter a word : ").upper()

    try:
        output_list = [data_dict[letter] for letter in input_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        NATO_phonetic_alphabet()
    else:
        print(output_list)  

NATO_phonetic_alphabet() 