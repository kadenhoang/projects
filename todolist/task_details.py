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