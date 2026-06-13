

tasks = []

while True:
    print("----- TO DO LIST -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    option = input("Select Option : ")

    if option == "1":
        new_task = input("Enter your task : ")

        tasks.append(new_task)

        with open("tasks.txt", "a") as file:
            file.write(new_task + "\n")

        print("✅ Task added Successfully!")

    elif option == "2":

        try:
            with open("tasks.txt", "r") as file:
                data = file.read()

            if data == "":
                print("📌 No tasks found.")
            else:
                print("----- Tasks -----")
                print(data)

        except FileNotFoundError:
            print("📌 No tasks found.")

    elif option == "3":

        if len(tasks) == 0:
            print("📌 No tasks to delete.")

        else:
            print("----- Tasks -----")

            for i, task in enumerate(tasks, start=1):
                print(i, ".", task)

            delete_task = int(input("Enter task number : "))

            if 1 <= delete_task <= len(tasks):
                tasks.pop(delete_task - 1)
                print("✅ Task deleted successfully!")

            else:
                print("❌ Invalid task number!")

    elif option == "4":
        print("👋 Goodbye! Thanks for managing your tasks today")
        break

    else:
        print("❌ Oops! Invalid choice. Please enter 1, 2, 3 or 4")