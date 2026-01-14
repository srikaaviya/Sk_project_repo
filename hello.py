def create_tasks(file_name):
    with open(file_name, "w") as file:
        file.write("Your List: \n")
    print("List Created")

def add_tasks(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added!")

def view_tasks(file_name):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()

            if not lines:
                print("list is empty")
                return
            if not lines[0].startswith("Your List:"):
                lines.insert(0,"Your List: \n")

            task = lines[1:]
            if task:
                # print("\nYour List:")
                # print(task)
                print("Your List: ")
                for i, task in enumerate(task, start=1):
                    print(f"{i}. {task.strip()}")
            else:
                print("List empty")
    except FileNotFoundError:
        print(f"{file_name} doesnt exit")

def mark_complete(task_num):
    try:
        with open("tasks.txt", "r") as file:
            lines = file.readlines()

        if not lines or not lines[0].startswith("Your List:"):
            lines.insert(0, "Your List: \n")

        task = lines[1:]
        if 0 < task_num <= len(task):
            task[task_num -1] = task[task_num - 1].strip() + " [completed]\n"

            with open("tasks.txt","w") as file:
                file.write(lines[0])
                file.writelines(task)
            print("Marked Completed")
        else:
            print("Invalid Task Number")
    except FileNotFoundError:
        print("Task not found")

def delete_task(task_num):
    try:
        with open("tasks.txt", "r") as file:
            task=file.readlines()

        if 0 < task_num <= len(task):
            del task[task_num -1]

            with open("tasks.txt", "w") as file:
                file.writelines(task)
            print("Task Deleted")
        else:
            print("Invalid Task Number")
    except FileNotFoundError:
        print("Task not found")

def main():
    file_name = "tasks.txt"

    while True:
        print("\n choose an operation")
        print("1. Create List")
        print("2. Add task ")
        print("3. View task ")
        print("4. Mark complete ")
        print("5. Delete ")
        print("6. Exit ")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_tasks(file_name)

        elif choice == "2":
            task = input("Enter the task: ")
            add_tasks(task)

        elif choice=="3":
            view_tasks(file_name)

        elif choice=="4":
            try:
                task_num=int(input("Enter task number: "))
                mark_complete(task_num)
            except ValueError:
                print("Invalid Number")

        elif choice=="5":
            try:
                task_number=int(input("Enter task number: "))
                delete_task(task_number)
            except ValueError:
                print("Invalid Number")

        elif choice=="6":
            break
        else:
            print("invalid")


if __name__== "__main__":
    main()






