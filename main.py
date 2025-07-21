print("Welcome to HealthyHabits Tracker!")
print("Track your daily healthy habits easily.")
import json
from datetime import date, timedelta
def log_habits():
    habits = {
        1: "Drink water",
        2: "Sleep before 10 PM",
        3: "20+ min of exercise",
        4: "Ate fruits or veggies",
        5: "Read a book"
    }
    print("What habits did you do today?")
    for number, habit in habits.items():
        print(f"{number}. {habit}")
    habit_numbers = input("Enter the numbers of the habits you did today (e.g., 1 3 5): ")
    selected_habits = []
    for number in habit_numbers.split():
        try:
            number = int(number)
            if number in habits:
                selected_habits.append(habits[number])
            else:
                print(f"Invalid habit number: {number}")
        except ValueError:
            print("Invalid input. Please enter numbers separated by spaces.")
            return
    today = date.today().strftime("%Y-%m-%d")
    log_data = {today: selected_habits}
    try:
        with open("log.json", "r") as f:
            existing_data = json.load(f)
    except FileNotFoundError:
        existing_data = {}
    existing_data.update(log_data)
    with open("log.json", "w") as f:
        json.dump(existing_data, f, indent=4)
    print("Habits logged successfully!")
def view_habit_history():
    try:
        with open("log.json", "r") as f:
            habit_data = json.load(f)
    except FileNotFoundError:
        print("No habit data found.")
        return
    print("--- Habit History ---")
    for date, habits in habit_data.items():
        print(f"{date}: {', '.join(habits)}")
def view_weekly_summary():
    try:
        with open("log.json", "r") as f:
            habit_data = json.load(f)
    except FileNotFoundError:
        print("No habit data found.")
        return
    today = date.today()
    weekly_data = {}
    for i in range(7):
        current_date = today - timedelta(days=i)
        date_str = current_date.strftime("%Y-%m-%d")
        weekly_data[date_str] = len(habit_data.get(date_str, []))
    print("--- Weekly Summary ---")
    for date_str, count in weekly_data.items():
        print(f"{date_str}: {count} habits")
    best_day = max(weekly_data, key=weekly_data.get)
    worst_day = min(weekly_data, key=weekly_data.get)
    print(f"Best day: {best_day} ({weekly_data[best_day]} habits)")
    print(f"Worst day: {worst_day} ({weekly_data[worst_day]} habits)")
def main():
    while True:
        print("\nMain menu:")
        print("1. Log today's habits")
        print("2. View habit history")
        print("3. View weekly summary")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            log_habits()
        elif choice == "2":
            view_habit_history()
        elif choice == "3":
            view_weekly_summary()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
    import matplotlib.pyplot as plt
    dates = ['Jun 14', 'Jun 15', 'Jun 16']
    habit_counts = [2, 3, 1]
    plt.bar(dates, habit_counts)
    plt.title("Habits Tracked Per Day")
    plt.ylabel("Number of Habits")
    plt.show()
    while True:
        print("Welcome to HealthyHabits Tracker!")
        print("1. Log today's habits")
        print("2. View habit history")
        print("3. View weekly summary")
        print("4. Show weekly chart")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Logging habits...")
        elif choice == '2':
            print("Viewing history...")
        elif choice == '3':
            print("Viewing summary...")
        elif choice == '4':
            print("Showing chart...")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")
    import random

    tips = [
        "Get up and stretch every hour.",
        "Drink water instead of soda today.",
        "Try to sleep and wake at the same time each day."
    ]

    print(" Tip of the Day:")
    print(random.choice(tips))
