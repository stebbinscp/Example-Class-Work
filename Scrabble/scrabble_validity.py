import scrabble_point_total
from itertools import permutations
import re

def letter_validity(letters):
    """Detemine if the letter inputs are valid, 
if not, returns False"""
    not_allowed = re.findall(r'[^A-z\,\ ]', letters)
    letters = list(letters)
    for char in letters:
        if char in not_allowed:
            oops = char
            print(f"Sorry, but {oops} is not a valid letter. Please try again.")
            return False

# print(letter_validity(letters))
def spaces_or_commas(letters):
    if letter_validity(letters) == None:
        letters_check = letters
        # print(re.match(r' ',letters))
        if re.match(r',',letters) != None :
            print("Commas!")
        # elif re.match(r'\s',letters) != None:
        #     # print("Spaces!")
        # else:
        #     # print("Joined!")
        letters_check = re.findall(r'[\w]', letters_check)
        letters_check = "".join(letters_check)
        # print(letters_check)
    return letters_check

# print(letters_check)
def file_open():
    file = open("scrabble_words.txt","r")
    text = []
    for line in file:
        text.append(re.findall(r'\w',line))
    text = [''.join(word) for word in text] # nested lists joined
    file.close()
    return text

def letter_permutations(letters_check,text):
    permutations_list = []
    for i in range(1,len(letters_check)+1):
        p = permutations(letters_check,i)
        # print(i)
        for perm in list(p):
            permutations_list.append(perm)
    permutations_list = [''.join(word) for word in permutations_list]
    final_list = []
    for i in range(0,len(permutations_list)):
        if permutations_list[i].upper() in text:
            final_list.append(permutations_list[i])
    return final_list
    # print(combinations_list)

def final_scores_sort(final_scored_list, final_list):
    dict = {}
    for i in range(0, len(final_list)):
        dict[final_list[i]] = final_scored_list[i]
    final_scored_list = sorted(final_scored_list, reverse=True)
    # print(final_scored_list)
    final_scored_sorted = []
    # print(len(final_scored_list))
    for number in final_scored_list:
        for tup in dict.items():
            (word,score) = tup
            if score == number:
                if tup not in final_scored_sorted:
                    final_scored_sorted.append(tup)
                    final_scored_list.remove(final_scored_list[0])
    return final_scored_sorted

def scrabble_output(final_scored_sorted, letters_check):
    output = ""
    # print(len(letters_check))
    for i in range(1,len(letters_check)+1): # from 1 to length of the word
        output = output + "\n" + f"\n{i} letter words" +"\n-----------"  # add to output the length of the word
        check_output = output
        count = 0
        for tup in final_scored_sorted:
            (word,score) = tup
            if len(word) == i:
                output = output + "\n" + f"{word}" + " - " + f"{score}"
                count += 1
            if count == 10:
                break
        if output == check_output:
            output = output + "\n" + f"No words of length {i}!"
    print(output)

def main():
    """Run the scrabble program"""
    letters = input("Please input your letters here:  ") #then try with spaces and with nothing
    if len(letters) < 1:
        print("Sorry, you didn't input anything! We can't work with this.")
    else: 
        letters_check = spaces_or_commas(letters)
        text = file_open()
        final_list = letter_permutations(letters_check,text)
        # print(final_list)
        # print(text)
        final_scored_list = scrabble_point_total.calculate_score(final_list) 
        # print(final_scored_list)
        final_scores_sorted = final_scores_sort(final_scored_list,final_list)
        scrabble_output(final_scores_sorted, letters_check)

if __name__ == "__main__":
    main()
