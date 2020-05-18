from sys import exit

print("Welcome to our script, valid inputs are Complete and Not Complete")
print("To exit app you must type 'quit'")


def check_list():
    task_1 = "Cut corn"
    task_2 = "Peel corn"
    task_3 = "Wash pots"
    task_4 = "Clean table"
    task_list = []
    c_t1_check = input("Have you completed task 1? ")
    if c_t1_check == "Complete":
        task_list.append((task_1, c_t1_check))
        print(task_list)
    elif c_t1_check == "Not complete":
        task_list.append((task_1, c_t1_check))
        print(task_list)
    elif c_t1_check == "quit":
        return exit()
    else:
        print("Response not valid")

    c_t2_check = input("Have you comp. task 2? ")
    if c_t2_check == "Complete":
        task_list.append((task_2, c_t2_check))
        print(task_list)
    elif c_t2_check == "Not complete":
        task_list.append((task_2, c_t2_check))
        print(task_list)
    elif c_t2_check == "quit":
        return exit()
    else:
        print("Response not valid")
    c_t3_check = input("Have you completed task 3?? " )
    if c_t3_check == "Complete":
        task_list.append((task_3, c_t3_check))
        print(task_list)
    elif c_t3_check == "Not complete":
        task_list.append((task_3, c_t3_check))
        print(task_list)
    elif c_t3_check == "quit":
        return exit()
    else:
        print("Response not valid")
    c_t4_check = input("Have you completed task 4? ")
    if c_t4_check == "Complete":
        task_list.append((task_4, c_t4_check))
    elif c_t4_check == "Not complete":
        task_list.append((task_4, c_t4_check))
        print(task_list)
    elif c_t4_check == "quit":
        exit()
    else:
        print("Response not valid")

check_list()