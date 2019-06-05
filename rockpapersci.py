import random
print("Choose: Rock, Paper or Scissors?")
choice = input("> ").lower()
options = ['Rock', 'Paper', 'Scissors']
computer = random.choice(options)
if choice == 'rock':
    if computer == 'Scissors':
        print("You Win!")
    elif computer == 'Rock':
        print("It's a Tie")
    else:
        print("You Lose")
if choice == 'paper':
    if computer == 'Rock':
        print('You win!')
    elif options == 'Paper':
        print("It's a Tie!")
    else:
        print("You Lose")
if choice == 'scissors':
    if computer == 'Paper':
        print("You Win!")
    elif computer == 'Scissors':
        print("It's a Tie")
    else:
        print("You Lose")
if choice == 'shoot':
    print("You Win!")
