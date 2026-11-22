# File Management System Project
# A complete CLI-based file CRUD (Create, Read, Update, Delete) application
# using Python's pathlib and file handling context managers.

from pathlib import Path


def readFileAndFolder():
    """Lists all files and folders in the current directory."""
    path = Path('.')
    items = list(path.glob('*'))
    print("\n--- Current Directory Files & Folders ---")
    if not items:
        print("(Directory is currently empty)")
    for i, item in enumerate(items, 1):
        item_type = "[Folder]" if item.is_dir() else "[File]"
        print(f"{i} : {item.name} {item_type}")
    print("-----------------------------------------\n")


def createFile():
    """Creates a new file with initial user content."""
    try:
        readFileAndFolder()
        name = input("Enter new file name (e.g. notes.txt): ").strip()
        p = Path(name)
        
        if not p.exists():
            with open(p, "w") as fs:
                data = input("What do you want to write: ")
                fs.write(data)
            print(f"File '{name}' created successfully!\n")
        else:
            print(f"File '{name}' already exists!\n")
            
    except Exception as err:
        print(f"An error has occurred: {err}\n")


def readFile():
    """Reads and displays the content of an existing file."""
    try:
        readFileAndFolder()
        name = input("Enter file name to read: ").strip()
        p = Path(name)
        
        if p.exists() and p.is_file():
            with open(p, "r") as fs:
                content = fs.read()
                print(f"\n--- Content of '{name}' ---")
                print(content)
                print("---------------------------\n")
        else:
            print(f"File '{name}' does not exist or is not a valid file!\n")
            
    except Exception as err:
        print(f"An error has occurred: {err}\n")


def updateFile():
    """Updates an existing file by appending or overwriting content."""
    try:
        readFileAndFolder()
        name = input("Enter file name to update: ").strip()
        p = Path(name)
        
        if p.exists() and p.is_file():
            print("\nUpdate Options:")
            print("Press 1 to Append content (preserves existing text)")
            print("Press 2 to Overwrite content (wipes existing text)")
            mode_choice = input("Enter choice (1/2): ").strip()
            
            if mode_choice == "1":
                with open(p, "a") as fs:
                    data = input("Enter data to append: ")
                    fs.write("\n" + data)
                print(f"Content appended to '{name}' successfully!\n")
            elif mode_choice == "2":
                with open(p, "w") as fs:
                    data = input("Enter new data to overwrite: ")
                    fs.write(data)
                print(f"File '{name}' overwritten successfully!\n")
            else:
                print("Invalid update choice!\n")
        else:
            print(f"File '{name}' does not exist!\n")
            
    except Exception as err:
        print(f"An error has occurred: {err}\n")


def deleteFile():
    """Deletes an existing file from disk."""
    try:
        readFileAndFolder()
        name = input("Enter file name to delete: ").strip()
        p = Path(name)
        
        if p.exists() and p.is_file():
            confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ").strip().lower()
            if confirm == 'y':
                p.unlink()  # Deletes file using pathlib
                print(f"File '{name}' deleted successfully!\n")
            else:
                print("Deletion cancelled.\n")
        else:
            print(f"File '{name}' does not exist!\n")
            
    except Exception as err:
        print(f"An error has occurred: {err}\n")


# --- Main Menu Loop ---
def main():
    while True:
        print("=" * 40)
        print("        FILE MANAGEMENT SYSTEM          ")
        print("=" * 40)
        print("Press 1 for creating a file")
        print("Press 2 for reading a file")
        print("Press 3 for updating a file")
        print("Press 4 for deleting a file")
        print("Press 5 to Exit")
        print("=" * 40)

        choice = input("Please tell your response: ").strip()

        if choice == "1":
            createFile()
        elif choice == "2":
            readFile()
        elif choice == "3":
            updateFile()
        elif choice == "4":
            deleteFile()
        elif choice == "5":
            print("Exiting File Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 5.\n")


if __name__ == "__main__":
    main()
