# Guess the numer Task :
import random      # importing the random module
num = random.randint(1, 20) # random number in the range of 1 to 20
guess =int (input("Guess the number:")) 
attempt =1
# looping is used for multiple attempts
while guess != num:
    # conditional statement is used to check whether the required condition is met or not
    if guess > num:
        print (" you guessed too high")
    else :
        print (" you guessed too low")
    guess = int(input ("Guess the number again:"))
    attempt +=1

print ("Correct ,you won the game")
