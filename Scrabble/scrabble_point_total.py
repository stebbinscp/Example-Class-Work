
def read_txt(filename):
    """Read in file and select only the first three letters"""
    import re # import regex
    file = open(filename, "r")  # open file
    text = [] # initiate empty list
    for line in file:
        text.append(re.findall(r'^[A-z]{3}',line)) 
        # append only the regex pattern
    txt = [''.join(word) for word in text] 
    # for each individual list in the list
    # join the nested list all together to form one string
    file.close()
    # print(txt) # sanity check
    return txt


def calculate_score(txt):
    """Calculate the score of each word using a dictionary"""
    tile_score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
            "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
            "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
            "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
            "x": 8, "z": 10}
    total_list = [] # initite empty list
    for i in range(0,len(txt)): # loop over every word
        # print(tile)
        word = txt[i].lower() # lowercase to match dict
        # print(word)
        total = 0 # start the total as 0 every time
        for char in word: # nested for loop
            # print(char)
            total = total + tile_score.get(char)
                # add to the total each time
            # print(tile_score.get(char))
            # print(total)
        total_list.append(total) # append the value to the total list
        # print(total_list)
    return(total_list)

# print(calculate_score(txt))

def main():
    filename = "3_letter_words.txt"
    txt = read_txt(filename)
    list_scores = (calculate_score(txt))
    file = open("3_letter_words_sorted.txt", "w")
    dict_two = {}
    list_two = []
    for i in range(0,len(txt)): # append the key value pair to the dict
        dict_two[txt[i]] = list_scores[i]
    list_scores = sorted(list_scores, reverse=True)
    for tup in dict_two.items():
        list_two.append(tup)
    list_two = sorted(list_two, reverse=True, key=lambda x: x[1])
    list_two.remove(list_two[len(list_two)-1])
    # print(list_two)
    for tup in list_two:
        (word,score) = tup
        file.write(f"\n {word} --> {score} ")
    file.close()
    # print(dict_two)

if __name__ == "__main__":
    main()