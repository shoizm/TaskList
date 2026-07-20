import sys

tasks = []

while True:
    print("""
___________________________
      | TO DO LIST |

1. Add a task
2. Remove a task
3. View all tasks
4. Mark a task as completed
5. Exit
___________________________\n """)

    action = int(input())
    if action == 1:
        task = input("\nEnter the task name: ")
        tasks.append(task)
        continue

    elif action == 2:
        delete = int(input("\nEnter task no. to delete\n"))
        calculated = delete -1
        del tasks[calculated]
        print("\nTask removed.")
        continue

    elif action == 3:
        for i, task in enumerate(tasks, start=1):
            print("\n" + "Task:", i)
            print(task)


    elif action == 4:
        print(tasks)

    elif action == 5:
        print("Exiting To-Do-List")
        break

    else:
        print("\n[ERROR]", file=sys.stderr)

    
