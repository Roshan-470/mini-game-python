import random

def game_result(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'snake' and computer == 'water') or \
         (user == 'water' and computer == 'gun') or \
         (user == 'gun' and computer == 'snake'):
        return "You win!"
    else:
        return "You lose!"

options = ['snake', 'water', 'gun']

print("Welcome to Snake, Water, Gun Game!")
print("Choose one: snake 🐍 | water 💧 | gun 🔫")

user_choice = input("Your choice: ").lower()

if user_choice not in options:
    print("Invalid input! Please choose snake, water, or gun.")
else:
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    result = game_result(user_choice, computer_choice)
    print(result)
