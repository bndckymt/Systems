def display_biceps():
    art = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⠿⡏⢿⡟⠿⠁⢸⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⣀⣀⡀⢠⣶⠶⠀⠁⣽⣿⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠘⣿⣿⣷⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀  ⠀⠀⠀⠀⢹⣿⣿⣿⣆⠀⠀⠀⠀
⠀⠀⢀⣠⣴⣶⣶⣶⣦⣄⠀⠀ ⠀⠀⢀⣀⣀⣀⠀⠀⠀⣼⣿⣿⣿⣿⣧⠀⠀⠀
⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣐⢾⣿⣿⣿⣿⣷⣦⣌⡻⣿⣿⣿⣿⣿⣧⠀⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⡇⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢋⡉⠛⠿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⡇⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⡏⢠⣿⣿⣷⡦⠀⣈⣉⣀⣤⣶⣿⣟⣛⠛⠛⠛⠛⠃⠀
⠀⣿⣿⣿⣿⣿⣿⣿⡿⠀⠾⠛⠋⠁⠐⠺⠿⠿⠿⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⣿⣿⠟⢁⣴⣶⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⠿⠋⣰⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠛⠛⠋⠁⠐⠛⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    print(art)

display_biceps()

print("---------------------------------------------")
print("\t GAIN MASTER (your gym guide/planner)")
print("---------------------------------------------\n")
 
name = input("Enter Your Name: ")
print(f"Welcome to GAIN MASTER {name}!")

workouts = {
    'm': {
        'name': 'Push Day: Chest, Triceps, Shoulders',
        'exercises': {
            'Chest': ['Dumbbell Chest Press 3x12', 'Incline Dumbbell Press 3x12', 'Chest Fly 3x12'],
            'Triceps': ['Tricep Pushdown 3x12', 'Overhead Dumbbell Extension 3x12', 'Skull Crusher 3x12'],
            'Shoulders': ['Dumbbell Shoulder Press 3x12', 'Lateral Raises 3x12', 'Rear Delt Fly 3x12']
        }
    },
    't': {
        'name': 'Pull Day: Back, Biceps, Forearms',
        'exercises': {
            'Back': ['Pull-ups 3x12', 'Lat Pulldowns 3x12', 'Deadlifts 3x12'],
            'Biceps': ['Dumbbell Bicep Curls 3x12', 'Hammer Curls 3x12', 'Preacher Curls 3x12'],
            'Forearms': ['Wrist Curls 3x12', 'Wrist Extensions 3x12', 'Forearm Curls 3x12']
        }
    },
    'w': {
        'name': 'Leg Day: Quads, Hamstrings, Calves',
        'exercises': {
            'Quads': ['Squats 3x12', 'Leg Press 3x12', 'Leg Extensions 3x12'],
            'Hamstrings': ['Deadlifts 3x12', 'Leg Curls 3x12', 'Glute-Ham Raises 3x12'],
            'Calves': ['Calf Raises 3x12', 'Seated Calf Raises 3x12', 'Calf Press 3x12']
        }
    },
    'th': {
        'name': 'Active Rest Day',
        'exercises': {
            'cardio':['Light Jogging 30 minutes', 'Walkings 30 minutes']
        }
    },
    'f': {
        'name': 'Push Day: Chest, Triceps, Shoulders',
        'exercises': {
            'Chest': ['Bench Press 3x12', 'Incline Bench Press 3x12', 'Chest Fly 3x12'],
            'Triceps': ['Tricep Pushdown 3x12', 'Overhead Dumbbell Extension 3x12', 'Skull Crusher 3x12'],
            'Shoulders': ['Dumbbell Shoulder Press 3x12', 'Lateral Raises 3x12', 'Rear Delt Fly 3x12']
        }
    },
    's': {
        'name': 'Pull Day: Back, Biceps, Forearms',
        'exercises': {
            'Back': ['Pull-ups 3x12', 'Lat Pulldowns 3x12', 'Deadlifts 3x12'],
            'Biceps': ['Dumbbell Bicep Curls 3x12', 'Hammer Curls 3x12', 'Preacher Curls 3x12'],
            'Forearms': ['Wrist Curls 3x12', 'Wrist Extensions 3x12', 'Forearm Curls 3x12']
        }
    },
    'su': {
        'name': 'Rest Day, Core',
        'exercises': {
            'Core': ['Plank 3x60s', 'Russian Twists 3x12', 'Leg Raises 3x12']
        }
    }
}

# Initialize progress tracker
progress = {
    'm': False,
    't': False,
    'w': False,
    'th': False,
    'f': False,
    's': False,
    'su': False,
}

def display_workout(day):
    #Display the workout for the selected day.
    day = day.lower()
    if day in workouts:
        print("Workout for", day.capitalize() + ":")
        print(workouts[day]['name'])
        for muscle_group, exercises in workouts[day]['exercises'].items():
            print(muscle_group + ":")
            for exercise in exercises:
                print("-", exercise)
    else:
        print("Invalid day. Please enter a valid day (M, T, W, TH, F, S, SU).")

def track_progress():
    #Display progress and update the tracker.
    print("Track Your Progress:")
    for day in progress:
        if progress[day]:
            print(day.capitalize() + ": Completed")
        else:
            print(day.capitalize() + ": Not Completed")

    day = input("Enter day you completed (or 'none' to skip): ").lower()
    if day in progress:
        progress[day] = True
        print("Progress for", day.capitalize(), "updated!")
    elif day == 'none':
        print("No progress recorded.")
    else:
        print("Invalid day. Progress not updated.")

def main():
    #Main function to run the workout planner.
    while True:
        print("\nWeekly Workout Planner")
        print("1. Display Workout")
        print("2. Track Progress")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            day = input("Enter the day of the week (M, T, W, TH, F, S, SU): ")
            display_workout(day)
        elif choice == '2':
            track_progress()
        elif choice == '3':
            print("Exiting the planner.")
            break
        else:
            print("Invalid choice. Please choose again.")

main()