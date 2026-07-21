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

    def addTask():
        task = input("\nEnter the task name: \n")
        if task in tasks:
            print("\n[ERROR] Task is already made!", file=sys.stderr)
        else:
            print("\nTask created.")
            tasks.append(task)


    def removeTask():
        delete = int(input("\nEnter task no. to delete\n"))
        calculated = delete -1
        del tasks[calculated]
        print("\nTask removed.")

    
    def viewTask():
        for i, task in enumerate(tasks, start=1):
            print("\nTask", "#" + str(i) + ":", "\n" + task)

    def markTask():
        print(tasks)

    action = int(input("Choose an action: "))

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
        print(tasks)

    elif action == 5:
        print("Exiting Task-List")
        break

    else:
        print("\n[ERROR]", file=sys.stderr)
