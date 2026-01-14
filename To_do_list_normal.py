import os

def open_file():
    # files = []
    # for f in os.listdir():
    #     if f.endswith('.txt'):
    #         files.append(f)
    files = [f for f in os.listdir() if f.endswith('.txt')]

    if not files:
        print("No text files found in the current directory.")
        return None

    print("Available text files:")
    for idx, file in enumerate(files, 1):
        print(f"{idx}. {file}")

    try:
        choice = int(input("Enter the number of the file: "))
        if 1 <= choice <= len(files):
            print(f"Using {files[choice - 1]}")
            return files[choice - 1]
        else:
            print("Invalid choice.")
            return None
    except ValueError:
        print("Invalid input.")
        return None

def create_tasks(file_name):
    if os.path.exists(file_name):
        print(f"'{file_name}' already exists.")
        print("1. Overwrite the file")
        print("2. Use the existing file")
        print("3. Enter a new file name")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            with open(file_name, "w") as file:
                pass
            print(f"'{file_name}' has been overwritten.")
            return file_name

        elif choice == "2":
            print(f"Using the existing file '{file_name}'.")
            return file_name

        elif choice == "3":
            new_file_name = input("Enter a new file name: ").strip()
            if not new_file_name.endswith('.txt'):
                new_file_name += '.txt'
            return create_tasks(new_file_name)

        else:
            print("Invalid choice. Please try again.")
            return create_tasks(file_name)  # Retry
    else:
        with open(file_name, "x") as file:
            pass
        print(f"'{file_name}' has been created.")
        return file_name

    # try:
    #     with open(file_name, "x") as file:
    #         pass
    #     print("List Created")
    # except FileExistsError:
    #     print(f"{file_name} already exists")

def add_tasks(file_name,task):
    with open(file_name, "a") as file:
        file.write(task + "\n")
    print("Task added!")

def view_tasks(file_name):
    try:
        with open(file_name, "r") as file:
            task = file.readlines()
            if task:
                print("Your List: ")
                for i, task in enumerate(task, start=1):
                    print(f"{i}. {task.strip()}")
            else:
                print("List empty")
    except FileNotFoundError:
        print(f"{file_name} doesnt exit")

def mark_complete(file_name, task_num):
    try:
        with open(file_name, "r") as file:
            task = file.readlines()

        if 0 < task_num <= len(task):
            if task[task_num -1].rstrip().endswith("[completed]"):
                print("Already Marked completed")
            else:
                task[task_num - 1] = task[task_num - 1].strip() + " [completed]\n"

                with open(file_name,"w") as file:
                    file.writelines(task)
                print("Marked Completed")
        else:
            print("Invalid Task Number")
    except FileNotFoundError:
        print("Task not found")

def delete_task(file_name, task_num):
    try:
        with open(file_name, "r") as file:
            task=file.readlines()

        if 0 < task_num <= len(task):
            del task[task_num -1]

            with open(file_name, "w") as file:
                file.writelines(task)
            print("Task Deleted")
        else:
            print("Invalid Task Number")
    except FileNotFoundError:
        print("Task not found")

def main():
    file_name = None
        # input("Enter List name:" )
    # if not file_name.endswith('.txt'):
    #     file_name.append(".txt")
    # file_name += '.txt'

    while True:
        print("\n Choose an operation")
        print("1. Open exising List")
        print("2. Create List")
        print("3. Add task ")
        print("4. View task ")
        print("5. Mark complete ")
        print("6. Delete ")
        print("7. Exit ")

        choice = input("Enter your choice: ")

        if choice == "1":
            file_name = open_file()

        elif choice == "2":
            file_name = input("Enter the name for your list: ").strip()
            if not file_name.endswith('.txt'):
                file_name += '.txt'
            file_name = create_tasks(file_name)

        elif choice == "3":
            task = input("Enter the task: ")
            add_tasks(file_name,task)

        elif choice=="4":
            view_tasks(file_name)

        elif choice=="5":
            try:
                task_num=int(input("Enter task number: "))
                mark_complete(file_name, task_num)
            except ValueError:
                print("Invalid Number")

        elif choice=="6":
            try:
                task_number=int(input("Enter task number: "))
                delete_task(file_name, task_number)
            except ValueError:
                print("Invalid Number")

        elif choice=="7":
            break
        else:
            print("invalid")


if __name__== "__main__":
    main()






