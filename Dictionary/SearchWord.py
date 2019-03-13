import json
import difflib
from difflib import get_close_matches
"""
This function is used to search for a particular word and return the result from the dictionary data set
"""
data = json.load(open("076 data.json"))
dkeys = data.keys() #get data kays from dictionary

def Def_word(word):
    if word in dkeys:
        return data[word.lower()]
    else: return "Word does not exist"

WordToDef = (input("Please enter a word to search for: \n"))
print(Def_word(WordToDef))
