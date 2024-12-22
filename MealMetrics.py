import numpy as py

import sqlite3

conn = sqlite3.connect('workout_meal.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS workouts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    workout_name TEXT,
    number_of_sets INTEGER,
    weight INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS meals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    meal_name TEXT,
    calories INTEGER
)
''')
conn.commit()

workout_list = {}

choice1 = int(input("Would you like to add a new workout? (Input 1 or 2) \n 1. Yes \n 2. No \n"))

if choice1 == 1:
    while choice1 == 1:
        num_workouts = int(input("Enter the number of workouts you want to add: "))
        if num_workouts < 20:
            for i in range(num_workouts):
                workout_name = input("Enter workout: ")
                sets = int(input("How many sets?: "))
                weight = int(input("How much weight?: "))

                cursor.execute('INSERT INTO workouts (workout_name, number_of_sets, weight) VALUES (?, ?, ?)',
                               (workout_name, sets, weight))
                conn.commit()

        print("Workouts added to database.")

        choice1 = int(input("Would you like to add more workouts? (Input 1 or 2) \n 1. Yes \n 2. No \n"))

elif choice1 == 2:
    choice2 = int(input("Would you like to add a meal? (Input 1 or 2) \n 1. Yes \n 2. No \n"))

    if choice2 == 1:
        num_entries = int(input("Enter the number of entries you want to add: "))
        if num_entries < 10:
            for i in range(num_entries):
                meal_name = input("Enter meal: ")
                calories = int(input("Enter calories: "))

                cursor.execute('INSERT INTO meals (meal_name, calories) VALUES (?, ?)',
                               (meal_name, calories))
                conn.commit()

            print("Meals added to database.")
        else:
            print("Number of additions is too high. Please input a smaller number.")
    else:
        print("Shutting down.")
else:
    print("Invalid input! Please input 1 or 2.")






cursor.execute('SELECT workout_name, number_of_sets, weight FROM workouts')
workouts = cursor.fetchall()


cursor.execute('SELECT meal_name, calories FROM meals')
meals = cursor.fetchall()

html_content = f'''
<html>
<head><title>Workout and Meal Tracker</title></head>
<body>
    <h1>Workout List</h1>
    <table border="1">
        <tr>
            <th>Workout Name</th>
            <th>Number of Sets</th>
            <th>Weight</th>
        </tr>
        {''.join(f'<tr><td>{w[0]}</td><td>{w[1]}</td><td>{w[2]}</td></tr>' for w in workouts)}
    </table>

    <h1>Meal List</h1>
    <table border="1">
        <tr>
            <th>Meal Name</th>
            <th>Calories</th>
        </tr>
        {''.join(f'<tr><td>{m[0]}</td><td>{m[1]}</td></tr>' for m in meals)}
    </table>
</body>
</html>
'''

with open('tracker.html', 'w') as file:
    file.write(html_content)

print("HTML file generated: tracker.html")


import webbrowser
import os

file_path = os.path.abspath('tracker.html')
webbrowser.open(f'file://{file_path}')

