import json
import os
from datetime import datetime

def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            return json.load(file)
    else:
        return []

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, task_description, task_priority, task_due_date):
    task = {
        'description': task_description,
        'priority': task_priority,
        'due_date': task_due_date,
        'completed': False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {task_description}")

def remove_task(tasks, task_index):
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number.")
        return
    removed_task = tasks.pop(task_index)
    save_tasks(tasks)
    print(f"Task removed: {removed_task['description']}")

def complete_task(tasks, task_index):
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number.")
        return
    tasks[task_index]['completed'] = True
    save_tasks(tasks)
    print(f"Task marked as completed: {tasks[task_index]['description']}")

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            status = "Done" if task['completed'] else "Not Done"
            print(f"{i + 1}. {task['description']} (Priority: {task['priority']}, Due Date: {task['due_date']}, Status: {status})")

def main():
    tasks = load_tasks()

    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Mark a task as completed")
        print("4. List tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task_description = input("Enter task description: ")
            task_priority = input("Enter task priority (high, medium, low): ")
            task_due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(tasks, task_description, task_priority, task_due_date)
        elif choice == '2':
            task_index = int(input("Enter the task number to remove: ")) - 1
            remove_task(tasks, task_index)
        elif choice == '3':
            task_index = int(input("Enter the task number to mark as completed: ")) - 1
            complete_task(tasks, task_index)
        elif choice == '4':
            display_tasks(tasks)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
