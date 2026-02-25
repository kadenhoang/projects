class Task_Manager:
    def __init__(self, id, title, description, due_date, completed = False):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed

    @classmethod
    def add_task(cls, id, title, description, due_date):
        task = Task_Manager(id, title, description, due_date)
        with open("tasks.txt", "a") as file:
            file.write(f"{task.id}|{task.title}|{task.description}|{task.due_date}|{task.completed}\n")
            #all the fields after being written in the file become string data
    @classmethod    
    def view_tasks(cls):
        with(open("tasks.txt", "r") as file):
            tasks = file.readlines()
            for task in tasks:
                id, title, description, due_date, completed = task.strip().split("|")
                status = "✔" if completed == "True" else "✗"
                print(f"{status} | ID: {id} | Title: {title}, Description: {description}, Due Date: {due_date}")

    # Delete task by id
    @classmethod
    def delete_tasks(cls, id):
        with (open("tasks.txt", "r") as file):
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

