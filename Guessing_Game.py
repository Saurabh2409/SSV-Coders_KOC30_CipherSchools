# THE GUESSING GAME
# Group Name : SSV - Coders
# Section : KOC 30
# Group Members
    # Name              Roll no.    Reg no.
    # Muhammed Sinan    A 13        12218621
    # Saurabh Jaiswal   A 14        12218268
    # Vivek Sharma      A 15        12218279

'''
This a program designed for a guessing game. The program generates a random number between a range specified by the user.
The user is given three chances to guess the number. If the guess is correct the user is awarded with one point.
If all the three guesses go wrong the user looses the game. At the end the user is given an option to continue or exit the game.

'''


#replay
def replay(score):
    print("Next Session")
    min=int(input("Enter the minimum number of the range(integer only): "))
    max=int(input("Enter the maximum number of the range(integer only): "))
    randomnumber=ranger(min, max)
    print("The random number has been selected")
    print("You have 3 guesses")
    count=0
    sc=0
    newscore=game(randomnumber,sc,count)
    newscore=int(newscore)
    highscore=score+newscore
    return(highscore)

#range giver
def ranger(min,max):
    import random as r
    num=r.randint(min,max)
    return(num)

#game
def game(num,score,count):
    guess=int(input("Your Guess(input the integer number): "))
    while (count<4):
        if(guess==num):
            print("\nCongrats!! Your Guess was right")
            score=score+1
            print("You got 1 Point!!")
            return(ece(score))
            break
        elif(guess>num):
            print("Your Guess is bigger, try again\n")
            count=count+1
            break
        elif(guess<num):
            print("Your Guess is smaller, try again\n")
            count=count+1
            break
    if count == 3:
        print("You lost, the number was", num)
        return (ece(score))
    else:
        return(game(num, score, count))

#exit or contine
def ece(score):
    eorc = input("\nTo exit input(E) or To continue input(C): ")
    if eorc == "e" or eorc == "E":
        return(score)
    elif eorc == "c" or eorc == "C":
        return(replay(score))
    else:
        print("Invalid reply either enter E or C")
        return(ece(score))

#body
print("\nHello People!")
print("Welcome to the Guessing Game!")
input("Press ENTER to continue....\n")
print("Rules For the Game are:")
print("1.The player has to give a maximum number and a minimum number for the range(integers only)")
print("2.The player has to guess which number the computer is holding between the given range")
print("3.The player has 3 chances to guess the number")
print("4.If the player Guesses the number correctly ,the player will be rewarded with one point each\n")
input("If you have finished reading the rules press ENTER.....\n")
print("Lets Begin!\n")
print("Enter the Range:")
min=int(input("Enter the minimum number of the range(integer only): "))
max=int(input("Enter the maximum number of the range(integer only): "))
randomnumber=ranger(min,max)
print("\nThe random number has been selected\n")
print("You have 3 guesses\n")
sc=0
count=0
score=game(randomnumber,sc,count)
print("\nYour Total Score is",score)
print("Thank you for playing the Guessing Game\n")
