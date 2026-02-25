from task_manager2 import Task_Manager

def main():

    print("Menu:")
    print("1. add task.")
    print("2. show task.")
    print("3. mark complete.")
    print("4. delete task.")

    while True:
        try:
            c = int(input("Choose an action: "))
        except ValueError:
            print("The choice should be a number.")
            continue
            
        match c:
            case 1:
                id = int(input("Task ID: "))
                title = input("What is your task?: ")
                description = input("task description: ")
                due_date = input("Due date: ")
                Task_Manager.add_task(id,title,description,due_date)
                print("task is successfully added!")
            
            case 2:
                Task_Manager.view_tasks()

            case 3:
                id = int(input("Task ID: "))
                mark = input("mark as completed?(Y/N): ")
                if mark == "Y":
                    completed = True
                else:
                    completed = False
                Task_Manager.complete_task(id,completed)
        
if __name__ == "__main__":
    main()