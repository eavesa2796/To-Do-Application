# Overview

# In this project, you will build a functional To-Do List Application using Python from scratch. This assignment will help you strengthen your understanding of Python concepts such as syntax, data types, control structures, functions, and error handling, all while creating a practical, interactive command-line application.

# Project

# In VS Code, create a .py file and complete the following requirements:

# User Interface (UI) and Storage Method

# Build a simple Command Line Interface (CLI) that welcomes users and displays a menu with options to add, view, delete tasks, or quit the application.
# The tasks should be stored in a Python list
# Core Features

# Add tasks
# View tasks
# Delete tasks
# Quit the application
# User Interaction

# Use input() to capture user selections and ensure proper input validation to handle invalid choices.
# Error Handling

# Implement error handling using try, except, else, and finally blocks to catch errors
# Alert the user if they provide invalid input
# Alert the user if there are no tasks to view
# Alert the user if they try to delete a task that doesn't exist
# Alert the user if they select an option on the main menu that doesn't exist
# Code Organization

# Organize your code into functions to improve clarity and maintainability. 
# Use descriptive function names and add comments/docstrings where necessary.
# Testing and Debugging

# Thoroughly test your application, considering edge cases such as empty lists and invalid input.
# Ensure that all features (adding, viewing, deleting tasks) work as expected.
# Verify that error messages are displayed appropriately for invalid actions.
# Test the application's behavior when quitting to ensure it exits gracefully.

# End of Project

def main():
    tasks = []

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Quit")

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            task = input("Enter the task: ")
            tasks.append(task)
            print(f"Task '{task}' added successfully.")
        elif choice == 2:
            if not tasks:
                print("No tasks to display.")
            else:
                print("Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
        elif choice == 3:
            if not tasks:
                print("No tasks to delete.")
            else:
                try:
                    task_num = int(input("Enter the task number to delete: "))
                    if 1 <= task_num <= len(tasks):
                        removed_task = tasks.pop(task_num - 1)
                        print(f"Task '{removed_task}' deleted successfully.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Invalid input. Please enter a valid task number.")
        elif choice == 4:
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")     
    
if __name__ == "__main__":
    main()