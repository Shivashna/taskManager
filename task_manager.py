# The purpose of this program is to help a small business manage tasks assigned to each member of the team


# DEFINING FUNCTIONS

# Creating a function to return the users choice from the option menu
def option_choice(username):
    if (username == "admin"):
        option = (input("\nPlease enter one of the following options :\nr\t- register user\na\t- add task\nva\t- view all tasks\nvm\t- view my tasks\ngr\t- generate reports\nds\t- display statistics\ne\t- exit\n\nSimply enter the key letter/s for the option you want to select : ")).lower()
    else:
        option = (input("\nPlease enter one of the following options :\nr\t- register user\na\t- add task\nva\t- view all tasks\nvm\t- view my tasks\ne\t- exit\n\nSimply enter the key letter/s for the option you want to select : ")).lower()
    return option



# Creating a function to register a new user
def reg_user(username):
    if (username == "admin"):
        new_username = (input("\nEnter a username : "))

        # Creating a list that stores all the usernames from the textfile 'user.txt'
        for line in user:
            user_list = line.split()
            username_text = user_list[0].strip(",")
            username_list.append(username_text)

        # Checking if the username being entered already exists in the list created above
        if (new_username in username_list):
            while (new_username in username_list):
                print("This username already exists!")
                new_username = (input("\nEnter a username : "))       
        

        new_password = (input("Enter a password : "))
        confirm_new_password = (input("Confirm your password : "))


        if (confirm_new_password == new_password):
            user_string = "\n" + new_username + ", " + new_password
            with open('user.txt','a')as users:
                user.write(user_string)
            print("{} has been added as a user.".format(new_username))

        else :
            print("Incorrect password confirmation")
            while (confirm_new_password != new_password):
                confirm_new_password = (input("Try confirming your password again : "))


            user_string = "\n" + new_username + ", " + new_password
            with open('user.txt','a')as users:
                user.write(user_string)
            print("{} has been added as a user.".format(new_username))
            
    else :
        print("\nYou are not allowed to register a new user!")



# Creating a function to add a new task
def add_task():
    username_task = (input("\nEnter the username of the person the task is being assigned to : "))
    task_title = input("Enter the title of the task : ")
    task_description = input("Enter a short description of the task : ")
    due_date = input("Enter the due date of the task (e.g. 10 October 2020) : ")
    today = date.today()
    current_date = today.strftime("%d %B %Y")
    task_completed = "No"
    task_string = username_task + ", " + task_title + ", " + task_description + ", " + str(current_date) + ", " + due_date + ", " + task_completed
    with open ('tasks.txt','a')as tasks_file:
        tasks_file.write("\n" + task_string)
    print("\nTask has been added to the text file 'tasks.py'")



def view_all():
    with open('tasks.txt','r') as tasks:
        task_data_list = tasks.readlines()#or we could use 'read().split("\n")'
        for i in range(len(task_data_list)):
            task_line_list = task_data_list[i].split(", ")
            task_username_txt = task_line_list[0]
            task_title_txt = task_line_list[1]
            task_description_txt = task_line_list[2]
            task_assigned_date_txt = task_line_list[3]
            task_due_date_txt = task_line_list[4]
            task_completed_txt = task_line_list[5]
            print("\nUsername\t: {}\nTask title\t: {}\nTask description: {}\nAssigned Date\t: {}\nDue date\t: {}\nTask completed\t: {}\n\n".format(task_username_txt,task_title_txt,task_description_txt,task_assigned_date_txt,task_due_date_txt,task_completed_txt))



def view_mine(username):
    i = 1
    with open('tasks.txt','r') as tasks:
        task_data_list = tasks.readlines()#or we could use 'read().split("\n")'    
        for j in range(len(task_data_list)):
            task_line_list = task_data_list[j].split(", ")
            task_username_txt = task_line_list[0]
            task_title_txt = task_line_list[1]
            task_description_txt = task_line_list[2]
            task_assigned_date_txt = task_line_list[3]
            task_due_date_txt = task_line_list[4]
            task_completed_txt = task_line_list[5].strip("\n")
            correct_task_list = [task_username_txt,task_title_txt,task_description_txt,task_assigned_date_txt,task_due_date_txt,task_completed_txt]
            task_dict[i] = correct_task_list # Creating a dictionary to assign a number to each task(line) in the text file 'tasks.txt'
            

            if (username == task_username_txt): 
                print("\nTask number\t: {}\nUsername\t: {}\nTask title\t: {}\nTask description: {}\nAssigned Date\t: {}\nDue date\t: {}\nTask completed\t: {}\n\n".format(i,task_username_txt,task_title_txt,task_description_txt,task_assigned_date_txt,task_due_date_txt,task_completed_txt))

            i = i + 1

        task_number = int(input("\nSelect a specific task by entering the task number or enter '-1' to return to the main menu : "))
        if (task_number == -1) :
            return
        else:    
            task_choice = int(input("\nEnter the number of the option you would like to select :\n1\t- Mark task as complete\n2\t- Edit task\nOption\t: "))
            # Marking a task as complete
            if (task_choice == 1):
                print("\nYou have selected to mark a task as complete.")
                dict_list = task_dict[task_number]
                dict_list[5] = "Yes"
                dict_string = dict_list[0] + ", " + dict_list[1] + ", " + dict_list[2] + ", " + dict_list[3] + ", " + dict_list[4] + ", " + dict_list[5] + "\n"  
                    
                with open('tasks.txt','r') as tasks:
                    list_of_lines = tasks.readlines()
                    list_of_lines[task_number-1] = dict_string
                    with open('tasks.txt','w') as task:
                        task.writelines(list_of_lines)
                    
                print("\nThe task has been marked as completed.")
            # Editing a task
            elif (task_choice == 2):
                print("\nYou have selected to edit a task.")

                with open('tasks.txt','r') as tasks:
                    task_data_list = tasks.readlines()
                    task_line_list = task_data_list[task_number-1].split(", ")
                    task_completed = task_line_list[5].strip("\n")
                    if (task_completed == "Yes"):
                        print("\nYou cannot edit this task as it has already been completed.")
                    elif (task_completed == "No"):
                        task_edit = int(input("\nEnter the number of the option you would like to select :\n1\t- Edit the username\n2\t- Edit the due date\nOption\t: "))
                        # Editing the username of the selected task
                        if (task_edit == 1):
                            print("\nYou have selected to edit the username of task number " + str(task_number))
                            changed_username = input("\nEnter the username you want to assign the task to : ")
                            dict_list = task_dict[task_number]
                            dict_list[0] = changed_username
                            dict_string = dict_list[0] + ", " + dict_list[1] + ", " + dict_list[2] + ", " + dict_list[3] + ", " + dict_list[4] + ", " + dict_list[5] + "\n"

                            with open('tasks.txt','r') as tasks:
                                list_of_lines = tasks.readlines()
                                list_of_lines[task_number-1] = dict_string
                                with open('tasks.txt','w') as task:
                                    task.writelines(list_of_lines)
                            print("\nThe username of the selected task has been changed.")    
                        # Editing the due date of the selected task
                        elif (task_edit == 2):
                            print("\nYou have selected to edit the due date of task number " + str(task_number))
                            changed_due_date = input("\nEnter the new due date(e.g. 10 October 2020) : ")
                            dict_list = task_dict[task_number]
                            dict_list[4] = changed_due_date
                            dict_string = dict_list[0] + ", " + dict_list[1] + ", " + dict_list[2] + ", " + dict_list[3] + ", " + dict_list[4] + ", " + dict_list[5] + "\n"

                            with open('tasks.txt','r') as tasks:
                                list_of_lines = tasks.readlines()
                                list_of_lines[task_number-1] = dict_string
                                with open('tasks.txt','w') as task:
                                    task.writelines(list_of_lines)
                            print("\nThe due date of the selected task has been changed.")
    


def display_stats():
    num_users = 0
    num_tasks = 0
    with open('user.txt','r+')as user:
        user_data = user.read()
        user_data_list = user_data.split("\n")
        for x in user_data_list:
            if x:
                num_users = num_users + 1

    with open('tasks.txt','r+')as tasks:
        task_data = tasks.read()
        task_data_list = task_data.split("\n")
        for y in task_data_list:
            if y:
                num_tasks = num_tasks + 1        

    print("\nStatistics :")
    print(f"\nTotal number of users\t: {num_users}")
    print(f"Total number of tasks\t: {num_tasks}")
    



def generate_reports():
    # Defining variables, lists and dictionaries
    num_users = 0
    num_tasks = 0
    i = 1
    task_dict = {}
    count_completed = 0
    count_uncompleted = 0
    count_overdue = 0
    count_num_tasks_user = 0
    user_num_tasks_dict = {}
    num_tasks_percentage_dict = {}
    percentage_task_completed_dict = {}
    percentage_task_uncompleted_dict = {}
    count_user_completed = 0
    count_user_incomplete = 0
    percentage_task_overdue_dict = {}
    count_user_overdue = 0

    # Generating text files 'user_overview.txt' and 'task_overview.txt'
    with open('user_overview.txt','w')as user_overview:
        with open('task_overview.txt','w')as task_overview:
            with open('user.txt','r+')as user:
                with open('tasks.txt','r+')as tasks:

                    # Storing data from text files into respective lists
                    user_data_list = user.read().split("\n")
                    task_data_list = tasks.read().split("\n")

                    # Information for text file 'task_overview.txt'

                    # Finding the number of tasks 
                    for y in task_data_list:
                        if y:
                            num_tasks = num_tasks + 1

                    # Finding the number of completed and uncompleted tasks
                    for i in range(len(task_data_list)-1):
                        task_line_list = task_data_list[i].split(", ")
                        if (task_line_list[5] == "Yes"):
                            count_completed += 1
                        elif (task_line_list[5] == "No"):
                            count_uncompleted += 1

                            # Determining the number of over-due tasks
                            task_due_date_str = task_line_list[4]
                            task_due_date = datetime.datetime.strptime(task_due_date_str, "%d %B %Y")
                            task_due_date = task_due_date.date()
                            current_date = date.today()
                            check_overdue = current_date > task_due_date
                            if check_overdue == True :
                                count_overdue += 1

                    # Calculating the total percentage of incomplete tasks
                    percentage_incomplete = round(((count_uncompleted/num_tasks) * 100),2)
                    # Calculating the total percentage of overdue tasks
                    percentage_overdue = round(((count_overdue/num_tasks)*100),2)

                    # Writing all the required information to 'task_overview.txt'
                    with open('task_overview.txt','a')as task_overview:
                        task_overview.write("The total number of tasks : " + str(num_tasks) + "\n")
                        task_overview.write("The total number of completed tasks : " + str(count_completed) + "\n")
                        task_overview.write("The total number of incomplete tasks : " + str(count_uncompleted) + "\n")
                        task_overview.write("The total number of tasks that are incomplete and overdue : " + str(count_overdue) + "\n")
                        task_overview.write("The percentage of tasks that are incomplete : " + str(percentage_incomplete) + "%\n")
                        task_overview.write("The percentage of tasks that are overdue : " + str(percentage_overdue) + "%\n")

                    # Displaying all the data from 'task_overview.txt'
                    with open('task_overview.txt','r')as task_overview:
                        task_overview_data_list = task_overview.read().split("\n")
                        print("\n")
                        print("Task Overview Report :\n")
                        for t in range(len(task_overview_data_list)-1):
                            print(str(task_overview_data_list[t]))
                        print("\n")

                    # Information for text file 'user_overview.txt'

                    # Finding the number of users
                    for x in user_data_list:
                        if x:
                            num_users = num_users + 1

                    # Determining how many tasks are assigned to each user and storing this information in a dictionary
                    for j in range(1,(num_users+1)):
                        user_line_list = user_data_list[j-1].split(", ")
                        username_user_text = user_line_list[0]
                        count_num_tasks_user = 0
                        count_user_completed = 0
                        count_user_incomplete = 0
                        count_user_overdue = 0

                        for k in range(1,(num_tasks+1)):
                            task_line_list = task_data_list[k-1].split(", ")
                            username_task_text = task_line_list[0]
                            task_completed_text = task_line_list[5]

                            if (username_user_text == username_task_text):
                                count_num_tasks_user += 1
                                user_num_tasks_dict[username_user_text] = count_num_tasks_user # Total number of tasks per each user
                                num_tasks_percentage_dict[username_user_text] = round((((user_num_tasks_dict[username_user_text])/num_tasks)*100),2)
                                if (task_completed_text == "Yes"):
                                    count_user_completed += 1
                                    percentage_task_completed_dict[username_user_text] = round(((count_user_completed/num_tasks)*100),2) # percentage of tasks completed for each user user
                                elif (task_completed_text == "No"):
                                    count_user_incomplete += 1
                                    percentage_task_uncompleted_dict[username_user_text] = round(((count_user_incomplete/num_tasks)*100),2) # percentage of tasks for each user that has not been completed yet

                                    # Determining the number of over-due tasks
                                    tasks_due_date_str = task_line_list[4]
                                    tasks_due_date = datetime.datetime.strptime(tasks_due_date_str, "%d %B %Y")
                                    tasks_due_date = tasks_due_date.date()
                                    current_date = date.today()
                                    check_over_due = current_date > tasks_due_date

                                    if check_over_due == True :
                                        count_user_overdue += 1
                                        percentage_task_overdue_dict[username_user_text] = round(((count_user_overdue/num_tasks)*100),2) # percentage of tasks overdue for each user

                    # Finding the keys(useranmes) of the dictionaries created above
                    user_num_tasks_dict_keys = user_num_tasks_dict.keys()
                    percentage_task_completed_dict_keys = percentage_task_completed_dict.keys()
                    percentage_task_uncompleted_dict_keys = percentage_task_uncompleted_dict.keys()
                    percentage_task_overdue_dict_keys = percentage_task_overdue_dict.keys()

                    # Writing all the required information to 'user_overview.txt'
                    with open('user_overview.txt','a')as user_overview:
                        user_overview.write("The total number of registered users : " + str(num_users) + "\n")
                        user_overview.write("The total number of generated tasks : " + str(num_tasks) + "\n\n")
                        for a in range(1,(num_users+1)):
                            user_line_list = user_data_list[a-1].split(", ")
                            username_user_text = user_line_list[0]
                            user_overview.write(str(username_user_text) + ":\n")
                            if (username_user_text in user_num_tasks_dict_keys) :
                                user_overview.write("Total number of tasks assigned : " + str(user_num_tasks_dict[username_user_text]) + "\n")
                                user_overview.write("percentage of total number of tasks assigned : " + str(num_tasks_percentage_dict[username_user_text]) + "%\n")

                                if (username_user_text in percentage_task_completed_dict_keys) : 
                                    user_overview.write("percentage of total number of completed tasks : " + str(percentage_task_completed_dict[username_user_text]) + "%\n")
                                else :
                                    user_overview.write("percentage of total number of completed tasks : 0%\n")

                                if (username_user_text in percentage_task_uncompleted_dict_keys):    
                                    user_overview.write("percentage of total number of incomplete tasks : " + str(percentage_task_uncompleted_dict[username_user_text]) + "%\n")
                                else :
                                    user_overview.write("percentage of total number of incomplete tasks : 0%\n")

                                if (username_user_text in percentage_task_overdue_dict_keys):    
                                    user_overview.write("percentage of total number of incomplete and overdue tasks : " + str(percentage_task_overdue_dict[username_user_text]) + "%\n\n")
                                else :
                                    user_overview.write("percentage of total number of incomplete and overdue tasks : 0%\n\n")

                            else:
                                user_overview.write("Total number of tasks assigned : 0\n")
                                user_overview.write("percentage of total number of tasks assigned : 0%\n")
                                user_overview.write("percentage of total number of completed tasks : 0%\n")
                                user_overview.write("percentage of total number of incomplete tasks : 0%\n")
                                user_overview.write("percentage of total number of incomplete and overdue tasks : 0%\n\n")

                    # Displaying all the data from 'user_overview.txt'
                    with open('user_overview.txt','r')as user_overview:
                        user_overview_data_list = user_overview.read().split("\n")
                        print("\n")
                        print("User Overview Report :\n")
                        for t in range(len(user_overview_data_list)-1):
                            print(str(user_overview_data_list[t]))
                        print("\n")
    




# PROGRAM

from datetime import date
import datetime
# Asking the user to enter their username and password
username = (input("Please enter your username : "))
password = (input("Please enter your password : "))

# Defining variables, lists and dictionaries
user_list = []
username_list = []
password_list = []
username_password = False
num_users = 0
num_tasks = 0
i = 1
task_dict = {}
count_completed = 0
count_uncompleted = 0
count_overdue = 0
count_num_tasks_user = 0
user_num_tasks_dict = {}
num_tasks_percentage_dict = {}
percentage_task_completed_dict = {}
percentage_task_uncompleted_dict = {}
count_user_completed = 0
count_user_incomplete = 0
percentage_task_overdue_dict = {}
count_user_overdue = 0



# Opening the required textfiles
with open('tasks.txt','r+') as tasks:
    with open('user.txt','r+')as user:

        # Looping through each line in the 'user.txt' textfile
        for line in user:

            # Converting the line into a list so that its easier to work with
            user_list = line.split()
            username_text = user_list[0].strip(",")
            username_list.append(username_text)# Storing all usernames in a list
            password_text = user_list[1]
            password_list.append(password_text)# Storing all passwords in a list


        # Checking if username and password are valid
        if (username in username_list) and (password in password_list):
            username_password = True    


        # If username or password isn't valid, the program will repeatedly ask the user to enter a username and password until it matches one in the text file 'user.txt'
        while (username_password == False) :
            print("The username or password you have entered is invalid.")
            username = (input("Please enter a valid username : "))
            password = (input("Please enter a valid password : "))
            if (username in username_list) and (password in password_list):
                username_password = True



        # Calling the function 'option_choice' to display an option menu to the user   
        option = option_choice(username)



        while (option != "e"):
            # If the user chooses 'r', the program first checks whether the username is 'admin'
            # If the username is 'admin', the program will prompt for details to register a new user
            # Else, an appropriate message is displayed
            if (option == "r"):
                reg_user(username)
                option = option_choice(username)

            

            # If the user chooses 'a', they must provide details to assign a task to a specific user
            elif (option == "a"):
                add_task()
                option = option_choice(username)



            # If the user chooses 'va', all the tasks assigned to each team member will be displayed in an easy-to-read format
            elif (option == "va"):
                view_all()
                option = option_choice(username)



            # If the user chooses 'vm', all the tasks assigned to the user will be displayed in a easy-to-read format
            elif (option == "vm"):
                view_mine(username)
                option = option_choice(username)



            # If a user chooses 'gr', 2 textfiles are generated and all the data from these textfiles will be displayed in a user-friendly manner
            elif (option == "gr"):
                generate_reports()                   
                option = option_choice(username)                      
                            

                                
            # If the user chooses 'ds', the total numbers of users and the total number of tasks will be displayed
            elif (option == "ds"):
                display_stats()
                option = option_choice(username)



            # If the user chooses 'e', the program will print 'Goodbye!' and the user will so-call 'exit'the program    
            elif (option == "e"):
                print("\nGoodbye!")                
