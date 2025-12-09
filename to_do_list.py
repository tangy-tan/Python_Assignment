"""Simple To-Do List Manager"""

def add_task(todo_list, task):
    "Add a new task to the to-do list"
    todo_list.append({"task": task, "done": False})
    print(f"Task added: '{task}'")  
    return todo_list  

def view_tasks(todo_list):
    "Display all tasks"
    if not todo_list:
        print("Your to-do list is empty!")
        return
    
    for i, item in enumerate(todo_list, 1):
        status = "Done" if item["done"] else "Not Done"
        print(f"{i}. {item['task']}  --> {status}")

def mark_done(todo_list, task_number):
    "Mark a task as completed"
    if task_number < 1 or task_number > len(todo_list):
        print("Invalid task number!")
        return todo_list  
    
    if todo_list[task_number-1]["done"]:
        print("This task is already marked as done.")
    else:
        todo_list[task_number-1]["done"] = True
        print("Task marked as done.")
    return todo_list  
def delete_task(todo_list, task_number):
    "Remove a task from the list"
    if task_number < 1 or task_number > len(todo_list):
        print("Invalid task number!")
        return todo_list  
    
    removed = todo_list.pop(task_number-1)
    print(f"Task removed: {removed['task']}")
    return todo_list  

def main():
    "Main function to run the to-do list application"
    todo_list = []

    print("---Simple TO-DO List Manager---")

    while True:
        print("\nWhat would you like to do?")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark a task as done")
        print("4. Delete a task")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            task = input("Enter the task: ").strip()
            if task:  
                todo_list = add_task(todo_list, task)  
            else:
                print("Task cannot be empty!")
        
        elif choice == "2":
            view_tasks(todo_list)
        
        elif choice == "3":
            view_tasks(todo_list)
            if todo_list:
                try:
                    task_num = int(input("Enter task number to mark as done: "))
                    todo_list = mark_done(todo_list, task_num)  
                except ValueError:
                    print("Please enter a valid number!")
        
        elif choice == "4":
            view_tasks(todo_list)
            if todo_list:
                try:
                    task_num = int(input("Enter task number to delete: "))
                    todo_list = delete_task(todo_list, task_num)  
                except ValueError:
                    print("Please enter a valid number!")
        
        elif choice == "5":
            print("\nThank you for using Simple To-Do List Manager!")
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please enter a number between 1-5.")


if __name__ == "__main__":
    main()