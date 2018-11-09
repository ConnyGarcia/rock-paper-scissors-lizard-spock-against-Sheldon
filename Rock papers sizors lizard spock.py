
# coding: utf-8

# In[46]:


import random
from skimage import io
import matplotlib.pyplot as plt

image = io.imread("https://zerode.files.wordpress.com/2010/09/432-sheldon-cooper-14945146-500-273.jpg")
defeat = io.imread("https://i.pinimg.com/originals/ec/cb/e2/eccbe21435c10a01b3ee01dd107762d9.jpg")


# In[47]:


def getPlayerChoice():
    while True: 
        choice = input("Sheldon: What is your choice?: ")

        if not choice.isnumeric(): 
            print("Sheldon: mI' neH!, that's klingon for numbers only")

        elif choice == '1':
            print("You picked Rock")
            break
        elif choice == '2':
            print("You picked Paper")
            break
        elif choice == '3':
            print("You picked Scissors")
            break
        elif choice == '4':
            print("You picked Lizard")
            break
        elif choice == '5':
            print("You picked Spock")
            break
        else:
            print("Sheldon: One cries because one is sad. For example, I cry because others are stupid, and that makes me sad.")
            print("")
    return choice


# In[48]:


def getCPUChoice():
    choice = random.randint(1,5)
    if choice == 1:
        print("Sheldon picked Rock")
    elif choice == 2:
        print("Sheldon picked Paper")
    elif choice == 3:
        print("Sheldon picked Scissors")
    elif choice == 4:
        print("Sheldon picked Lizard")
    elif choice == 5:
        print("Sheldon picked Spock")
    return choice


# In[49]:


flag = True
PlayerWon = 0 
ShellyWon = 0 
ties = 0 

playerChoice = 0
CPUChoice = 0
    
play = input("Sheldon: Would you like to play Rock, Paper, Scissors, Lizard, Spock(y/n): ").lower()
if play == "y" or play == "yes":
        print("")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Lizard")
        print("5. Spock")
        print("Sheldon: Scissors cuts paper, paper covers rock, rock crushes lizard,") 
        print("lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard,")
        print("lizard eats paper, paper disproves Spock, Spock vaporizes rock,") 
        print("and as it always has, rock crushes scissors.")
            
elif play != "n":
        print("")
        print("Sheldon: It's just yes or no, not rocket science. Let's just play")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Lizard")
        print("5. Spock")
    
elif play == "n" or play == "no":
        print("Sheldon: I knew you were afraid of my intellectual superiority and I didn't wated to play with you anyway")
        flag = False

while True: 

    if flag == False:
        break
    
    else: 
        print("")
        playerChoice = getPlayerChoice()
        playerChoice = int(playerChoice)
        CPUChoice = getCPUChoice()

        if playerChoice == 1 and (CPUChoice == 3 or CPUChoice == 4):
            print("Computer: Player wins")
            print("Sheldon: You mess with the bull, you get the horns. I'm about to show you just how horny I can be.")
            print("")
            PlayerWon += 1 
        elif playerChoice == 2 and (CPUChoice == 1 or CPUChoice == 5):
            print("Computer: Player wins")
            print("Sheldon: Oh you, like gravity, thou art a heartless bitch.")
            print("")
            PlayerWon += 1 
        elif playerChoice == 3 and (CPUChoice == 2 or CPUChoice == 4):
            print("Computer: Player wins")
            print("Sheldon: Very good. Chocolate?")
            print("")
            PlayerWon += 1 
        elif playerChoice == 4 and (CPUChoice == 2 or CPUChoice == 5):
            print("Computer: Player wins")
            print("Sheldon: You are he Green Goblin to my Spider-Man, the Pope Paul V to my Galileo, the Internet Explorer to my Firefox!")
            print("")
            PlayerWon += 1
        elif playerChoice == 5 and (CPUChoice == 1 or CPUChoice == 3):
            print("Computer: Player wins")
            print("Sheldon: (Crying) Mommy, I love you. Don't let Spock take me to the future!")
            print("")
            PlayerWon += 1
        elif playerChoice == CPUChoice:
            print("Tie")
            print("Sheldon: Must be the computer. What computer do you have? And please don't say a white one.")
            print("")
            ties += 1
        else:
            print("Computer: Sheldon wins")
            Shelldon_win = ["Sheldon: It must be humbling to suck on so many levels.", "Sheldon: Wow! I'm on fire.","Sheldon: I'm Dr. Sheldon Cooper, BS, MS, MA, PhD and ScD. OMG, right?", "Sheldon: I don't need to outrun the computer, I just need to outrun you, and I just did."]
            shelly = random.choice(Shelldon_win)
            print(shelly)
            print("")
            ShellyWon += 1 
        
        if PlayerWon + ShellyWon == 3: 
            print("")
            print("Player final score: ", PlayerWon)
            print("Sheldon final Score: ", ShellyWon)
            print("Total ties: ", ties)

            if PlayerWon > ShellyWon:
                plt.imshow(defeat)
                plt.show()
                break
            if ShellyWon > PlayerWon:
                plt.imshow(image)
                plt.show()
                break

