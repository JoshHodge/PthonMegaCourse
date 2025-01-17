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
    elif get_close_matches(word, dkeys, cutoff=0.6)[0] != "":
        NewWord = get_close_matches(word, dkeys)[0]
        return ("Did you mean: " + NewWord + "? \n" + "The definition for " + NewWord + " is: " + str(data[NewWord.lower()]).strip('[]'))
    else: return "Word does not exist"

WordToDef = (input("Please enter a word to search for: \n"))
output = Def_word(WordToDef)

if type(output) == list:
    for item in output:
        print(item)
else: print(output)
