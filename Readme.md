"Simple To-Do List Manager"
This is a CLI-based Python project for the Introduction to Python Programming course.
This program allows users to manage a simple to-do list through the terminal.

Features
1)Add new task
2)View all activities
3)Mark a task as completed
4)Delete a task

-->Simple text-based menu
-->Runs entirely in the terminal

How to Run the Program
1)Make sure that Python is installed on your system.
2)Clone or download this repository.
3)Open the folder in your terminal.
4)Run the command below:
python3 todo.py
(or python depending on your system)

Functions Used in the Project

1. add_task(todo_list, task)
   Adds a new task to the list.
   Each problem has:
   a task name
   a status (done or not done)
2. view_tasks(todo_list)
   Displays all tasks with their number and completion status.
3. mark_done(todo_list, task_number)
   Marks a selected task as completed.
4. delete_task(todo_list, task_number)
   Removes a task from the list by number.
5. main()
   This is the main function that:
   Shows the menu
   Takes User Input
   Calls other functions
   Keeps the program running until the user exits.

Description of the Project
The project is a simple, text-based to-do list manager.
It uses:
Lists
Dictionaries
Functions
Loops
Basic input and output
This follows the requirement to have one main function and at least four other functions.
