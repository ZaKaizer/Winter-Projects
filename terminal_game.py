import random
winning_pair = {"Scissors":["Paper","Lizard"],"Paper":["Rock","Spock"],"Rock":["Lizard","Scissors"],
                "Lizard":["Spock","Paper"],"Spock":["Scissors","Spock"]}

Option_map = {1:"Rock",2:"Paper",3:"Scissors",4:"Lizard",5:"Spock"}

Running = 1
Pscore = 0
Cscore = 0

while(Running):
    print("""
          ================================================
                  Rock Paper Scissors Lizard Spock
          ================================================\v""")
    Pchoice = Option_map[int(input("""
                        1)Rock 🪨
                        2)Paper 📃
                        3)Scissors ✂️
                        4)Lizard 🦎
                        5)Spock 🖖\n"""))]
    Cchoice = Option_map[random.randint(1,5)]
    print("Player choice - " + Pchoice)
    print("Computer choice - " + Cchoice)
    if (Pchoice==Cchoice):
        print("It was a draw")
    elif Cchoice in winning_pair[Pchoice]:
        print("Player wins!")
        Pscore += 1
    else:
        print("Computer wins!")
        Cscore += 1
    playing = input("Would you like to play again? (Y-Yes,N-No): ")
    if (playing.lower()== "n"):
        Running =0

print(f"Player Score - {Pscore} || Computer Score - {Cscore}")