# Task Tracker

Solution for the [task-tracker](https://roadmap.sh/projects/task-tracker) challenge from [roadmap.sh](https://roadmap.sh/)

## How to run
Clone the repository and run the following command

```bash
# Add a new task
python3 ./main.py add "task description"`

# Show tasks
python3 ./main.py list
python3 ./main.py list todo
python3 ./main.py list in-progress
python3 ./main.py list done

# Change task status
python3 ./main.py id mark-in-progress
python3 ./main.py id mark-in-done

# Change task decription
python3 ./main.py update id "new description"
```