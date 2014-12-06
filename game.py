#!/usr/bin/python
import os

def main():
    print "Welcome to guess the number game\n==========================="
    print """
    Instructions:
    ------------
    1) Guess a number between 0 to 100.
    2) The game tells you how close you are to the guess.
    3) It would also tell you whether you have guess higher
       or lower than the previous guess.
    4) Continue until you guess it right!
    And you win... :-) Kudos!
    """

    num = 42
    guess = ""

    while guess != num:
        guess = int(raw_input("Take a guess: "))
        if guess < num:
            print "Guess higher next time\n"
        elif guess > num:
            print "Guess lower next time\n"
    print "CONGRATULATIONS!"

main()
