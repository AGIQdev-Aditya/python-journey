import os
import todo
import calculator
import notes
import stats

# ANSI Color Codes
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"
RED = "\033[91m"
RESET = "\033[0m"

def welcome_screen():
    ascii_art = f"""{CYAN}
    **************************************************
    *                                                *
    *    WELCOME TO THE PERSONAL DASHBOARD, {YELLOW}ADITYA{CYAN}!   *
    *                                                *
    *        ____  _____ ____  ____   _   _          *
    *       |  _ \| ____|  _ \|  _ \ / \ | |         *
    *       | | | |  _| | |_) | |_) / _ \| |         *
    *       | |_| | |___|  _ <|  __/ ___ \ |___      *
    *       |____/|_____|_| \_\_| /_/   \_\_____|    *
    *                                                *
    **************************************************
    {RESET}"""
    print(ascii_art)

def main_menu():
    while True:
        welcome_screen()
        print(f"{WHITE}Choose a module to launch:{RESET}")
        print(f"{BLUE}1. To-Do Manager{RESET} (Tasks & Lists)")
        print(f"{GREEN}2. Scientific Calculator{RESET} (Math operations)")
        print(f"{MAGENTA}3. Personal Notes{RESET} (Write & Search)")
        print(f"{YELLOW}4. Productivity Stats{RESET} (Analyze performance)")
        print(f"{RED}5. Exit Dashboard{RESET}")
        
        choice = input(f"\n{WHITE}Enter your choice (1-5): {RESET}")
        
        if choice == '1':
            todo.run_todo()
        elif choice == '2':
            calculator.run_calculator()
        elif choice == '3':
            notes.run_notes()
        elif choice == '4':
            stats.run_stats()
        elif choice == '5':
            print(f"\n{CYAN}Goodbye, Aditya! Have a productive day!{RESET}")
            break
        else:
            print(f"{RED}Invalid choice! Please select between 1 and 5.{RESET}")
            input(f"{YELLOW}Press Enter to continue...{RESET}")
        
        # Clear screen for next menu iteration (os-dependent)
        os.system('clear' if os.name == 'posix' else 'cls')

if __name__ == "__main__":
    # Ensure data directory exists
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(BASE_DIR, "data")
    
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    
    # Run the dashboard
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{RED}Dashboard terminated by user. Goodbye!{RESET}")
