import random
print("\n ✨Welcome to the Rock 🪨 Paper 📄 Scissors ✂️ Game.✨ \n")

choices={"rock":"🪨","paper":"📄","scissor":"✂️"}
user_score = computer_score = 0

print("🎲 Let's play Rock, Paper, Scissors with a twist! 🎉 (Type 'q' to quit)")

while True:
  user = input("👉 Your move (rock/paper/scissors): ").lower()
  if user == 'q':
    print(f"🏆 Final Score - You: {user_score} | Computer: {computer_score}")
    print("👋 Nice Play! Thanks for playing.")
    break
    if user not in choices:
        print("⚠️ Invalid choice! Try again.")
        continue
  computer = random.choice(list(choices))
  print(f"🤖 Computer chose: {choices[computer]} {computer}")

  if user == computer:
      print("🤝 It's a tie!")
  elif (user == "rock" and computer == "scissors") or \
        (user == "paper" and computer == "rock") or \
        (user == "scissors" and computer == "paper"):
        user_score += 1
        print("🎉 You win this round!")
  else:
        computer_score += 1
        print("💀 You lose this round!")

  print(f"📊 Score: You {user_score} - {computer_score} Computer\n")