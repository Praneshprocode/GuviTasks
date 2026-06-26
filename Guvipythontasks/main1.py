#Unscramble a jumbled word
import random
words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']
word = random.choice(words)
letters = list(word)
random.shuffle(letters)
jumbled_word = "".join(letters)
print("Unscramble..", jumbled_word)
while True:
    guess = input("Guess: ")
    if guess.lower() != word.lower():
        print("Incorrect try again")
    else:
        break
print("You won")