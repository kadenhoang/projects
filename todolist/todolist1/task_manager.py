from todolist.todolist1.storage import Storage
from todolist.todolist1.reminders import Reminders
from todolist.todolist1.task_details import Task
from todolist.todolist1.utils import generate_id


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.storage = Storage("tasks.json")
        self.reminders = Reminders()

    def load_tasks(self):
        self.tasks = self.storage.load_tasks()

    def save_tasks(self):
        self.storage.save_tasks(self.tasks)

    def add_task(self, title, description, due_date, timeframe, reminder=None):
        task = Task(title, description, due_date, timeframe, reminder, completed=False, task_id=generate_id())
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{title}' added.")

    def view_tasks(self, timeframe):
        filtered = [t for t in self.tasks if timeframe == "all" or t.timeframe == timeframe]
        if not filtered:
            print("No tasks found.")
            return
        for t in filtered:
            status = "✔" if t.completed else "✗"
            print(f"ID: {t.id} | {status} | {t.title} | Due: {t.due_date} | Reminder: {t.reminder}")

    def complete_task(self, task_id):
        for t in self.tasks:
            if t.id == task_id:
                t.completed = True
                self.save_tasks()
                print(f"Task '{t.title}' marked complete.")
                return
        print("Task not found.")

    def delete_tasks(self, ids):
        id_list = [i.strip() for i in ids.split(",")]
        before = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.id not in id_list]
        deleted = before - len(self.tasks)
        self.save_tasks()
        print(f"Deleted {deleted} task(s).")
