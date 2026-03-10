import math

def simple_calculator():
    print("Simple Calculator")
    while True:
        print("Options:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = input("Enter choice (1/2/3/4/5): ")
        if choice == '5':
            print("Exiting simple calculator.")
            break
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if choice == '1':
                    print(f"{num1} + {num2} = {num1 + num2}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {num1 - num2}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {num1 * num2}")
                elif choice == '4':
                    if num2 == 0:
                        print("Error! Division by zero.")
                    else:
                        print(f"{num1} / {num2} = {num1 / num2}")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid choice! Please select 1-5.")

def scientific_calculator():
    print("Scientific Calculator (trigonometric functions in radians)")
    while True:
        print("Options:")
        print("1. Sin")
        print("2. Cos")
        print("3. Tan")
        print("4. Log")
        print("5. Exit")
        choice = input("Enter choice (1/2/3/4/5): ")
        if choice == '5':
            print("Exiting scientific calculator.")
            break
        if choice in ('1', '2', '3', '4'):
            try:
                num = float(input("Enter a number: "))
                if choice == '1':
                    print(f"sin({num}) = {math.sin(num)}")
                elif choice == '2':
                    print(f"cos({num}) = {math.cos(num)}")
                elif choice == '3':
                    print(f"tan({num}) = {math.tan(num)}")
                elif choice == '4':
                    if num <= 0:
                        print("Error! Logarithm of non-positive number.")
                    else:
                        print(f"log({num}) = {math.log(num)}")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
        else:
            print("Invalid choice! Please select 1-5.")

def main():
    print("Calculator Modes:")
    print("1. Simple Calculator")
    print("2. Scientific Calculator")
    print("3. Exit")
    while True:
        mode_choice = input("Enter mode choice (1/2/3): ")
        if mode_choice == '1':
            simple_calculator()
        elif mode_choice == '2':
            scientific_calculator()
        elif mode_choice == '3':
            print("Exiting calculator.")
            break
        else:
            print("Invalid mode choice! Please select 1-3.")

if __name__ == "__main__":
    main()