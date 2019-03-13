import json
import difflib
from difflib import get_close_matches
from difflib import SequenceMatcher
"""
This function is used to search for a particular word and return the result from the dictionary data set
"""
data = json.load(open("076 data.json"))
dkeys = data.keys() #get data keys from dictionary

def Def_word(word):
    if word in dkeys:
        return data[word.lower()]
    elif get_close_matches(word, dkeys)[0] != "":
        return ("Did you mean: " + get_close_matches(word, dkeys)[0] + '?')
    else: return "Word does not exist"
    
WordToDef = (input("Please enter a word to search for: \n"))
print(Def_word(WordToDef))
