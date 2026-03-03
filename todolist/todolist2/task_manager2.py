from utils2 import date_format

class Task_Manager:
    def __init__(self, id, title, description, due_date, completed = False):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed

    @classmethod
    def add_task(cls, id, title, description, due_date):
        valid_date = date_format(due_date)
    
        # Convert datetime to string for storage
        due_date_str = valid_date.strftime("%Y-%m-%d")
        task = Task_Manager(id, title, description, due_date_str)
        with open("tasks.txt", "a") as file:
            file.write(f"{task.id}|{task.title}|{task.description}|{task.due_date}|{task.completed}\n")
            #all the fields after being written in the file become string data

    @classmethod    
    def view_tasks(cls):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("Empty List")
            for task in tasks:
                id, title, description, due_date, completed = task.strip().split("|")
                status = "✔" if completed == "True" else "✗"
                print(f"{status} | ID: {id} | Title: {title}, Description: {description}, Due Date: {due_date}")
                

    # Delete task by id
    @classmethod
    def delete_tasks(cls, id):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        # Rewrite the file without the deleted task
        with (open("tasks.txt", "w") as file):
            for task in tasks:
                if not task.startswith(f"{id}"):
                    file.write(task)

    @classmethod
    def complete_task(cls, id,completed):
        with (open("tasks.txt", "r") as file):
            tasks = file.readlines()
        with (open("tasks.txt", "w") as file):
            for task in tasks:
                saved_id, title, description, due_date, _ = task.strip().split("|")
                #even though the complete field is not needed, unpacking a tuple or list must match the number of elements
                # use '_' (throwaway value) if the value is not needed, the unpack still match the elements
                if saved_id == str(id):
                        file.write(f"{saved_id}|{title}|{description}|{due_date}|{str(completed)}\n")
                else:
                    file.write(task)

    @classmethod
    def edit_task(cls,id):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        task_found = False
        updated_tasks = []

        for task in tasks:
            saved_id, title, description, due_date, completed = task.strip().split("|")

            if saved_id == str(id):
                task_found = True

                print("\nCurrent Task: ")
                print(f"1. Title       : {title}")
                print(f"2. Description : {description}")
                print(f"3. Due Date    : {due_date}")
                print("4. Finish editing")

                while True:
                    try:
                        choice = int(input("Choose field to edit(1-4): "))
                    except ValueError:
                        print("Enter option as integer")
                        continue

                    match choice: 

                        case 1:
                            new_title = input("Edit title: ").strip()
                            if new_title:
                                title = new_title

                        case 2:
                            new_description = input("Edit description: ").strip()
                            if new_description:
                                description = new_description

                        case 3:
                            new_due_date = input("Change Due Date: ").strip()
                            if new_due_date:
                                due_date = new_due_date
                        
                        case 4:
                            break

                        case _:
                            print("Invalid Choice, Try again.")
                            continue

                
                updated_tasks.append(f"{saved_id}|{title}|{description}|{due_date}|{completed}\n")
            else:
                updated_tasks.append(task)

        with open("tasks.txt", "w") as file:
            file.writelines(updated_tasks)

        if not task_found:
            print("Task not found.")
        else:
            print("Task updated")