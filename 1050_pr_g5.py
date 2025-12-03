import doctest
import datetime
import json  
def main():
    # Create two empty dictionaries for storage
    main_dict, secondary_dict = load_tasks()
    print(f"Loaded {len(main_dict)} high priority and {len(secondary_dict)} normal tasks.")
    
    # Main program loop
    while True:
        # Display menu options
        Display()
        
        # Get user choice
        choice = input("Enter your choice (1-7): ")
        
        # Option 1: Add priority task
        if choice == '1':
            Retrieval(main_dict, is_high=True)
    
        
        # Option 2: Add normal task
        elif choice == '2':
            Retrieval(secondary_dict, is_high=False)
        
        # Option 3: View all tasks
        elif choice == '3':
            ShowTask(main_dict, secondary_dict)
        
        # Option 4: Delete a task
        elif choice == '4':
            Deletion(main_dict, secondary_dict)
        
        # Option 5: Show reminders
        elif choice == '5':
            Reminders(main_dict, secondary_dict)
        
        # Option 6: Quit program
        elif choice == '6':
            save_tasks(main_dict, secondary_dict)
            print("Tasks saved!")
            print("Goodbye!")
    
            break
        
        elif choice == '7':
            task_name = input("Enter the task name to prioritize: ").strip()
            Prioritization(main_dict, secondary_dict, task_name)
        
        else:
            print("Invalid choice. Please try again.")


#Major Functions




def Display():
   
    print("TASK TRACKER MENU")
    print("1. Add Priority Task")
    print("2. Add Normal Task")
    print("3. View All Tasks")
    print("4. Delete a Task")
    print("5. Show Reminders")
    print("6. Quit")
    print("7. Prioritize a Task")
     

def Retrieval(task_dict, is_high=False):
    """
    Get task details from user and add to dictionary
    
    Args:
        task_dict: Dictionary to store the task (either main_dict or secondary_dict)
        is_high: Boolean indicating if this is a high priority task

    """
    # ASSERTION: Check that function received correct parameter types
    assert isinstance(task_dict, dict), "needs to be dicty"
    assert isinstance(is_high, bool), "needs to be T/F"
    
    print("\n--- Add New Task ---")
    
    # Step 1: Get task name (must be non-empty)
    while True:
        task_name = input("Enter task name: ").strip()
        
        if task_name == '':
            print("Error: Task name can't be empty. Please try again.")
            continue
        
        if task_name in task_dict:
            print(f"Error: Task '{task_name}' already exists. Please use a different name.")
            continue
        
        break
    
    # Step 2: Get deadline with error handling
    while True:
        date_str = input("Enter deadline (YYYY-MM-DD, e.g., 2025-11-20): ").strip()
        
        try:
           
            due_date = DeadLines(date_str)
            
            assert isinstance(due_date, datetime.date), "DeadLines must return a date object"
            
            if due_date < datetime.date.today():
                confirm = input("Warning: This date is in the past. Continue? (y/n): ").lower()
                if confirm != 'y':
                    continue
            
         
            break
            
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")
    
    # Step 3: Build task dictionary
    info = {
        "due": due_date,
        "priority": "high" if is_high else "normal"
    }
    

    assert "due" in info, "Task must have a due date"
    assert "priority" in info, "Task must have a priority level"
    
    # Step 5: Add to dictionary
    task_dict[task_name] = info
    
 
    assert task_name in task_dict, "Task should be in dictionary after adding"
    
    # Step 6: Print confirmation
    label = "HIGH PRIORITY" if is_high else "NORMAL"
    print(f"\n✓ Task '{task_name}' added successfully as {label}!")
    print(f"  Due: {due_date.strftime('%Y-%m-%d')}")
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

     
    
def Deletion(main_dict, secondary_dict):
    """Delete task by name from storage"""
    print("Delete Task")
    task_name = input("Enter the task name to delete: ").strip()

    # Delete from priority dict
    if task_name in main_dict:
        del main_dict[task_name]
        print(f"✓ Task '{task_name}' deleted from HIGH PRIORITY list.")
        return
    # Delete from normal dict
    if task_name in secondary_dict:
        del secondary_dict[task_name]
        print(f"✓ Task '{task_name}' deleted from NORMAL list.")
        return
    # Not Found
    print(f"✗ Task '{task_name}' not found")
     


def Reminders(main_dict:dict, secondary_dict:dict):
    """
    Display reminders for all tasks
    
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
    
  
    for task_name, info in main_dict.items():
        all_tasks.append((task_name, info, "HIGH PRIORITY"))
    
 
    for task_name, info in secondary_dict.items():
        all_tasks.append((task_name, info, "NORMAL"))
    
    print("\n" + "="*50)
    print("TASK REMINDERS")
    print("="*50)
    
    
    for task_name, info, priority in all_tasks:
        # Calculate days until deadline
        due_date = info["due"]
        days_left = calc(today, due_date)
        
        print(f"\nTask: {task_name} ({priority})")
        print(f"Due Date: {due_date.strftime('%Y-%m-%d')}")
        print(f"Days until due: {days_left}")
        
        # Generate reminder schedule based on days left
        if days_left < 0:
            
            print("Status: OVERDUE!")
            print("Reminder: Complete this task immediately!")
        
        elif days_left == 0:
            
            print("Status: DUE TODAY!")
            print("Reminder: Complete this task today!")
        
        elif 0 < days_left < 7:
            # Task is due within a week - daily reminders
            print("Reminder Schedule (Daily):")
            reminders= []
            for i in range(days_left + 1):
                reminder_date = today + datetime.timedelta(days=i)
                reminders.append(reminder_date.strftime('%Y-%m-%d'))       #strtime->string format time ->displays special type as string     
            print("  " + ", ".join(reminders))
        
        else:
            # Task is 7+ days away - weekly reminders
            print("Reminder Schedule (Weekly):")
            reminders= []
            current_reminder = today
            
            # Generate reminders every 7 days until we're within a week
            while calc(current_reminder, due_date) >= 7:
                reminders.append(current_reminder.strftime('%Y-%m-%d'))
                current_reminder = current_reminder + datetime.timedelta(days=7) #display difference between date 1 & 2
            
            # Add daily reminders for the last week
            while current_reminder <= due_date:
                reminders.append(current_reminder.strftime('%Y-%m-%d'))
                current_reminder = current_reminder + datetime.timedelta(days=1)
            
            print("  " + ", ".join(reminders))
        
        print("-" * 40)
    
    print()
     

def Prioritization(main_dict, secondary_dict, task_name):#major
    """Move task from sec to main(prioritizing this task)"""
    if task_name in secondary_dict:
        task = secondary_dict.pop(task_name) # Remove from normal list
        task["priority"] = "high" # Update field
        main_dict[task_name] = task # Insert into high priority
        print(f"✓ Task '{task_name}' has been moved to HIGH PRIORITY.")
    else:
        print(f"✗ Task '{task_name}' not found in normal tasks.")
     




#Helper Functions


def calc(start, end):
    """
    Calculates # of days between 2 dates 

    >>> calc(datetime.date(2025, 1, 1), datetime.date(2025, 1, 8))
    7
    >>> calc(datetime.date(2025, 1, 1), datetime.date(2025, 1, 1))
    0
    """
    # ASSERTIONS: Check parameter types
    assert isinstance(start, datetime.date), "start must be a datetime.date object"
    assert isinstance(end, datetime.date), "end must be a datetime.date object"
    
    delta = end - start
    
    # ASSERTION: Result should be an integer
    assert isinstance(delta.days, int), "Result must be an integer"
    
    return delta.days


def DeadLines(date_str):
    """
    Convert date string to datetime.date object
    
    """
    # ASSERTION: Input must be a string
    assert isinstance(date_str, str), "date_str must be a string"
    
    try:
        # Split the string by '-'
        year, month, day = date_str.split('-')
        
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
    
def save_tasks(hi_pri, norm, file="tasks.json"):
    """Save tasks to a JSON file"""
    data = {
        "high_priority": {},
        "normal": {}
    }
    
    for name, info in hi_pri.items():
        data["high_priority"][name] = {
            "due": info["due"].strftime('%Y-%m-%d'),
            "priority": info["priority"]
        }
    
    for name, info in norm.items():
        data["normal"][name] = {
            "due": info["due"].strftime('%Y-%m-%d'),
            "priority": info["priority"]
        }
    
    with open(file, 'w') as f:
        json.dump(data, f, indent=2)


def load_tasks(file="tasks.json"):
    """Load tasks from a JSON file"""
    try:
        with open(file, 'r') as f:
            data = json.load(f)
        
        hi_pri = {}
        norm = {}
        
        for name, info in data.get("high_priority", {}).items():
            hi_pri[name] = {
                "due": DeadLines(info["due"]),
                "priority": info["priority"]
            }
        
        for name, info in data.get("normal", {}).items():
            norm[name] = {
                "due": DeadLines(info["due"]),
                "priority": info["priority"]
            }
        
        return hi_pri, norm
    
    except FileNotFoundError:
        return {}, {}

doctest.testmod()
if __name__ == "__main__": #this line specifically was a Sonnet 4.5 suggestion to ensure the program runs
    main() 
