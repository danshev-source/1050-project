import doctest
import datetime
def main():
    # Create two empty dictionaries for storage
    main_dict = {}  # High priority tasks
    secondary_dict = {}  # Normal priority tasks
    
    # Main program loop
    while True:
        # Display menu options
        Display()
        
        # Get user choice
        choice = input("Enter your choice (1-6): ")
        
        # Option 1: Add priority task
        if choice == '1':
            Retrieval(main_dict, is_priority=True)
        # If user wants to add a task:
            # 2 commands 1 for priority one for non priority
            # Get task details from user (name, deadline, etc.)
            # if it's priority then add to main_dict
            # if not priority than add to secondary_dict
                #Add helper/subordinate function named calc
                # Calculate reminders for this task
        
        # Option 2: Add normal task
        elif choice == '2':
            Retrieval(secondary_dict, is_priority=False)
        
        # Option 3: View all tasks
        elif choice == '3':
            ShowTask(main_dict, secondary_dict)
        
        # Option 4: Delete a task
        elif choice == '4':
            Deletion(main_dict, secondary_dict)
        # If user wants to delete a task:
            # Ask for task name
            # Remove from whichever dict it's in
        
        # Option 5: Show reminders
        elif choice == '5':
            Reminders(main_dict, secondary_dict)
         # If user wants to see reminders:
            # Show upcoming reminders (main_dict first, then secondary)
        
        # Option 6: Quit program
        elif choice == '6':
            print("Goodbye!")
            break
        # If user wants to quit:
            # Exit programv
        else:
            print("Invalid choice. Please try again.")

def Display():
    """
    Displays the menu options that the user can utilize    
    Menu Options
    # 1. Add Priority Task
    # 2. Add normal task
    # 3. View all tasks
    # 4. Delete a task
    # 5. Show reminders
    # 6. Quit
    # """
    pass
def Retrieval(secondary_dict, is_priority=False):
    """
    Get task details from user and add to dict
    # 1. Prompt the user for task_name (non-empty), deadline (stirng), and optional notes
# 2. Convert date string to datetime.data via Deadlines (deadline) (handle ValueError with a retry message).
# 3. Build a task to dict; set field priority = high if is_priority, else "normal"
# 4. Insert into secondary_dict[task_name] (the argument alias refers to either main or secondary store).
# 5. Print a confirmation
    """
    pass
def ShowTask(main_dict, secondary_dict):
    """
    Display all tasks (prioritized first, next secondary)
    1. Print "HIGH PRIORITY TASKS" header
    # 2. Loop through main_dict and display each task with formatting
    # 3. Print "NORMAL TASKS" header  
    # 4. Loop through secondary_dict and display each task
    # 5. If both dicts are empty, print "No tasks to display"
    """
    pass
def Deletion(main_dict, secondary_dict):
    """Delete task by name from storage"""
    # 1. Ask for task_name
# 2. If task_name in main_dict: del main_dict[task_name], print success
# 3. elif task_name in secondary_dict: delete and print success
# 4. Else: print "Task not found"
    pass
def DeadLines(deadline_date):
    """
    Calculate days until deadline
    # 1. Ask for 'task_name'.
# 2. If task_name in main_dict: del main_dict[task_name], print success.
# 3. elif task_name in secondary_dict: delete and print sucess
# 4. Else: print "Task not found."
    """
    pass
def Reminders(main_dict, secondary_dict):
    """
    Desplay reminders for all tasks
    # 1. Gather all tasks as (name, task) from main_dict then secondary_dict
# 2. For each task:
    # - days_left = calc(date.today(), task["due"])
    # - Else:
    #   - If days_left >= 7: generate reminder dates every 7 days until due
    #   - If 0 <= days_left < 7: generate reminder dates every 1 day until due
# 3. Print task header and its reminder schedule (dates only)
    """
    pass
def calc(startDate, endDate):#helper to reminders
    """
    Calculates # of days between 2 dates 
    # 1. Compute delta = endDate - startDate
# 2. Return delta.days
    """
    pass
def Prioritization(main_dict, secondary_dict, task_name):#major
    """Move task from sec to main(prioritizing this task)
# 1. If task_name in secondary_dict:
    # - task = secondary_dict.pop(task_name)
    # - set task[priority] = "high" (if that field exists)
    # - main_dict[task_name] = task
    # - Print success
# 2. Else: print "Task not found in secondary list"
    """
    pass
def TimeTracker(): #debating to add
    """When task reaches to 2 weeks before due date set reminders to everyday, 
    when task reaches day after due date, call deletion"""#could be extra overdraft(missing assignment) function made
    pass
doctest.testmod()