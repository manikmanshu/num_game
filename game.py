#!/usr/bin/python
import os

def main():
    print "Welcome to guess the number\n==========================="

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
