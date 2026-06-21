tasks = []

# Load existing tasks from the file when the program starts
try:
    with open("tasks.txt", "r") as file:
        # Read lines and remove extra whitespaces or newlines
        tasks = [line.strip() for line in file.readlines() if line.strip()]
except FileNotFoundError:
    tasks = []

while True:
    print("\n----- TO DO LIST -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Task Complete")
    print("5. Search Task")
    print("6. Edit task")
    print("7. Exit")

    option = input("Select Option : ")

    if option == "1":
        new_task = input("Enter your task : ")
        tasks.append(new_task)

        # Overwrite the file to keep it synced with the tasks list
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")

        print("✅ Task added Successfully!")

    elif option == "2":
        if len(tasks) == 0:
            print("📌 No tasks found.")
        else:
            print("----- Tasks -----")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif option == "3":
        if len(tasks) == 0:
            print("📌 No tasks to delete.")
        else:
            print("----- Tasks -----")
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task)

            try:
                delete_task = int(input("Enter task number to delete : "))

                if 1 <= delete_task <= len(tasks):
                    tasks.pop(delete_task - 1)
                    
                    with open("tasks.txt", "w") as file:
                        for task in tasks:
                            file.write(task + "\n")
                            
                    print("✅ Task deleted successfully!")
                else:
                    print("❌ Invalid task number!")
            except ValueError:
                print("❌ Please enter a valid number!")

    elif option == "4":
        if len(tasks) == 0:
            print("📌 No tasks to mark as complete.")
        else:
            print("----- Tasks -----")
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task)
            
            try:
                task_complete = int(input("Enter task number to mark complete: "))
                
                if 1 <= task_complete <= len(tasks):
                    index = task_complete - 1
                    
                    if "[Complete]" not in tasks[index]:
                        tasks[index] = tasks[index] + " [Complete]"
                        
                        with open("tasks.txt", "w") as file:
                            for task in tasks:
                                file.write(task + "\n")
                                
                        print("🎉 Task marked as Complete!")
                    else:
                        print("🤔 This task is already completed!")
                else:
                    print("❌ Invalid task number!")
            except ValueError:
                print("❌ Please enter a valid number!")

    elif option == "5":
        if len(tasks) == 0:
            print("📌 No task available to search.")
        else:
            search_task = input("Enter task name : ").strip().lower()
            found = False

            print("----- Search Results -----")
            for i, task in enumerate(tasks, start=1):
                if search_task in task.lower():
                    print(f"{i}. {task}")
                    found = True

            # Yeh check hamesha FOR loop ke BAHAR hona chahiye ekdum same line me
            if found == False:
                print("❌ Task not found!")
    elif option == "6":
        edit_task=int(input("Enter task number : "))
        new_task = input("Enter new task : ")
        tasks[edit_task - 1] = new_task
        with open("tasks.txt", "w") as file:
         for task in tasks:
          file.write(task + "\n")

    elif option == "7":
        print("👋 Goodbye! Thanks for managing your tasks today")
        break

    else:
        print("❌ Oops! Invalid choice. Please enter 1, 2, 3, 4, 5 or 6")