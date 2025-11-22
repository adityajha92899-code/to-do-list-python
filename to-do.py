todo_list = []

def show_menu():
    print("\n--- TO-DO LIST APP ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        todo_list.append(task)
        print("Task added.")

    elif choice == "2":
        if len(todo_list) == 0:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(todo_list):
                print(f"{i+1}. {t}")

    elif choice == "3":
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(todo_list):
            todo_list.pop(task_no - 1)
            print("Task deleted.")
        else:
            print("Invalid task number.")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")
