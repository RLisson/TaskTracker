from pathlib import Path
from TaskTracker import Task, TaskManager
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

ids = set()
if load:
    for dict_ in load:
        task = Task(dict_['id'], dict_['description'], dict_['status'])
        ids.add(dict_['id'])
t1.max_id = max(ids)

t1.add_new_task("gooo")
t1.add_new_task("aaaa")

t1.dump_all()
