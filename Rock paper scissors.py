import random
while True:
    print("\n")
    print("1) Rock")
    print("2) Paper")
    print("3) Scissors")
    selection = int(input("Enter Throw: "))
    
    if (selection == 1):
        player_throw = "Rock"
    elif (selection == 2):
        player_throw = "Paper"
    else:
        player_throw = "Scissors"

    
    print("\n")
    print("Player throws", player_throw)
    
    throws = ["Rock", "Paper", "Scissors"]
    ai_throw = random.choice(throws)

    # Output the ai_throw
    print("AI throws", ai_throw)
    

    if (player_throw == ai_throw):
        print("Tie Game!")
    elif (player_throw == "Rock"):
        if (ai_throw == "Paper"):
            print("AI Wins!")
        elif (ai_throw == "Scissors"):
            print("Player Wins!")
    elif (player_throw == "Paper"):
        if (ai_throw == "Scissors"):
            print("AI Wins!")
        elif (ai_throw == "Rock"):
            print("Player Wins!")
    elif (player_throw == "Scissors"):
        if (ai_throw == "Rock"):
            print("AI Wins!")
        elif (ai_throw == "Paper"):
            print("Player Wins!")

            
    print("\n")
    print("1) Play Again")
    print("2) Quit")
    selection = int(input("Enter Choice: "))


    if (selection == 2):
        break
