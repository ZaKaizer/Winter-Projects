import random
winning_pair = {"Scissors":["Paper","Lizard"],"Paper":["Rock","Spock"],"Rock":["Lizard","Scissors"],
                "Lizard":["Spock","Paper"],"Spock":["Scissors","Spock"]}

Option_map = {1:"Rock",2:"Paper",3:"Scissors",4:"Lizard",5:"Spock"}
Pchoice = Option_map[int(input("""
                        1)Rock 🪨
                        2)Paper 📃
                        3)Scissors ✂️
                        4)Lizard 🦎
                        5)Spock 🖖\n"""))]
print(Pchoice)
