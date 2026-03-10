import math

# ANSI Color Codes
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

def show_menu():
    print(f"\n{CYAN}=== SCIENTIFIC CALCULATOR ==={RESET}")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Square Root (√)")
    print("7. Percentage (%)")
    print("8. Back to Main Menu")

def get_numbers(count=2):
    try:
        if count == 1:
            num = float(input(f"{YELLOW}Enter number: {RESET}"))
            return num
        else:
            num1 = float(input(f"{YELLOW}Enter first number: {RESET}"))
            num2 = float(input(f"{YELLOW}Enter second number: {RESET}"))
            return num1, num2
    except ValueError:
        print(f"{RED}Error: Invalid numeric input!{RESET}")
        return None

def run_calculator():
    while True:
        show_menu()
        choice = input(f"{YELLOW}Select operation: {RESET}")
        
        if choice == '8':
            break
            
        if choice in ['1', '2', '3', '4', '5']:
            nums = get_numbers(2)
            if nums is None: continue
            a, b = nums
            
            if choice == '1': print(f"{GREEN}Result: {a + b}{RESET}")
            elif choice == '2': print(f"{GREEN}Result: {a - b}{RESET}")
            elif choice == '3': print(f"{GREEN}Result: {a * b}{RESET}")
            elif choice == '4':
                if b == 0: print(f"{RED}Error: Division by zero!{RESET}")
                else: print(f"{GREEN}Result: {a / b}{RESET}")
            elif choice == '5': print(f"{GREEN}Result: {math.pow(a, b)}{RESET}")
            
        elif choice == '6':
            num = get_numbers(1)
            if num is None: continue
            if num < 0: print(f"{RED}Error: Cannot calculate square root of negative number!{RESET}")
            else: print(f"{GREEN}Result: {math.sqrt(num)}{RESET}")
            
        elif choice == '7':
            nums = get_numbers(2)
            if nums is None: continue
            a, b = nums
            print(f"{GREEN}Result: {(a / 100) * b}{RESET}") # a% of b
            
        else:
            print(f"{RED}Invalid selection!{RESET}")

if __name__ == "__main__":
    run_calculator()
