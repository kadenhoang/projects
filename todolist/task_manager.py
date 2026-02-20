from storage import Storage
from reminders import Reminders
from utils import generate_id

class Task:
    def __init__(self, title, description, due_date, timeframe, reminder=None, completed=False, task_id=None):
        self.id = task_id or generate_id()
        self.title = title
        self.description = description
        self.due_date = due_date
        self.timeframe = timeframe
        self.reminder = reminder
        self.completed = completed

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
        task = Task(title, description, due_date, timeframe, reminder)
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
