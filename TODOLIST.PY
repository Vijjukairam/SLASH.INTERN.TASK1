# Define a class to represent a task
class Task:
  def __init__(self, task_name):
    self.task_name = task_name
    self.completed = False

  def mark_completed(self):
    self.completed = True

# Define an empty list to store tasks
tasks = []

# Function to display the to-do list
def display_tasks():
  if not tasks:
    print("Your to-do list is empty.")
  else:
    print("To-Do List:")
    for task in tasks:
      status = "Done" if task.completed else "Not Done"
      print(f"{task.task_name} ({status})")

# Function to add a task to the to-do list
def add_task(task_name):
  new_task = Task(task_name)
  tasks.append(new_task)
  print(f"Task '{task_name}' added to your to-do list.")

# Function to mark a task as completed
def mark_completed(task_name):
  found = False
  for task in tasks:
    if task.task_name == task_name:
      task.mark_completed()
      found = True
      print(f"Task '{task_name}' marked as completed.")
      break
  if not found:
    print(f"Task '{task_name}' not found.")

# Function to remove a task from the to-do list
def remove_task(task_name):
  found = False
  for i, task in enumerate(tasks):
    if task.task_name == task_name:
      tasks.pop(i)
      found = True
      print(f"Task '{task_name}' removed from your to-do list.")
      break
  if not found:
    print(f"Task '{task_name}' not found.")

# Main program loop
while True:
  print("\nOptions:")
  print("1. Display to-do list")
  print("2. Add a task")
  print("3. Mark a task as completed")
  print("4. Remove a task")
  print("5. Quit")
  choice = input("Enter your choice: ")

  if choice == '1':
    display_tasks()
  elif choice == '2':
    task_name = input("Enter the task: ")
    add_task(task_name)
  elif choice == '3':
    task_name = input("Enter the task name to mark as completed: ")
    mark_completed(task_name)
  elif choice == '4':
    task_name = input("Enter the task name to remove: ")
    remove_task(task_name)
  elif choice == '5':
    break
  else:
    print("Invalid choice. Please enter a valid option.")
