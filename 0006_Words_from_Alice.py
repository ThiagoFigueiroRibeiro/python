# 0006 - Words from Alice - In this program, we are given a Alice.txt full of text. In it,
# we use RegEx (Regular Expression) to find strings that matches our wishes. 
# For instance, I'll upload an aditional file called "Alice.txt" in which there is the 
# full text of Lewis Carroll's "Alice’s Adventures in Wonderland" 
# From it, we will print every word that has the following format: 4 to 7 letters + '-' + 5 to 7 letters,
# like "frog-footman".
# This code was made using "Automate the Boring Stuff with Python" By Al Sweigart.

import re       # Importing the RegEx library.

f = open("Alice.txt", "r")      # Opening the Alice.txt

wordRegex = re.compile(r'\w{4,7}-\w{5,7}')      # Using RegEx to get us words with 4 to 7 letters + '-' + 5 to 7 letters

print (wordRegex.findall(f.read()))     # Print our results.