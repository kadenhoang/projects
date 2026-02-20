import json
from task_manager import Task

class Storage:
    def __init__(self, filename):
        self.filename = filename

    def load_tasks(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                tasks = []
                for t in data:
                    task = Task(
                        title=t["title"],
                        description=t["description"],
                        due_date=t["due_date"],
                        timeframe=t["timeframe"],
                        reminder=t.get("reminder"),
                        completed=t.get("completed", False),
                        task_id=t["id"]
                    )
                    tasks.append(task)
                return tasks
        except FileNotFoundError:
            return []

    def save_tasks(self, tasks):
        data = [t.__dict__ for t in tasks]
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)
