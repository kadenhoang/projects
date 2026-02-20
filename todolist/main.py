from task_manager import TaskManager
from utils import parse_date

def main():
    manager = TaskManager()
    manager.load_tasks()

    while True:
        print("\n=== TO-DO LIST MENU ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Tasks")
        print("5. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            title = input("Task title: ")
            desc = input("Description: ")
            due_date = parse_date(input("Due date (YYYY-MM-DD): "))
            timeframe = input("Timeframe (day/week/month/year): ").lower()
            reminder = parse_date(input("Reminder date/time (optional, press enter to skip): "), optional=True)
            manager.add_task(title, desc, due_date, timeframe, reminder)

        elif choice == "2":
            timeframe = input("View timeframe (day/week/month/year/all): ").lower()
            manager.view_tasks(timeframe)

        elif choice == "3":
            task_id = input("Enter task ID to mark complete: ")
            manager.complete_task(task_id)

        elif choice == "4":
            ids = input("Enter task IDs to delete (comma-separated): ")
            manager.delete_tasks(ids)

        elif choice == "5":
            manager.save_tasks()
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
