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


#Major Functions


def Display():
"""Displays the menu options that the user can utilize"""
    print("TASK TRACKER MENU")
    print("1. Add Priority Task")
    print("2. Add Normal Task")
    print("3. View All Tasks")
    print("4. Delete a Task")
    print("5. Show Reminders")
    print("6. Quit")
    print("7. Prioritize a Task")

    pass
def Retrieval(task_dict, is_priority=False):
    """
    Get task details from user and add to dictionary
    
    Args:
        task_dict: Dictionary to store the task (either main_dict or secondary_dict)
        is_priority: Boolean indicating if this is a high priority task
    
    Process:
    1. Prompt user for task_name (non-empty) and deadline (string)
    2. Convert date string to datetime.date via DeadLines (handle ValueError with retry)
    3. Build a task dict; set field priority = "high" if is_priority, else "normal"
    4. Insert into task_dict[task_name]
    5. Print confirmation
    """
    # ASSERTION: Check that function received correct parameter types
    assert isinstance(task_dict, dict), "task_dict must be a dictionary"
    assert isinstance(is_priority, bool), "is_priority must be a boolean"
    
    print("\n--- Add New Task ---")
    
    # Step 1: Get task name (must be non-empty)
    while True:
        task_name = input("Enter task name: ").strip()
        
        # Use IF for user input validation (not assert!)
        if task_name == '':
            print("Error: Task name can't be empty. Please try again.")
            continue
        
        # Check if task already exists
        if task_name in task_dict:
            print(f"Error: Task '{task_name}' already exists. Please use a different name.")
            continue
        
        # Valid task name - break out of loop
        break
    
    # Step 2: Get deadline with error handling
    while True:
        deadline_str = input("Enter deadline (YYYY-MM-DD, e.g., 2025-11-20): ").strip()
        
        try:
            # Convert string to date object using DeadLines function
            deadline_date = DeadLines(deadline_str)
            
            # ASSERTION: Verify DeadLines returned correct type
            assert isinstance(deadline_date, datetime.date), "DeadLines must return a date object"
            
            # Optional: Check if date is in the past
            if deadline_date < datetime.date.today():
                confirm = input("Warning: This date is in the past. Continue? (y/n): ").lower()
                if confirm != 'y':
                    continue
            
            # Valid deadline
            break
            
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")
    
    # Step 3: Build task dictionary
    task_info = {
        "due": deadline_date,
        "priority": "high" if is_priority else "normal"
    }
    
    # ASSERTION: Verify task_info has all required fields
    assert "due" in task_info, "Task must have a due date"
    assert "priority" in task_info, "Task must have a priority level"
    
    # Step 5: Add to dictionary
    task_dict[task_name] = task_info
    
    # ASSERTION: Verify task was actually added
    assert task_name in task_dict, "Task should be in dictionary after adding"
    
    # Step 6: Print confirmation
    priority_label = "HIGH PRIORITY" if is_priority else "NORMAL"
    print(f"\n✓ Task '{task_name}' added successfully as {priority_label}!")
    print(f"  Due: {deadline_date.strftime('%Y-%m-%d')}")
    print()
    
def ShowTask(main_dict, secondary_dict):
    """Display all tasks grouped by priority"""

    if not main_dict and not secondary_dict:
        print("\nNo tasks to display.")
        return

    print("\n===== HIGH PRIORITY TASKS =====")
    for name, info in main_dict.items():
        print(f"\nName: {name}")
        print(f"Due: {info['due'].strftime('%Y-%m-%d')}")
        print(f"Priority: HIGH")
        print("=" * 40)

    print("\n===== NORMAL TASKS =====")
    for name, info in secondary_dict.items():
        print(f"\nName: {name}")
        print(f"Due: {info['due'].strftime('%Y-%m-%d')}")
        print(f"Priority: NORMAL")
        print("=" * 40)

    pass
    
def Deletion(main_dict, secondary_dict):
    """Delete task by name from storage"""
print("Delete Task")
task_name = input("Enter the task name to delete: ").strip()

# Delete from priority dict
if task_name in main _dict:
    del main_dict [task_name]
    print(f"✓ Task '{task_name}' deleted from HIGH PRIORITY list.")
    return
# Delete from normal dict
if task_name in secondary dict:
    del secondary_dict[task_name]
    print(f"✓ Task '{task_name}' deleted from NORMAL list.")
    return
# Not Found
print(f"✗ Task '{task_name}' not found")
    pass


def Reminders(main_dict:dict, secondary_dict:dict):
    """
    Display reminders for all tasks
    
    This function shows reminder schedules for all tasks:
    - For tasks 7+ days away: reminders every 7 days
    - For tasks 0-6 days away: reminders every day
    - For overdue tasks: displays "OVERDUE" message
    """
    assert type(main_dict)==dict
    assert type(secondary_dict)==dict

    # Check if there are any tasks at all
    if not main_dict and not secondary_dict:
        print("\nNo tasks to show reminders for.")
        return
    
    # Get today's date
    today = datetime.date.today()
    
    # Gather all tasks from both dictionaries
    all_tasks = []
    
    # Add high priority tasks first
    for task_name, task_info in main_dict.items():
        all_tasks.append((task_name, task_info, "HIGH PRIORITY"))
    
    # Add normal priority tasks
    for task_name, task_info in secondary_dict.items():
        all_tasks.append((task_name, task_info, "NORMAL"))
    
    print("\n" + "="*50)
    print("TASK REMINDERS")
    print("="*50)
    
    # Process each task
    for task_name, task_info, priority in all_tasks:
        # Calculate days until deadline
        due_date = task_info["due"]
        days_left = calc(today, due_date)
        
        print(f"\nTask: {task_name} ({priority})")
        print(f"Due Date: {due_date.strftime('%Y-%m-%d')}")
        print(f"Days until due: {days_left}")
        
        # Generate reminder schedule based on days left
        if days_left < 0:
            # Task is overdue
            print("Status: OVERDUE!")
            print("Reminder: Complete this task immediately!")
        
        elif days_left == 0:
            # Task is due today
            print("Status: DUE TODAY!")
            print("Reminder: Complete this task today!")
        
        elif 0 < days_left < 7:
            # Task is due within a week - daily reminders
            print("Reminder Schedule (Daily):")
            reminder_dates = []
            for i in range(days_left + 1):
                reminder_date = today + datetime.timedelta(days=i)
#atrftime is short for string format time, i.e. it put a time/date object into a dstring fomat so it can be displayed
                reminder_dates.append(reminder_date.strftime('%Y-%m-%d'))            
                print("  " + ", ".join(reminder_dates))
        
        else:
            # Task is 7+ days away - weekly reminders
            print("Reminder Schedule (Weekly):")
            reminder_dates = []
            current_reminder = today
            
            # Generate reminders every 7 days until we're within a week
            while calc(current_reminder, due_date) >= 7:
                reminder_dates.append(current_reminder.strftime('%Y-%m-%d'))
                #.timedelta is to display the difference between two dates or a time span
                current_reminder = current_reminder + datetime.timedelta(days=7)
            
            # Add daily reminders for the last week
            while current_reminder <= due_date:
                reminder_dates.append(current_reminder.strftime('%Y-%m-%d'))
                current_reminder = current_reminder + datetime.timedelta(days=1)
            
            print("  " + ", ".join(reminder_dates))
        
        print("-" * 40)
    
    print()
    pass

def Prioritization(main_dict, secondary_dict, task_name):#major
    """Move task from sec to main(prioritizing this task)"""
    If task_name in secondary_dict:
        task = secondary_dict.pop(task_name) # Remove from normal list
        task["priority"] = "high" # Update field
        main_dict[task_name] = task # Insert into high priority
        print(f"✓ Task '{task_name}' has been moved to HIGH PRIORITY.")
else:
        print(f"✗ Task '{task_name}' not found in normal tasks.")
    pass

def TimeTracker(): #debating to add
    """When task reaches to 2 weeks before due date set reminders to everyday, 
    when task reaches day after due date, call deletion"""#could be extra overdraft(missing assignment) function made
    pass


#Helper Functions


def calc(startDate, endDate):
    """
    Calculates # of days between 2 dates 

    >>> calc(datetime.date(2025, 1, 1), datetime.date(2025, 1, 8))
    7
    >>> calc(datetime.date(2025, 1, 1), datetime.date(2025, 1, 1))
    0
    """
    # ASSERTIONS: Check parameter types
    assert isinstance(startDate, datetime.date), "startDate must be a datetime.date object"
    assert isinstance(endDate, datetime.date), "endDate must be a datetime.date object"
    
    delta = endDate - startDate
    
    # ASSERTION: Result should be an integer
    assert isinstance(delta.days, int), "Result must be an integer"
    
    return delta.days


def DeadLines(deadline_str):
    """
    Convert date string to datetime.date object
    
    """
    # ASSERTION: Input must be a string
    assert isinstance(deadline_str, str), "deadline_str must be a string"
    
    try:
        # Split the string by '-'
        year, month, day = deadline_str.split('-')
        
        # Convert to integers
        year = int(year)
        month = int(month)
        day = int(day)
        
        # Create and return date object
        result = datetime.date(year, month, day)
        
        # ASSERTION: Result should be a date object
        assert isinstance(result, datetime.date), "Result must be a datetime.date object"
        
        return result
    
    except ValueError:
        # This catches invalid dates like '2025-13-40' or wrong format
        raise ValueError("Invalid date format. Please use YYYY-MM-DD (e.g., 2025-11-20)")

doctest.testmod()
