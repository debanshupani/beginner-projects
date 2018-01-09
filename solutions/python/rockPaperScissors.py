import random

user = 0
comp = 0
moves = ["rock","paper","scissor"]
moves_pref = [0,1,2]

def play():
    global user
    global comp
    user_move = input("rock, paper or scissor? ")
    try:
        user_move = moves_pref[moves.index(user_move)]
        comp_move = random.choice(moves_pref)
    except ValueError:
        print("Please type only rock, paper or scissor.")
        return 1

    print("My move: ",moves[comp_move])
    if(user_move == comp_move):
        print("That' s a tie!")
    elif(user_move == 0 and comp_move == 2):
        user+=1
        print("You win!")
    elif(user_move == 1 and comp_move == 0):
        user+=1
        print("You win!")
    elif(user_move == 2 and comp_move == 1):
        user+=1
        print("You win!")
    else:
        comp+=1
        print("I win!")

counter = "y"
while(True):
    if(counter == "score"):
        print("The score is:\nYou\tMe\n"+str(user)+"\t"+str(comp))
        counter = input("Do you want to play again? (Y/N) ")
    if(counter == "n" or counter == "N"):
        break
    elif(counter == "y" or counter == "Y"):
        play()
        counter = input("Do you want to play again? (Y/N)\nAt any time, type 'score'for the score. ")
    else:
        print("Dude, it was a yes/no question.")
        counter = input("Do you want to play again? (Y/N)\nAt any time, type 'score'for the score. ")
    print("\n\n")