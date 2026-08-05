import pickle
import sys
from pathlib import Path

tasks = []

TASK = Path(__file__).parent / "tasks.deez"

try:
    with open(TASK, "rb") as f:
        tasks = pickle.load(f)
except FileNotFoundError, EOFError:
    tasks = []

while True:
    print("""
___________________________
      | TO DO LIST |

1. Add a task
2. Remove a task
3. View all tasks
4. Mark a task as completed
5. Exit & Save Changes
___________________________\n """)

    def addTask():
        task = input("\nEnter the task name: \n")
        if any(taskname["name"] == task for taskname in tasks):
            print("\n[ERROR] Task is already made!", file=sys.stderr)
            return
        
        if task.strip() == "":
            print("[ERROR] Task cannot be empty", file=sys.stderr)
            return
        
        tasks.append({"name": task, "completed": False})
        print("\nTask Created.")
        return

    def removeTask():
        viewTask()
        
        try:
            taskdel = int(input("\nEnter task No. to delete:\n")) - 1
            
            if not (0 <= taskdel < len(tasks)):
                print("\n[ERROR] Task not found.", file=sys.stderr)
            else:
                print("\nTask removed.")
            
            del tasks[taskdel]
        except ValueError:
            print("\n[ERROR] Incorrect Task Selection", file = sys.stderr)

    def viewTask():
        if not tasks:
            print("\n[ERROR] No task found", file=sys.stderr)
            return

        for i, task in enumerate(tasks, start=1):
            status = "/" if task["completed"] else "X"
            print(f"\nTask #{i} [{status}]: {task['name']}")

    def markTask():
        if not tasks:
            print("\n[ERROR] No task found", file=sys.stderr)
            return
        
        viewTask()
        
        try:
            num = int(input("\nNumber of Task: "))
            if not (1 <= num <= len(tasks)):
                print("\n[ERROR] Task not found.", file=sys.stderr)
                return
            tasks[num - 1]["completed"] = True
            print("\nTask Completed.")
        except ValueError:
            print("\n[ERROR] Enter a valid number.")

    try:
        action = int(input("Choose an action: "))
    except ValueError:
        print("\n[ERROR] Enter valid numbers.")

    if action == 1:
        addTask()
        continue

    elif action == 2:
        removeTask()
        continue

    elif action == 3:
        viewTask()
        continue

    elif action == 4:
        markTask()
        continue

    elif action == 5:
        print("\n[EXITING] Saving Changes")
        
        with open(TASK, "wb")as f:
            pickle.dump(tasks, f)
        break
