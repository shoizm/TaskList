tasks = [""]

while True:
    print("""
| TO DO LIST |
1. Add a task
2. Remove a task
3. View all tasks
4. Mark a task as completed
5. Exit\n """)

    action = int(input())
    if action == 1:
        print("\nEnter the task name: ")
        task = input
        tasks.insert(0, task)
    elif action == 2:
        print(list)
    elif action == 3:
        print(list)
    elif action == 4:
        print(list)
    elif action == 5:
        print("Exiting To-Do-List")
        break