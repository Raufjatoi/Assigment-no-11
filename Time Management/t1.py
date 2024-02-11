# 1. To-Do List: Develop a program that allows the user to add tasks to a to-do list. Use if statements 
# to categorize tasks as urgent, important, or less important based on their due date and priority.

urgent = []
important = []
less_important = []

task = input("Enter the task: ")
due_date = input("Enter the due date (e.g., DD/MM/YYYY): ")
priority = input("Enter the priority (urgent, important, less important): ").lower()


if priority == "urgent":
    urgent.append((task, due_date))
elif priority == "important":
    important.append((task, due_date))
elif priority == "less important":
    less_important.append((task, due_date))
else:
    print("Invalid priority input.")


print("Urgent tasks:", urgent)
print("Important tasks:", important)
print("Less important tasks:", less_important)
