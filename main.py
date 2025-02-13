"""
words = file_contents.split()

word_counter = 0

for word in words:
    if word != " " :
        word_counter += 1

print(word_counter)

"""

def sort_chars(file):
    chars_dict = {}
    lower_case_file = file.lower()

    filtered_file = "".join([char for char in lower_case_file if char.isalpha()])

    for char in filtered_file:
        
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1

    return chars_dict
        
def main():  
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    sorted_dict = sort_chars(file_contents)

    #print(sorted_dict)

    for key in sorted_dict:
        print(f"The character '{key}' was found {sorted_dict[key]} times")    

import os
os.system('clear')
main()