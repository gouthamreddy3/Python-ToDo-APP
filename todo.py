tasks = [] 
 
def show_tasks(): 
    if not tasks: 
        print("No tasks in your list!") 
    else: 
        print("\\nYour Tasks:") 
        for i, task in enumerate(tasks, 1): 
            print(f"{i}. {task}") 
    print() 
 
def add_task(): 
    task = input("Enter a new task: ") 
    tasks.append(task) 
    print(f'"{task}" added to your list!\\n') 
 
def remove_task(): 
    show_tasks() 
    try: 
        task_num = int(input("Enter the task number to remove: ")) 
        removed = tasks.pop(task_num - 1) 
        print(f'"{removed}" removed from your list!\\n') 
    except (ValueError, IndexError): 
        print("Invalid task number!\\n") 
 
def menu(): 
    while True: 
        print("To-Do List Menu:") 
        print("1. Show tasks") 
        print("2. Add task") 
        print("3. Remove task") 
        print("4. Exit") 
        choice = input("Enter your choice: ") 
        if choice == '1': 
            show_tasks() 
        elif choice == '2': 
            add_task() 
        elif choice == '3': 
            remove_task() 
        elif choice == '4': 
            print("Bye!") 
            break 
        else: 
            print("Invalid choice! Try again.\\n") 
 
if __name__ == "__main__": 
    menu() 
