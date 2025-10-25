# -------------------------------------------------------
# Name       : Anshuman Jha
# Date       : 15 October 2025
# Project    : Daily Calorie Tracker
# -------------------------------------------------------
# Description:
# This program helps users track their daily calorie intake.
# It allows entering meal names and calorie values, calculates
# total and average calories, compares intake with a daily limit,
# and optionally saves the session log to a text file.
# -------------------------------------------------------

# Task 1: Setup & Introduction

print("==============================================")
print("   Welcome to Daily Calorie Tracker ")
print("==============================================")
print("This tool helps you log your meals, calculate total & average calories,\nand compare them with your daily calorie limit.")

# Task 2: Input & Data Collection

meals=[]
calories=[]

n=int(input("How many meals do you want to enter? "))
for i in range(1,n+1):
    print(f"Meal #{i}")
    m = input("Meal name: ")
    c = float(input("Calories amount: "))
    
    meals.append(m)
    calories.append(c)

print("Meals list:", meals)
print("Calories list:", calories)

# Task 3: Calorie Calculations

total_calories = sum(calories)
average_calories = total_calories / len(calories)

daily_limit = float(input("Enter your daily calorie limit: "))

# Task 4: Exceed Limit Warning System

if(total_calories > daily_limit):
    print("Warning: You have exceeded your daily calorie limit!")
else:
    print("Great job! You are within your daily calorie limit.")

# Task 5: Neatly Formatted Output

print("==============================================")
print("              DAILY SUMMARY REPORT           ")
print("==============================================")

print("\nMeal Name\t\tCalories")
print("----------------------------------------------")

for i in range(len(meals)):
    print(f"{meals[i]:<20}{calories[i]}")
    

print(f"{'Total:':<20}{total_calories:.2f}")
print(f"{'Average:':<20}{average_calories:.2f}")
print("----------------------------------------------")

# Task 6 (Bonus): Save Session Log to File

s = input("\nDo you want to save this session log to a file? (y/n): ")
if s.lower() == "y":
    from datetime import datetime
    timestamp = datetime.now()
    
    with open("calorie_log.txt", "a") as file:
        file.write("\n=========================================\n")
        file.write(f"Calorie Tracker Session - {timestamp}\n")
        file.write("-----------------------------------------\n")
        for i in range(n):
            file.write(f"{meals[i]:<20}{calories[i]}\n")
        file.write(f"Total calories: {total_calories}\n")
        file.write(f"Average calories: {average_calories:.2f}\n")
        if total_calories > daily_limit:
            file.write("Status: Exceeded daily limit\n")
        else:
            file.write("Status: Within daily limit\n")
    print("✅ Session log saved to calorie_log.txt")

