import json

class ToDoList:
    def __init__(self):
        self.tasks = []

    def load_tasks(self, filename='tasks.json'):
        try:
            with open(filename, 'r') as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self, filename='tasks.json'):
        with open(filename, 'w') as f:
            json.dump(self.tasks, f)

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added: {task}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = new_task
            self.save_tasks()
            print("Task updated.")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            self.save_tasks()
            print(f"Task removed: {removed_task}")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()
    todo_list.load_tasks()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            index = int(input("Enter the task number to update: ")) - 1
            new_task = input("Enter the new task: ")
            todo_list.update_task(index, new_task)
        elif choice == '4':
            index = int(input("Enter the task number to delete: ")) - 1
            todo_list.delete_task(index)1
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
