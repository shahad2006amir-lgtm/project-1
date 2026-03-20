# Task Reward System Project
# Project Owner: (Write Your Name Here)
print("--- 🎮 Welcome to the Task Achievement Game 🎮 ---")

# التعديل: إضافة متغير لجمع النقاط
total_points = 0

task = input("What task did you complete today? ")

print("\nChoose your category to claim your reward:")
print("1- Study 📚")
print("2- Housework 🏠")
print("3- Others ✨")

choice = input("Enter category number (1, 2, or 3): ")

if choice == "1":
    print(f"Great job! Since you finished '{task}' in Study..")
    print("Reward: You earned a Blue Gem! 💎")
    total_points += 50 # أضفتِ 50 نقطة
elif choice == "2":
    print(f"Awesome! Completing '{task}' in housework deserves a treat..")
    print("Reward: You earned a Chocolate bar! 🍫")
    total_points += 30 # أضفتِ 30 نقطة
elif choice == "3":
    print(f"Excellent! Doing '{task}' is a great achievement..")
    print("Reward: You earned 100 Gold Coins! 💰")
    total_points += 20 # أضفتِ 20 نقطة
else:
    print("Invalid choice!")

# عرض مجموع النقاط النهائي
print(f"\n🏆 Your current total score is: {total_points} Points!")
print("Keep up the great work! 💪")
