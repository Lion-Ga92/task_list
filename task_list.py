print("Welcome to our script, valid inputs are Complete and Not Complete")
print("To exit app you must type 'quit'")


def check_list():
    task_1 = "Cut corn"
    task_2 = "Peel corn"
    global run
    task_list = []
    c_t1_check = input("Have you completed task 1? ")
    if c_t1_check == "Complete":
        task_list.append((task_1, c_t1_check))
        return print(task_list)
    elif c_t1_check == "Not complete":
        task_list.append((task_1, c_t1_check))
        return print(task_list)
    c_t2_check = input("Have you comp. task 2? ")
    if c_t2_check == "Complete":
        task_list.append((task_2, c_t2_check))
        return print(task_list)
    elif c_t2_check == "Not complete":
        task_list.append((task_2, c_t2_check))
    if c_t1_check == "quit":
        run = False


run = True
while run:
    check_list()