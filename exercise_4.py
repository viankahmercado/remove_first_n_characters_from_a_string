# Assignment 5:
# Do the exercise 1-15 in https://pynative.com/python-basic-exercise-for-beginners/
# Try do challenge yourself by not checking the "solution"

# Exercise 4: 
# Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.

# create a function to remove the characters
def remove_letter(any_word, n):
    print('Original string:', any_word)
    result = ''.join(any_word[i] for i in range(len(any_word)) if i >= n)
    return result

# ask user word input
inputted_word = input("Please enter a word: ")

#print result
