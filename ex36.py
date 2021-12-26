# Author: Kevin Johnson
# Created: DEC 24 2021

# I don't have time to make a game right now

# ok, how about one where I choose to study or take care of my kid?

# choose study and > 5 hours, die, too long, kid starved
# study < 5 hours, ok, better to take care of kid, branch to kid
# choose kid and is hungry, choose feed, play, or study
# feed kid, is happy
# play, kid is happy but starved
# study, branch to study

from sys import exit

def dead(why):
    print(why, "Good job!")
    exit(0)

def study():
    print("stub for study function")
    print("Okay, how many hours will you study?")
    kid_hungry = False

    while True:
        choice = input("> ")
        choice_int = int(choice)

        if choice_int < 5:
            print("Ok, time to check kid.")
            feed_kid()
        elif choice_int > 5:
            dead("You studied too long and your kid starved.")
        else:
            print("IDK what that means")

def feed_kid():
    print("Is your kid hungry?")

    choice = input("> ")

    if choice == "yes":
        print("You feed your kid and go back to studying.")
        study()
    elif choice == "no":
        print("Kid is okay, go back to studying.")
        study()
    else:
        print("IDK what that means")

def start():
    print("You need to study to get a better job, but you also need to take care of your kid.")
    print("You are at home, your laptop is there, with which you use to study.")
    print("You are also home with your kid, who needs to eat and play.")
    print("Do you study or feed your kid?")

    choice = input("> ")

    if choice == "study":
        study()
    elif choice == "feed kid":
        feed_kid()
    else:
        dead("Your kid starves, then you starve.")

start()