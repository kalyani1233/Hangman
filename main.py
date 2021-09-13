import random

def hangman():
    word = random.choice(["thor","avengers","loki","apple","sinchan","banana","hulk"])
    validletters = "abcdefghijklmnopqrstuvwxyz"
    turns=10
    guessmade = ''

    while len(word)>0: # word=thor  4
        main = ''
        for letter in word: # t  h o r
            if letter in guessmade:
                main=main+letter
            else:
                main = main +"_" + " "     #  - - - -
        if main == word:
            print(main)
            print("You win!!")
            break
        else:

            print("Guess word",main)
            guess=input()
        if guess in validletters:
            guessmade =guessmade+guess
        else:
            print("Enter a valid character:")
            guess=input()
        if guess not in word:
            turns=turns-1
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break




while(True):
    name=input("Enter your name:")
    print(f"Welcome {name}")
    print("---------------------")
    print("Try to guess the word less than 10 turns!!")
    hangman()
    print()
    con=input("Do you want to play again type yes/no:")
    if con=="no" or con=="No":
        break
    else:
        continue
