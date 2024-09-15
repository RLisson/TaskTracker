from pathlib import Path
from datetime import datetime
from TaskTracker import Task, TaskManager, Status
import os
import json


PATH = Path(__file__).parent
FILE = PATH / "tasks.json"

if os.path.exists(FILE):
    with open(FILE, 'r', encoding='utf8') as f:
        try:
            load = json.load(f)
        except:
            load = None
else:
    with open(FILE, 'w', encoding='utf8') as f:
        f.write('')
        load = None
t1 = TaskManager(FILE)

if load:
    ids = set()
    date_format = "%Y-%m-%d %H:%M:%S.%f"
    for dict_ in load:
        status = Status[dict_['status'][7::]]
        task = Task(dict_['id'], dict_['description'], status)
        created = datetime.strptime(dict_['created_at'], date_format)
        task.created_at = created
        ids.add(dict_['id'])
        t1.add_task(task)

    t1.max_id = max(ids)
