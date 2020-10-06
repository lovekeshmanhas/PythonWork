# Snake water gun
import random
lst = ["Snake", "Water", "Gun"]
global computer_winCount
global player_winCount
i = 1
computer_winCount =0
player_winCount=0
while(i <= 10):
    input_Player = input("Please enter s for snake, w for water and g for Gun: ").upper()
    choice = random.choice(lst)
    if (input_Player == "S") and (choice == "Water"):
        print("Computer choose: ",choice)
        player_winCount = player_winCount + 1
        print("Player win ", player_winCount)
    elif (input_Player == "S") and (choice == "Gun"):
        print("Computer choose: ", choice)
        computer_winCount = computer_winCount + 1
        print("Computer win ", computer_winCount)
    elif (input_Player == "W") and (choice == "Snake"):
        print("Computer choose: ", choice)
        computer_winCount = computer_winCount + 1
        print("Computer win ", computer_winCount)
    elif (input_Player == "W") and (choice == "Gun"):
        print("Computer choose: ", choice)
        player_winCount = player_winCount + 1
        print("Player win ", player_winCount)
    elif (input_Player == "G") and (choice == "Snake"):
        print("Computer choose: ", choice)
        player_winCount = player_winCount + 1
        print("Player win ",player_winCount)
    elif (input_Player == "G") and (choice == "Water"):
        print("Computer choose: ", choice)
        computer_winCount = computer_winCount + 1
        print("Computer win ",computer_winCount)
    else:
        print("Computer choose: ", choice)
        print("Draw match")


    i = i + 1

if(computer_winCount > player_winCount):
    print("Computer win this game")
elif(computer_winCount == player_winCount):
    print("Match draw")
else:
    print("Player win this game")


#print(choice)