import random

Goal = random.randint(0,20)

for i in range(0,5):
    print "Guess a number form 1 to 10, TO FIND OUT THE ANSWER!"
    Guess = raw_input("Please enter a number you guess: ")
    Guess = int(Guess)

    if Guess < Goal:
        print "Sorry, too low to the answer."
  

    if Guess > Goal:
        print "Sorry, too high to the answer."
 

    if Guess == Goal:
        print "Great you got it! Thank you for playing!"
        exit()
    

keystroke = raw_input("press enter to continue .")
