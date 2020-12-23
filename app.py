import json
from difflib import get_close_matches

data = json.load(open("application1\data.json"))

#print(type(data))
#print(data)

def dic(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data: 
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        ans = input("Did you mean %s? Y or N: "%get_close_matches(word,data.keys())[0]) 
        ans = ans.upper()
        if ans == "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif ans == "N":
            return "Sorry we couldn't find the word!!"
        else:
            return "Sorry we could'nt understand your entry!!"
    else:
        return "Word not found!!\nPlease re-check!!"

w = input("Search: ")

out = dic(w)

if type(out) == list:
    for item in out:
        print("\n",item)
else:
    print(out)