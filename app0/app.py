import json
import os
from difflib import get_close_matches
def translate(word,data):
    """
    Three scenarios: 1. enter the exact word 
    2. enter a word that is close ---return the first of the list return by get_close_matches
    3. return empty list by get_close_matches
    """
    word=word.lower()
    if word in data:  #if you think the probablity that a user will enter an exact word is high, check this first
        return data[word]
    elif word.title() in data:#handle word like 'Texas"
        return data[word.title()]
    elif word.upper() in data: 
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        yn=input("Did you mean %s instead of? Enter Y if yes, or N if no: "%get_close_matches(word,data.keys())[0])
        
        if yn=="Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn=="N":
            return "The word doesn't exist, Please double check it."
            #w=input('please input correct word again: ')
            #return data[w]
        else:
            return "We didn't understand the entry."
    else:
        return "The word doesn't exist, Please double check it."
    
if os.path.exists('data.json'):
    data=json.load(open('data.json'))
    word=input('Enter word: ') 
    #what if the word is not in the data distionary
    output=translate(word,data)
    #Optimizing the final output
    if isinstance(output,list):
        for item in output:
            print(item)
    elif isinstance(output,str):
        print(output)
else:
    print("file does not exist")