# PersonalDashboard

Welcome to the **PersonalDashboard**, a terminal-based productivity suite designed for Aditya.

## Project Structure

- **main.py**: The central entry point. Features a beautiful ASCII welcome screen and a menu to navigate between different modules.
- **todo.py**: Manage your daily tasks.
  - Features: Add, View, Mark Complete, and Delete tasks.
  - Storage: Data is saved to `data/todos.txt`.
- **calculator.py**: A powerful scientific calculator.
  - Features: Basic arithmetic, Power, Square Root, and Percentage calculation.
- **notes.py**: A personal note-taking app.
  - Features: Create multi-line notes, view existing notes, search through notes, and delete them.
  - Storage: Data is saved to `data/notes.txt`.
- **stats.py**: Your productivity analyzer.
  - Features: Shows total tasks, completion percentage, and total number of notes.
- **data/**: Directory containing all persistent data files.

## How to Run

Navigate to the project directory and run:

```bash
python main.py
```

## Features
- **Colorful Terminal UI**: Uses ANSI color codes for a visually appealing experience.
- **Persistent Storage**: All your data stays safe even after closing the program.
- **Error Handling**: Built-in checks for invalid inputs to ensure a smooth experience.
- **Modular Design**: Each tool is a separate module for clean code.

Enjoy your productivity journey, Aditya!
