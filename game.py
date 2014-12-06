#!/usr/bin/python
import os
import random

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

    play_again = 'y'
    while play_again == 'y':
        num = random.random()*100 // 1
        guess = ""

        while guess != num:
            guess = int(raw_input("Take a guess: "))
            if guess < num:
                print "Guess higher next time\n"
            elif guess > num:
                print "Guess lower next time\n"
        print "Voila! You got it!\nNow you know the deep secrets of life, universe and everything...\n"

        play_again = raw_input("Wanna play again (y/n): ")
        if play_again == 'n':
            print "Bye..."
            break
main()
