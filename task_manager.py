#=====importing libraries===========
import time
import datetime
from datetime import date
import os
import sys

def get_path():
  return(os.path.dirname(os.path.realpath(sys.argv[0])))

data_path = get_path()

#============= define classes and functions ====================
# copied from https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
class bcolors:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKCYAN    = '\033[96m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'


# checks due date is less than current date
def compare_time(first_time, second_time):
  d_obj1 = datetime.datetime.strptime(first_time, '%d %b %Y')
  d_obj2 = datetime.datetime.strptime(second_time, '%d %b %Y')
  
  mon1 = str(d_obj1.month)
  if len(mon1) == 1:
    mon1 = '0' + mon1
  
  mon2 = str(d_obj2.month)
  if len(mon2) == 1:
    mon2 = '0' + mon2
  
  day1 = str(d_obj1.day)
  if len(day1) == 1:
    day1 = '0' + day1
  
  day2 = str(d_obj2.day)
  if len(day2) == 1:
    day2 = '0' + day2
  
  st1 = "".join([str(d_obj1.year),mon1,day1])
  st2 = "".join([str(d_obj2.year),mon2,day2])
  return(int(st1) <= int(st2))


# print display of task components
def print_list(temp_list):
  print(f"Task:                    {temp_list[1]}")
  print(f"Assigned to:             {temp_list[0]}")
  print(f"Date assigned:           {temp_list[4]}")
  print(f"Due date:                {temp_list[3]}")
  print(f"Task complete?           {temp_list[5]}")
  print("Task descreption:")
  print(temp_list[2])
  print("*******************************************\n")


# register user according to tested conditions
def reg_user(users_names, users_passes, data_path, users_file, new_user, new_pass, new_passC):
    with open(data_path + users_file, 'a+') as f:
        f.write('\n' + new_user + ', ' + new_pass)
        users_names.append(new_user)
        users_passes.append(new_pass)
    return([users_names, users_passes])


# add tasks to file and current session
def add_task(data_path, tasks_file, tasked_person, tasks_list):
    task_title = input("Please give a title for the task. ")
    task_description = input("Please give a description of the task and. ")
    task_due_date = input("Please geve the due date of the task eg 10 Oct 2019: ")
    date_today = date.today().strftime("%d %b %Y")
    task = tasked_person + ', ' + task_title + ', ' + task_description + ', ' + task_due_date + ', ' + date_today + ', ' + 'No\n'
    tasks_list.append(task.split(', '))
    with open(data_path + tasks_file, 'a+') as f:
      f.write(task)

    return(tasks_list)


# view all tasks by owner only
def view_all(data_path, tasks_file):
  with open(data_path + tasks_file, 'r+') as f:
    counter = 0
    for line in f:
      counter += 1
      temp_list = line.split(', ')
      if len(temp_list[0]) > 1:
        print(f"Task No: {counter}\n")
        print_list(temp_list)

# view current user tasks
def view_mine(data_path, tasks_file, user_n):
  with open(data_path + tasks_file, 'r+') as f:
    counter = 0
    for line in f:
      counter += 1
      temp_list = line.split(', ')
      if temp_list[0] == user_n:
        print(f"Task No: {counter} \n")
        print_list(temp_list)


#======================================= main function ===================
def run_manager(data_path):
  
    #-------------------- Declaire variables ---------------------
    users_names = []
    users_passes = []
    tasks_list = []
    temp_list = []              # a list that may change throught the program
    owner = 'admin'             # the owner or higher permission login name
    users_file = '\\users.txt'
    tasks_file = '\\tasks.txt'
    tasks_report = '\\task_overview.txt'
    users_report = '\\user_overview.txt'
    user_n = ''                 # is a single user name variable
    user_p = ''                 # is a single user pass variable

    #--------------------- Reading users
    with open(data_path + users_file, 'r+') as f:
      for line in f:
        temp_list = line.split(', ')
        users_names.append(temp_list[0])
        users_passes.append(temp_list[1].replace('\n', ''))

    #--------------------- Reading tasks
    with open(data_path + tasks_file, 'r+') as f:
      for line in f:
          tasks = line.split(', ')
          tasks_list.append(tasks)

    #--------------------- Login Section
    user_n = input(f"{bcolors.OKBLUE}{bcolors.UNDERLINE}Please type in a valid username: {bcolors.ENDC}")
    user_p = input(f"{bcolors.OKBLUE}{bcolors.UNDERLINE}Please type in a valid password: {bcolors.ENDC}")
    os.system('cls')
    while True:
        # check validity of username and password
        if user_p in users_passes and user_n in users_names:
                print("\n")
                if user_n == owner:
                  menu = input('''Please select one of the following Options:
                  r  - Register a new user
                  a  - Add a new task
                  et - Edit my tasks
                  dt - Delete tasks
                  va - View all tasks
                  vm - View my tasks
                  ds - Display statistics
                  gr - Generate reports
                  e  - Exit
                  : ''').lower()
                  os.system('cls')
                else:
                  menu = input('''Please select one of the following Options:
                  a  - Add a new task
                  et - Edit my task
                  vm - View my task
                  e  - Exit
                  : ''').lower()
                  os.system('cls')
          
        else:
            print(f"{bcolors.WARNING}Username and password do not much! {bcolors.ENDC}")
            user_n = input(f"{bcolors.OKBLUE}Please type in a valid username: {bcolors.ENDC}")
            user_p = input(f"{bcolors.OKBLUE}Please type in a valid password: {bcolors.ENDC}")
            os.system('cls')
            continue

        #------------------ register new user can only be done by owner 
        if menu == 'r' and user_n == owner:
            new_user = input(f"{bcolors.OKGREEN}Please type in a valid username: {bcolors.ENDC}")
            new_pass = input(f"{bcolors.OKGREEN}Please type in a valid password: {bcolors.ENDC}")
            new_passC= input(f"{bcolors.OKGREEN}Please confirm password: {bcolors.ENDC}")
            os.system('cls')
            if new_pass == new_passC and not(new_pass in users_passes) and not(new_user in users_names):
                result = reg_user(users_names, users_passes, data_path, users_file, new_user, new_pass, new_passC)
                users_names = result[0]
                users_passes = result[1]
            else:
                print(f"{bcolors.OKGREEN}There is a problem with password or username! {bcolors.ENDC}")

        #----------------- add task: anyone can add tasks to any other member including themselves
        elif menu == 'a':
            tasked_person = input("A username of the person whom the task is assigned to: ")
            if  tasked_person in users_names:
                tasks_list = add_task(data_path, tasks_file, tasked_person, tasks_list)
            else:
                print(f"{bcolors.OKGREEN}User not in data base. {bcolors.ENDC}")


        #----------------- view all records: can only be done by admin
        elif menu == 'va' and user_n == owner:
            view_all(data_path, tasks_file)


        #----------------- View my 'active user' records only
        elif menu == 'vm':
            view_mine(data_path, tasks_file, user_n)


        #----------------- Delete task can only be done by admin 'owner'
        elif menu == 'dt' and user_n == owner:
            inputDT = input(f"Please type in the task {bcolors.OKGREEN}number{bcolors.ENDC}: ")
            if not inputDT.isalpha():
              del_task = int(inputDT)-1
              if del_task in range(len(tasks_list)):
                flag = input("Are you sure?   y/n")
                os.system('cls')
                if flag == 'y':
                  tasks_list.pop(del_task)
                  with open(data_path + tasks_file, 'w') as f:
                    for line in tasks_list:
                      f.write(", ".join(line).replace('\n', ''))
                      f.write('\n')
                
              else:
                print(f"{bcolors.OKGREEN}Task do not exist.{bcolors.ENDC}")
            else:
              print(f"{bcolors.OKGREEN}Non numeric input.{bcolors.ENDC}")
              continue
        

        #----------------- Edit task can only be done by current user to his/her own tasks.
        elif menu == 'et':
            inputET = input(f"Please type in the task {bcolors.OKGREEN}number:{bcolors.ENDC} ")
            if not inputET.isalpha():
              task_number = int(inputET)-1
              if task_number in range(len(tasks_list)):
                target_task = tasks_list[task_number]
                if target_task[0] == user_n:
                  counter = 0
                  target_task = tasks_list[task_number]
                  for item in target_task:
                    if counter != 4:
                      print(f"{bcolors.OKGREEN}Text to be modified:{bcolors.ENDC} {item} ")
                      new_value = input(f"{bcolors.OKGREEN}Please type in the new value or 'Enter' to skip.{bcolors.ENDC} ")
                      if new_value != '':
                        target_task[counter] = new_value
                        counter += 1
                      else:
                        counter += 1
                    else:
                      counter += 1
                      continue
                  tasks_list[task_number] = target_task
                  
                  with open(data_path + tasks_file, 'w') as f:
                    for line in tasks_list:
                      f.write(", ".join(line).replace('\n', ''))
                      f.write('\n')
                else:
                  print(f"{bcolors.OKGREEN}Sorry! you don't have permission{bcolors.ENDC}")      
              else:
                print(f"{bcolors.OKGREEN}Task do not exist.{bcolors.ENDC}")
            else:
              print(f"{bcolors.OKGREEN}Non numeric input.{bcolors.ENDC}")
              continue
            
            
        #-------------------- display statistics can only be done by admin
        elif menu == 'ds' and user_n == owner:
            all_completed_tasks = 0
            all_uncompleted_tasks = 0
            over_due_tasks = 0
            #----- tasks statistics
            for i in range(len(tasks_list)):
              if tasks_list[i][5].replace('\n', '') == 'Yes':
                all_completed_tasks += 1
              else:
                all_uncompleted_tasks += 1
              
              if compare_time(tasks_list[i][3], date.today().strftime("%d %b %Y")) and tasks_list[i][5].replace('\n', '') == 'No':
                over_due_tasks += 1
              else:
                continue
            
            print("============  All Tasks Report   ============\n")   
            print(f"The number of users is:              {len(users_names)}")
            print(f"The number of tasks is:              {len(tasks_list)}")
            print(f"The number of completed tasks is:    {all_completed_tasks}")
            print(f"The number of uncomplete tasks is:   {all_uncompleted_tasks}")
            print(f"The number of overdue tasks is:      {over_due_tasks}")
            print(f"The percentage of uncomplete tasks:  {int((all_uncompleted_tasks/len(tasks_list))*100)}%")
            print(f"The percentage of overdue tasks:     {int(((over_due_tasks)/len(tasks_list))*100)}%")
            print('\n')
            
            
            #----- Users statistics
            for user in users_names:
                all_completed_tasks = 0
                all_uncompleted_tasks = 0
                over_due_tasks = 0
                all_user_tasks = 0
                for i in range(len(tasks_list)):
                  if tasks_list[i][0] == user:
                    all_user_tasks += 1
                    if tasks_list[i][5].replace('\n', '') == 'Yes':
                      all_completed_tasks += 1
                    else:
                      all_uncompleted_tasks += 1
                    
                    if compare_time(tasks_list[i][3], date.today().strftime("%d %b %Y")) and tasks_list[i][5].replace('\n', '') == 'No':
                      over_due_tasks += 1
                    else:
                      continue
                    
                if all_user_tasks >= 1:
                        print("================= By User Reprots =============")
                        print(f"User Name: {user} --------------------------\n")
                        print(f"The number of user tasks is:             {all_user_tasks}")
                        print(f"The percentage of all tasks:             {int((all_user_tasks/len(tasks_list))*100)}%")
                        print(f"The percentage of user complete tasks:   {int((all_completed_tasks/all_user_tasks)*100)}%")
                        print(f"The percentage of user uncomplete tasks: {int((all_uncompleted_tasks/all_user_tasks)*100)}%")
                        print(f"The percentage of user overdue tasks:    {int((over_due_tasks/all_user_tasks)*100)}%")
                        print('\n\n')
            
        #------------------ Generate Reprots
        elif menu == 'gr' and user_n == owner:
            all_completed_tasks = 0
            all_uncompleted_tasks = 0
            over_due_tasks = 0
            for i in range(len(tasks_list)):
              if tasks_list[i][5].replace('\n', '') == 'Yes':
                all_completed_tasks += 1
              else:
                all_uncompleted_tasks += 1
              
              if compare_time(tasks_list[i][3], date.today().strftime("%d %b %Y")) and tasks_list[i][5].replace('\n', '') == 'No':
                over_due_tasks += 1
              else:
                continue
            
            with open(data_path + tasks_report, 'w') as f:
                f.write("========== All Tasks Report ==========\n")
                #f.write(f"The number of users is:              {len(users_names)}")
                #f.write('\n')
                f.write(f"The number of tasks is:              {len(tasks_list)}")
                f.write('\n')
                f.write(f"The number of completed tasks is:    {all_completed_tasks}")
                f.write('\n')
                f.write(f"The number of uncomplete tasks is:   {all_uncompleted_tasks}")
                f.write('\n')
                f.write(f"The number of overdue tasks is:      {over_due_tasks}")
                f.write('\n')
                f.write(f"The percentage of uncomplete tasks:  {int((all_uncompleted_tasks/len(tasks_list))*100)}%")
                f.write('\n')
                f.write(f"The percentage of overdue tasks:     {int(((over_due_tasks)/len(tasks_list))*100)}%")
                f.write('\n')
                
            #---------- Single users reports
            with open(data_path + users_report, 'w') as f:
                f.write('')
            for user in users_names:
                all_completed_tasks = 0
                all_uncompleted_tasks = 0
                over_due_tasks = 0
                all_user_tasks = 0
                for i in range(len(tasks_list)):
                  if tasks_list[i][0] == user:
                    all_user_tasks += 1
                    if tasks_list[i][5].replace('\n', '') == 'Yes':
                      all_completed_tasks += 1
                    else:
                      all_uncompleted_tasks += 1
                    
                    if compare_time(tasks_list[i][3], date.today().strftime("%d %b %Y")) and tasks_list[i][5].replace('\n', '') == 'No':
                      over_due_tasks += 1
                    else:
                      continue
                  
                with open(data_path + users_report, 'a+') as f:
                  if all_user_tasks >= 1:
                    f.write(f"=========== Single User Report ==============\n")
                    f.write(f"User Name: {user} ---------------------------\n")
                    f.write(f"The number of user tasks is:             {all_user_tasks}")
                    f.write('\n')
                    f.write(f"The percentage of all tasks:             {int((all_user_tasks/len(tasks_list))*100)}%")
                    f.write('\n')
                    f.write(f"The percentage of user complete tasks:   {int((all_completed_tasks/all_user_tasks)*100)}%")
                    f.write('\n')
                    f.write(f"The percentage of user uncomplete tasks: {int((all_uncompleted_tasks/all_user_tasks)*100)}%")
                    f.write('\n')
                    f.write(f"The percentage of user overdue tasks:    {int((over_due_tasks/all_user_tasks)*100)}%")
                    f.write('\n\n')
                
                
                    
        #------------------ Exit from the current user session
        elif menu == 'e':
            print('Goodbye!!!')
            break

        else:
            print(f"{bcolors.OKGREEN}You have made a wrong choice, Please Try again{bcolors.ENDC}")
    input(f"\n{bcolors.OKGREEN}Press Enter to continue. {bcolors.ENDC}")


while True:
    os.system('cls')
    run_manager(data_path)
    input("")


# import py_compile
# py_compile.compile('C:\\Users\\rahim\\bootCump\\T26\\task_manager.py')
