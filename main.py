import random 

print("Welcome to the game!")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]

print("What do you choose?")

player = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors --->\n"))

if player >= 3 or player < 0 :
    print("You typed an invalid number. Please recheck!")

else:

    print(images[player])
 
    random_int = random.randint(0, 2)

    print(f"Computer choose {random_int}---> ")

    print(images[player])

    if player == 0 and random_int == 2:
        print(f"Computer chose Scissors {scissors}. You WIN!")

    elif random_int == 0 and player == 2 :
        print("You lose!")

    elif random_int > player :
        print("You loose!")

    elif player > random_int :
        print("You win!")

    elif random_int == player :
        print("It's a draw.")


  
