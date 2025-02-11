with open("books/frankenstein.txt") as f:
    file_contents = f.read()

words = file_contents.split()

word_counter = 0

for word in words:
    if word != " " :
        word_counter += 1

print(word_counter)