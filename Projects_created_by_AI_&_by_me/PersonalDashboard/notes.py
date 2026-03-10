import os

# ANSI Color Codes
MAGENTA = "\033[95m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
NOTES_FILE = os.path.join(DATA_DIR, "notes.txt")

def ensure_notes_file():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            pass

def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        for note in notes:
            f.write(note + "\n---\n")

def load_notes():
    ensure_notes_file()
    if not os.path.exists(NOTES_FILE): return []
    with open(NOTES_FILE, "r") as f:
        content = f.read()
    if not content.strip(): return []
    return [n.strip() for n in content.split("---\n") if n.strip()]

def add_note():
    print(f"{YELLOW}Type your note (Press Enter twice to save):{RESET}")
    lines = []
    while True:
        line = input()
        if line == "" and (not lines or lines[-1] == ""):
            if lines: lines.pop() # remove last empty line
            break
        lines.append(line)
    
    note_text = "\n".join(lines).strip()
    if note_text:
        notes = load_notes()
        notes.append(note_text)
        save_notes(notes)
        print(f"{GREEN}Note saved!{RESET}")

def view_notes():
    notes = load_notes()
    print(f"\n{MAGENTA}=== YOUR NOTES ==={RESET}")
    if not notes:
        print(f"{YELLOW}No notes found!{RESET}")
    else:
        for idx, note in enumerate(notes, 1):
            print(f"{idx}. {note[:50]}..." if len(note) > 50 else f"{idx}. {note}")
    print("-" * 18)

def search_notes():
    query = input(f"{YELLOW}Search for: {RESET}").lower()
    notes = load_notes()
    found = False
    for idx, note in enumerate(notes, 1):
        if query in note.lower():
            print(f"\n{GREEN}[Match found at #{idx}]{RESET}")
            print(note)
            found = True
    if not found:
        print(f"{RED}No notes match your search.{RESET}")

def delete_note():
    view_notes()
    notes = load_notes()
    if not notes: return
    try:
        choice = int(input(f"{YELLOW}Note number to delete: {RESET}"))
        if 1 <= choice <= len(notes):
            notes.pop(choice-1)
            save_notes(notes)
            print(f"{GREEN}Note deleted!{RESET}")
        else:
            print(f"{RED}Invalid note number!{RESET}")
    except ValueError:
        print(f"{RED}Invalid input!{RESET}")

def run_notes():
    while True:
        print(f"\n{MAGENTA}=== NOTE MANAGER ==={RESET}")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Search Notes")
        print("4. Delete Note")
        print("5. Back to Main Menu")
        
        choice = input(f"{YELLOW}Choice: {RESET}")
        if choice == '1': view_notes()
        elif choice == '2': add_note()
        elif choice == '3': search_notes()
        elif choice == '4': delete_note()
        elif choice == '5': break
        else: print(f"{RED}Invalid option!{RESET}")

if __name__ == "__main__":
    run_notes()
