
# TO-DO LIST APPLICATION
# PS No. 24

FILE_NAME = "todo.txt"


# Load tasks from the file
def load_tasks():
    tasks = []

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                try:
                    task_id, title, status = line.split("|", 2)

                    task = {
                        "id": int(task_id),
                        "title": title,
                        "status": status
                    }

                    tasks.append(task)

                except ValueError:
                    print("Warning: A damaged task record was skipped.")

    except FileNotFoundError:
        save_tasks(tasks)

    return tasks


# Save tasks to the file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(
                f'{task["id"]}|{task["title"]}|{task["status"]}\n'
            )


# Add a new task
def add_task(tasks):
    title = input("Enter task title: ").strip()

    if title == "":
        print("Task title cannot be empty.")
        return

    if tasks:
        new_id = max(task["id"] for task in tasks) + 1
    else:
        new_id = 1

    task = {
        "id": new_id,
        "title": title,
        "status": "Pending"
    }

    tasks.append(task)
    save_tasks(tasks)

    print(
        f'Task added. {task["id"]} | '
        f'{task["title"]} | {task["status"]}'
    )


# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found. Your to-do list is empty.")
        return

    print("\n------ YOUR TO-DO LIST ------")

    for task in tasks:
        print(
            f'{task["id"]} | {task["title"]} | {task["status"]}'
        )


# Mark a task as completed
def complete_task(tasks):
    if not tasks:
        print("No tasks found. Your to-do list is empty.")
        return

    try:
        task_number = int(input("Enter task number to complete: "))
    except ValueError:
        print("Invalid task number. Please enter a number.")
        return

    for task in tasks:
        if task["id"] == task_number:

            if task["status"] == "Done":
                print(f"Task {task_number} is already completed.")
                return

            task["status"] = "Done"
            save_tasks(tasks)

            print(f"Task {task_number} marked as completed.")
            return

    print(f"Task number {task_number} not found.")


# Delete a task
def delete_task(tasks):
    if not tasks:
        print("No tasks found. Your to-do list is empty.")
        return

    try:
        task_number = int(input("Enter task number to delete: "))
    except ValueError:
        print("Invalid task number. Please enter a number.")
        return

    for task in tasks:
        if task["id"] == task_number:
            tasks.remove(task)
            save_tasks(tasks)

            print(
                f"Task {task_number} deleted. "
                f"Tasks left: {len(tasks)}"
            )
            return

    print(f"Task number {task_number} not found.")


# Main menu
def main():
    tasks = load_tasks()

    while True:
        print("\n========== TO-DO LIST MENU ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Thank you for using the To-Do List Application!")
            break

        else:
            print("Invalid choice. Please select between 1 and 5.")


# Start the program
if __name__ == "__main__":
    main()
