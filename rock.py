import random



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

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to the game of Rock ,Paper, or Scissors")
choice = input("Choose/ Type/ Rock, Paper, or Scissor\n").lower()

game = [rock, paper, scissor]
random_choice= random.choice(game)

if choice == "rock":
    print(game[0])
    print(random_choice)
    if random_choice == game[0]:
        print("Tie")
    elif random_choice ==game[1]:
        print("You Loose")
    else:
        print("You win")
elif choice == "paper":
    print(game[1])
    print(random_choice)
    if random_choice == game[0]:
        print("You Win")
    elif random_choice ==game[1]:
        print("Tie")
    else:
        print("You Loose")
else:
    print(game[2])
    print(random_choice)
    if random_choice == game[0]:
        print("You Loose")
    elif random_choice ==game[1]:
        print("You Win")
    else:
        print("Tie")

