class Task_Manager:
    def __init__(self, id, title, description, due_date):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date

    def add_task(self, id, title, description, due_date):
        task = Task_Manager(id, title, description, due_date)
        return task

    def save_tasks(self, task):
        with open("tasks.txt", "a") as file:
            file.write(f"{task.title}|{task.description}|{task.due_date}\n")

    def view_tasks(self):
        with(open("task.txt", "r") as file):
            tasks = file.readlines()
            for task in tasks:
                title, description, due_date = task.strip().split("|")
                print(f"Title: {title}, Description: {description}, Due Date: {due_date}")

    # Delete task by id
    def delete_tasks(self, id):
        with (open("tasks.txt", "r") as file):
            tasks = file.readlines()
        # Rewrite the file without the deleted task
        with (open("tasks.txt", "w") as file):
            for task in tasks:
                if not task.startswith(f"{id}|"):
                    file.write(task)
