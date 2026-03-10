import os

# ANSI Color Codes
WHITE = "\033[97m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
TODO_FILE = os.path.join(DATA_DIR, "todos.txt")
NOTES_FILE = os.path.join(DATA_DIR, "notes.txt")

def get_todo_stats():
    if not os.path.exists(TODO_FILE):
        return 0, 0, 0
    
    total = 0
    completed = 0
    with open(TODO_FILE, "r") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) == 2:
                total += 1
                if parts[1] == "True":
                    completed += 1
    
    percentage = (completed / total * 100) if total > 0 else 0
    return total, completed, percentage

def get_note_stats():
    if not os.path.exists(NOTES_FILE):
        return 0
    
    with open(NOTES_FILE, "r") as f:
        content = f.read()
    notes = [n.strip() for n in content.split("---\n") if n.strip()]
    return len(notes)

def run_stats():
    total_tasks, completed_tasks, percentage = get_todo_stats()
    total_notes = get_note_stats()
    
    print(f"\n{WHITE}=== PRODUCTIVITY STATS ==={RESET}")
    print(f"{BLUE}Tasks Management:{RESET}")
    print(f"  - Total Tasks:     {total_tasks}")
    print(f"  - Completed Tasks: {GREEN}{completed_tasks}{RESET}")
    print(f"  - Pending Tasks:   {YELLOW}{total_tasks - completed_tasks}{RESET}")
    print(f"  - Completion Rate: {GREEN}{percentage:.1f}%{RESET}")
    
    print(f"\n{BLUE}Notes Management:{RESET}")
    print(f"  - Total Notes:     {total_notes}")
    
    print(f"\n{WHITE}Keep it up, Aditya!{RESET}")
    input(f"\n{YELLOW}Press Enter to return to main menu...{RESET}")

if __name__ == "__main__":
    run_stats()
