import os

# ANSI Color Codes
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
TODO_FILE = os.path.join(DATA_DIR, "todos.txt")

def ensure_data_file():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(TODO_FILE):
        with open(TODO_FILE, "w") as f:
            pass

def load_todos():
    ensure_data_file()
    todos = []
    with open(TODO_FILE, "r") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) == 2:
                todos.append({"task": parts[0], "completed": parts[1] == "True"})
    return todos

def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        for todo in todos:
            f.write(f"{todo['task']}|{todo['completed']}\n")

def view_todos():
    todos = load_todos()
    print(f"\n{BLUE}--- YOUR TODO LIST ---{RESET}")
    if not todos:
        print(f"{YELLOW}No tasks found!{RESET}")
    else:
        for idx, todo in enumerate(todos, 1):
            status = f"{GREEN}[✓]{RESET}" if todo['completed'] else f"{RED}[ ]{RESET}"
            print(f"{idx}. {status} {todo['task']}")
    print("-" * 22)

def add_todo():
    task = input(f"{YELLOW}Enter task description: {RESET}").strip()
    if task:
        todos = load_todos()
        todos.append({"task": task, "completed": False})
        save_todos(todos)
        print(f"{GREEN}Task added successfully!{RESET}")
    else:
        print(f"{RED}Task cannot be empty!{RESET}")

def complete_todo():
    view_todos()
    todos = load_todos()
    if not todos: return
    try:
        choice = int(input(f"{YELLOW}Enter task number to mark complete: {RESET}"))
        if 1 <= choice <= len(todos):
            todos[choice-1]['completed'] = True
            save_todos(todos)
            print(f"{GREEN}Task marked as complete!{RESET}")
        else:
            print(f"{RED}Invalid task number!{RESET}")
    except ValueError:
        print(f"{RED}Please enter a valid number!{RESET}")

def delete_todo():
    view_todos()
    todos = load_todos()
    if not todos: return
    try:
        choice = int(input(f"{YELLOW}Enter task number to delete: {RESET}"))
        if 1 <= choice <= len(todos):
            removed = todos.pop(choice-1)
            save_todos(todos)
            print(f"{GREEN}Deleted: {removed['task']}{RESET}")
        else:
            print(f"{RED}Invalid task number!{RESET}")
    except ValueError:
        print(f"{RED}Please enter a valid number!{RESET}")

def run_todo():
    while True:
        print(f"\n{BLUE}=== TODO MANAGER ==={RESET}")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Back to Main Menu")
        
        choice = input(f"{YELLOW}Choice: {RESET}")
        if choice == '1': view_todos()
        elif choice == '2': add_todo()
        elif choice == '3': complete_todo()
        elif choice == '4': delete_todo()
        elif choice == '5': break
        else: print(f"{RED}Invalid option!{RESET}")

if __name__ == "__main__":
    run_todo()
