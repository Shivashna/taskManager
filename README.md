# Task Manager

## What Is The Purpose Of This Program And Who Can Use It?

This program is designed to help small businesses manage tasks assigned to each member of their team. This project is useful as it would allow small business owners to keep track of their employees and the progress of the business as well.

## Describing The Program

When the program runs, the user will be prompted to enter their username and password. If the username or password is incorrect, the program will display a suitable message and repeatedly ask the user to enter a correct username and password until the username and password matches one stored in the textfile called 'user.txt'. Once the user enters a correct username and password, a menu will be displayed to the user.

If the username entered is 'admin', the following menu will be displayed to the user :

r  - register user
a  - add task
va - view all tasks
vm - view my tasks
gr - generate reports
ds - display statistics
e  - exit

Else for any other user the following menu will be displayed:

r  - register user
a  - add task
va - view all tasks
vm - view my tasks
e  - exit

## Registering A User

Only a user with the username 'admin' is allowed to register a new user. When this option is chosen, the user will be prompted to enter a username and password for the new user. The user will then be asked to confirm the password. If the password confirmation is incorrect, the program will display a suitable message and repeatedly ask the user to confirm their password until it matches the password they entered previously. Once the user enters the correct password, the username and password of the new user will be stored in 'user.txt' textfile and the above menu will be displayed again.

## Adding A Task

When this option is selected, the user will be asked to enter :

*the username of the person the task is being assigned to 
*the title of the task 
*a description of the task and
*the due date of the task

Once this information has been entered by the user it will be stored in the text file 'tasks.txt' and the main menu will displayed again.

## Viewing All Tasks

When this option is selected, all the tasks from the text file 'tasks.txt' will be displayed in an easy to read manner.

## Viewing My Tasks

If the user selects this option, all the tasks assigned to the user will be displayed in an easy to read manner. The user can select to either mark a task as complete or edit a task by entering the task number. If the user selects to mark a task as complete, the program will mark the selected task as complete. If the user chooses to edit a task, they can either choose to edit the username that the task has been assigned to or change the due date of the task. In the first case, the program will ask the user to enter the username they wish to assign the task to. In the second case, the program will ask the user to enter the new due date. In both cases, the information stored for that specific task in the text file 'tasks.txt' will be edited and saved and the main menu will be displayed again.

## Generating reports

When the user selects this option the following will take place :

A text file named 'task_overview.txt' will be generated. The following information will be written to this text file and displayed :

  * The total number of tasks
  * The total number of completed tasks
  * The total number of incomplete tasks
  * The total number of tasks that are incomplete and overdue
  * The percentage of tasks that are incomplete
  * The percentage of tasks that are overdue

A text file name 'user_overview.txt' will be generated. The following information will be written to this text file and displayed :

  * The total number of users
  * The total number of tasks
  * For each user :
     a) The total number of tasks assigned to that user
     b) The percentage of total tasks assigned to that user
     c) The percentage of total tasks assigned to that user that have been completed
     d) The percentage of tasks assigned to that user that are still incomplete
     e) The percentage of tasks assigned to the user that are incomplete and overdue

Once the above information has been written to respective text files and displayed on screen, the main menu will be displayed again.

## Displaying Statistics

When this option is selected, the total number of tasks and the total number of users are displayed in a user friendly manner. The main menu will be displayed again.

## Exiting The Program

The program will execute and the main menu will be always be displayed until the user chooses to exit the program.

## Maintainability Of The Code

This program will be easy to maintain as it makes use of modular programming. This means that the code is written in parts or modules. If there is an error in one part of the code, the rest of the code will not be affected, or if a feature needs to be updated, you can simply update the part of the code that needs to updated without it affecting the rest of the code

## How To Access This Code And It Working

Simply download and install Python and run this code(press F5)! As easy as that!
