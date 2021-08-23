import json as js
from difflib import get_close_matches, SequenceMatcher
data = js.load(open("data.json"))

def print_line(string):
    for letter in range(50):
        print("-",end="")

def print_menu(mode):
    if mode=="main":
        string = "\nType a word to look for definition.\nType 'q' and press Enter to quit.\n"
        print_line(string)
        print(string)
    if mode=="word_search":
        string = "\n\nPress enter too look up for a next word:\nq - quit\n"
        print_line(string)
        print(string)

def look_up_word(word):
    word = word.lower()
    if word in data.keys():
        return data[word]
    else:
        closest_word = get_close_matches(word,  data.keys(), n=1, cutoff=0.70)
        if len(closest_word) > 0:
            while True:
                print(f'Did you mean: {closest_word[0]}?')
                user_conf = input("\nType 'y' if yes.\nType your word again if no.\nType 'q' to leave.\n")

                if user_conf.lower() == "q":
                    break
                if user_conf.lower() == "y":
                    return data[closest_word[0]]
                
                closest_word = get_close_matches(user_conf,  data.keys(), n=1, cutoff=0.70)

                if len(closest_word) == 0:
                    return "\nWord not found.\n"
        
    return "\nWord not found.\n"


def english_dict_app():
    print_menu("main")
    while True:
        user_word = input()
        if user_word.lower() == "q" or user_word.lower() == "quit":
            break

        output = look_up_word(user_word)

        if type(output) == list:
            for index, item in enumerate(output):
                print(index+1,". ", item, sep="")
        else:
            print(output)

        print_menu("word_search")



english_dict_app()

############################
## Backup of an old version of look_up_word
#def look_up_word(word):
#     word = word.lower()
#     if word in data.keys():
#         return data[word]
#     else:
#         closest_word = get_close_matches(word,  data.keys(), n=1, cutoff=0.70)
#         if len(closest_word) > 0:
#             print(f'Did you mean: {closest_word[0]}?')
#             yn = input("Type 'y' if yes. Type your word again if no.")
#             if yn.lower() == "y":
#                 return data[closest_word[0]]
            
            
#     return "Word not found."
