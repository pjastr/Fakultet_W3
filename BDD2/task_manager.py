from datetime import datetime
from enum import Enum
import uuid


class TaskStatus(Enum):
    TO_DO = "TO_DO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"


class Task:
    def __init__(self, title, description, task_id=None):
        self.id = task_id or str(uuid.uuid4())
        self.title = title
        self.description = description
        self.status = TaskStatus.TO_DO
        self.created_date = datetime.now()
        self.due_date = None
        self.completed_date = None

    def mark_as_in_progress(self):
        self.status = TaskStatus.IN_PROGRESS

    def mark_as_done(self):
        self.status = TaskStatus.DONE
        self.completed_date = datetime.now()

    def set_due_date(self, due_date):
        self.due_date = due_date

    def is_overdue(self):
        if not self.due_date:
            return False
        if self.status == TaskStatus.DONE:
            return False
        return datetime.now() > self.due_date


class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks[task.id] = task
        return task.id

    def get_task(self, task_id):
        return self.tasks.get(task_id)

    def mark_as_in_progress(self, task_id):
        task = self.get_task(task_id)
        if task:
            task.mark_as_in_progress()

    def mark_as_done(self, task_id):
        task = self.get_task(task_id)
        if task:
            task.mark_as_done()

    def set_due_date(self, task_id, due_date):
        task = self.get_task(task_id)
        if task:
            task.set_due_date(due_date)

    def get_all_tasks(self):
        return list(self.tasks.values())

    def get_tasks_by_status(self, status):
        return [task for task in self.tasks.values() if task.status == status]

    def get_overdue_tasks(self):
        return [task for task in self.tasks.values() if task.is_overdue()]