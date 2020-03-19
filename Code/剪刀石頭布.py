import random
player_win=0
computer_win=0
while(True):
    computer=random.randrange(1,4)
    if((player_win-computer_win)==3):
        print("You won more than two times")
        break
    elif((computer_win-player_win)==3):
        print("The computer won more than two times")
        break
    else:
        print(computer)
        player=int(input("scissor(1), rock(2), paper(3): "))
        if((player==3 and computer==2) or (player==2 and computer==1) or (player==1 and computer==3)):
            print("You won")
            player_win+=1
        elif(player==computer):
            print("Tie")
        else:
            print("You lost")
            computer_win+=1