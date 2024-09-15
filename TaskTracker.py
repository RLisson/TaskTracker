from pathlib import Path
from enum import Enum
from datetime import datetime
import json


class Status(Enum):
    Todo = 1
    In_progress = 2
    Done = 3


class Task:
    def __init__(self, _id: int, description: str, status: Status | None):
        self.id = _id
        self.description = description
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime | None = None
        if not status:
            self.status = Status.Todo
        else:
            self.status = status

    def __repr__(self) -> str:
        _repr = (f'{self.id} - {self.description} - {self.status.name}. Created at: '
                 f'{self.created_at.strftime("%d/%m/%y, %H:%M:%S")}')
        if self.updated_at:
            _repr += f', Updated at: {
                self.updated_at.strftime("%d/%m/%y, %H:%M:%S")}'
        return _repr


class TaskManager:
    def __init__(self, file: Path) -> None:
        self.file = file
        self._tasks: list[Task] = []
        self.max_id: int = 0

    def dump_all(self):
        dumps: list[dict] = []
        for task in self._tasks:
            data = task.__dict__
            dumps.append(data)
        with open(self.file, 'w', encoding='utf8') as f:
            json.dump(dumps, f, indent=4, default=str)

    def add_task(self, task: Task):
        self._tasks.append(task)

    def add_new_task(self, description: str, status: Status | None = None) -> None:
        _id = self.max_id + 1
        self.max_id += 1
        self._tasks.append(Task(_id, description, status))

    def load_json(self) -> None:
        with open(self.file, 'r', encoding='utf8') as f:
            print(json.load(f))

    def delete_task(self, id) -> None:
        for task in self._tasks:
            if task == id:
                self._tasks.remove(task)

    def update_task(self, id: int, description: str) -> bool:
        for task in self._tasks:
            if task.id == id:
                task.description = description
                return True
        return False

    def list_tasks(self) -> None:
        for task in self._tasks:
            print(task)
