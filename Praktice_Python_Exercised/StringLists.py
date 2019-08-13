#Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

word = input("Please enter a word :")
word = str(word)

reverse_word=word[::-1]

if word == reverse_word:
    print("This word is palindrome")

else:
    print("This word is not palindrome! ")





