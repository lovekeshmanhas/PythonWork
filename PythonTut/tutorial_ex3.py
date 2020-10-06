# guess the hidden number
# number of guess for one persion is 9
# Print pending guess
# Game over in case of guess count over

numberOfGuess = 9
print("Total number of guess: ", numberOfGuess)
hiddenNumber = 34
while(True):
    if numberOfGuess > 0:
        inputNumber = int(input("Please guess the number "))
        if inputNumber == hiddenNumber:
            print("You are the winner")
            break
        elif inputNumber > hiddenNumber:
            print("Your number is greater then actual number")
            numberOfGuess = numberOfGuess -1
            print("Pending Guess: ", numberOfGuess)
            continue
        else:
            print("Your number is smaller then actual number")
            numberOfGuess = numberOfGuess - 1
            print("Pending Guess: ", numberOfGuess)
            continue
    else:
        print("Game over")
        break

