def empty_task(tasks):
    if not tasks:
        print("No tasks here.")
        return True
    return False

def add_tasks(tasks):
    new_task = input("Add task: ").strip().upper()
    if new_task:
        tasks.append(new_task)
        print("Task added.")

def remove_tasks(tasks):
    if empty_task(tasks): 
        return
    else:
        show_tasks(tasks)
        try:
            task_number = int(input("Enter task number to remove: "))
            if 1 <= task_number <= len(tasks):
                tasks.pop(task_number - 1)
                print("Task removed.")
            else:
                print("No matching task.")

        except ValueError:
            print("Invalid number.")

def show_tasks(tasks):
    if empty_task(tasks): 
        return
    else:
        for index,task in enumerate(tasks, 1):
            print(f"{index}. {task.title()}")

def search_tasks(tasks):
    if empty_task(tasks): 
        return
    else:
        keyword = input("Enter keyword to search task: ").strip().upper()
        found = [task for task in tasks if keyword in task.upper()]
        show_tasks(found)

def clear_tasks(tasks):
    if empty_task(tasks): 
        return
    else:
        confirm = input("Are you sure to clear all tasks? (y/n): ").strip().lower()
        if confirm in ["y","yes"]:
            tasks.clear()
            print("All tasks cleared.")

def to_do_list():
    
    tasks = []
    view_command = ["view","tasks","list"]
    quit_command = ["exit","quit"]
    remove_command = ["remove","delete"]
    help_command = (
        "\nCommands:\n"
    "  add             -> Add a new task\n"
    "  view/tasks/list -> View all tasks\n"
    "  remove/delete   -> Remove a task by number\n"
    "  search          -> Search tasks by keyword\n"
    "  clear           -> Remove all tasks\n"
    "  exit/quit       -> Exit the program\n"
    "  help            -> Show this help message\n"
    )

    while True:

        command = input("> ").strip().lower()

        if command in quit_command:
            break

        elif command == "help":
            print(help_command)
            continue

        elif command in view_command:
            show_tasks(tasks)
            continue

        elif command == "search":
            search_tasks(tasks)
            continue

        elif command == "add":
            add_tasks(tasks)
            continue

        elif command in remove_command:
            remove_tasks(tasks)
            continue

        elif command == "clear":
            clear_tasks(tasks)
            continue
                
        else:
            print("Invalid command. Type 'help' to see valid command.")

if __name__ == "__main__":
    to_do_list()