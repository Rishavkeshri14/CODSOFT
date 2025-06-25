import random

# Define possible choices
choices = ['rock', 'paper', 'scissors']

# Initialize scores
user_score = 0
computer_score = 0
round_number = 1

print("🎮 Welcome to Rock, Paper, Scissors!")
print("Instructions: Type 'rock', 'paper', or 'scissors' to play.\n")

# Game loop
while True:
    print(f"\n🔁 Round {round_number}")
    
    # Get user's choice
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

    # Validate user input
    if user_choice not in choices:
        print("❌ Invalid choice! Please try again.")
        continue

    # Computer's random choice
    computer_choice = random.choice(choices)
    
    print(f"🧍 You chose: {user_choice}")
    print(f"💻 Computer chose: {computer_choice}")

    # Determine winner
    if user_choice == computer_choice:
        print("🤝 It's a tie!")
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        print("✅ You win this round!")
        user_score += 1
    else:
        print("❌ Computer wins this round!")
        computer_score += 1

    # Show current score
    print(f"🏆 Score => You: {user_score} | Computer: {computer_score}")

    # Ask to play again
    play_again = input("\nDo you want to play another round? (yes/no): ").lower()
    if play_again != 'yes':
        print("\n🎉 Final Score:")
        print(f"   You: {user_score}")
        print(f"   Computer: {computer_score}")
        print("👋 Thanks for playing!")
        break

    round_number += 1
