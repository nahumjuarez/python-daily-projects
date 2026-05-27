tasks = []

while True:
    print("\nTo-Do List")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")
    
    option = input("Choose any option: ")
    
    if option == "1":
        if len(tasks) == 0:
            print("You don't have any tasks yet.")
        else: 
            print("Your tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        
    elif option == "2":
        new_task = input("Write the new task: ")
        tasks.append(new_task)
        print("Nice, you added a task!")
        
    elif option == "3":
        if len(tasks) == 0:
            print("You don't have any tasks.")
        else: 
            print("Your tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
                
            delete_task = int(input("Enter the task number to delete: "))
            if 1 <= delete_task <= len(tasks):
                removed = tasks.pop(delete_task - 1)
                print(f"Task '{removed}' deleted successfully.")
            else:
                print("Invalid task number.")
        
    elif option == "4":
        print("Goodbye.") 
        break
    
    else:
        print("Invalid option.")