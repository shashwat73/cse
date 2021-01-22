def count_occurrences(a,b):
    counter = 0
    for check in a:
        if(check == b):
            counter+=1
    return counter
word = input("Enter a word:")
letter = input("Enter a letter:")

print count_occurrences(word, letter)
