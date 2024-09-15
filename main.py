from pathlib import Path
from datetime import datetime
from TaskTracker import Task, TaskManager, Status
import os
import json
import sys


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
        if (dict_['updated_at']):
            updated = datetime.strptime(dict_['updated_at'], date_format)
            task.updated_at = updated
        ids.add(dict_['id'])
        t1.add_task(task)

    t1.max_id = max(ids)

if (sys.argv[1] == 'add'):
    t1.add_new_task(sys.argv[2])
    t1.list_tasks()
elif (sys.argv[1] == 'update'):
    success = t1.update_task_description(int(sys.argv[2]), sys.argv[3])
    t1.list_tasks()
elif (sys.argv[1]) == 'delete':
    success = t1.delete_task(int(sys.argv[2]))
    t1.list_tasks()
elif (sys.argv[1] == 'mark-in-progress'):
    success = t1.update_task_status(int(sys.argv[2]), Status.In_progress)
    t1.list_tasks()
elif (sys.argv[1] == 'mark-done'):
    success = t1.update_task_status(int(sys.argv[2]), Status.Done)
    t1.list_tasks()
elif (sys.argv[1] == 'list'):
    if len(sys.argv) == 2:
        t1.list_tasks()
    elif (sys.argv[2] == 'done'):
        t1.list_done_tasks()
    elif (sys.argv[2] == 'in-progresss'):
        t1.list_in_progress_tasks()
    elif (sys.argv[2] == 'todo'):
        t1.list_todo_tasks()

t1.dump_all()

if not success:
    print("Invalid ID!")
