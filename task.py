tasks= []

print('-----WELCOME TO THE TASK MANAGEMENT APP-----')

total_task= int(input('Enter how many tasks you want to add: '))
for i in range(1, total_task+1):
    task_name= input(f'Enter task {i}= ')
    tasks.append(task_name)

print(f"Today's tasks are: \n{tasks}")

while True:
    operation= int(input("Enter:\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop/"))
    if operation == 1:
        add= input('Enter task you want to add: ')
        tasks.append(add)
        print(f"Task {add} has been added successfully...")
    
    elif operation == 2:
        update_val= input("Enter a task you want to update: ")
        if update_val in tasks:
            up= input('Enter new task: ')
            ind= tasks.index(update_val)
            tasks[ind]= up
            print(f"Updated task {up}")

    elif operation==3:
        del_val= input("Which task you want to delete: ")
        if del_val in tasks:
            ind= tasks.index(del_val)
            del tasks[ind]
            print(f"Task {del_val} has been deleted....")

    elif operation == 4:
        print(f"Total tasks are: {tasks}")

    elif operation == 5:
        print("Closing the program...")
        break
    else:
        print("Invalid Input")