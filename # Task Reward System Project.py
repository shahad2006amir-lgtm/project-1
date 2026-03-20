# Task Reward System Project
# Project Owner: (Write Your Name Here)

print("--- 🎮 Welcome to the Task Achievement Game 🎮 ---")

task = input("What task did you complete today? ")

print("\nChoose your category to claim your reward:")
print("1- Study 📚")
print("2- Housework 🏠")
print("3- Others ✨")

choice = input("Enter category number (1, 2, or 3): ")

if choice == "1":
    print(f"Great job! Since you finished '{task}' in Study..")
    print("Reward: You earned a Blue Gem! 💎")
elif choice == "2":
    print(f"Awesome! Completing '{task}' in housework deserves a treat..")
    print("Reward: You earned a Chocolate bar! 🍫")
elif choice == "3":
    print(f"Excellent! Doing '{task}' is a great achievement..")
    print("Reward: You earned 100 Gold Coins! 💰")
else:
    print("Invalid choice, please run the program again and choose 1, 2, or 3.")

print("\nKeep up the great work! 💪")