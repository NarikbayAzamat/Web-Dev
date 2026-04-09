from storage import load_tasks, save_tasks
from models import Task
def show_menu():
    print("\n=== Task Manager ===")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")
def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"[{i}] {task}")
def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            title = input("Enter task: ").strip()
            if title:
                tasks.append(Task(title))
                save_tasks(tasks)
                print("Task added!")
            else:
                print("Task title cannot be empty.")
        elif choice == "3":
            show_tasks(tasks)
            try:
                index = int(input("Enter task ID to complete: ")) - 1
                if 0 <= index < len(tasks):
                    tasks[index].mark_completed()
                    save_tasks(tasks)
                    print("Task completed!")
                else:
                    print("Invalid task ID.")
            except ValueError:
                print("Please enter a number.")
        elif choice == "4":
            show_tasks(tasks)
            try:
                index = int(input("Enter task ID to delete: ")) - 1
                if 0 <= index < len(tasks):
                    tasks.pop(index)
                    save_tasks(tasks)
                    print("Task deleted!")
                else:
                    print("Invalid task ID.")
            except ValueError:
                print("Please enter a number.")
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Invalid option.")
if __name__ == "__main__":
    main()