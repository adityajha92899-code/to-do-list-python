def add_task(tasks):
    task = input("Enter the task description: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully.")

def view_tasks(tasks):
    print("\n--- Your Tasks ---")
    if not tasks:
        print("Your to-do list is empty.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def main():
    tasks = []
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
