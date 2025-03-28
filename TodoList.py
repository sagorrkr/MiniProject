class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority

    def __str__(self):
        return f"{self.description}: {self.priority}"
    

class TodoList:
    def __init__(self):
        self.tasks = []
        self.completed_task = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task Added: {task.description} ")

    def remove_task(self, description):
        for task in self.tasks:
            if task.description.lower() == description.lower():
                self.tasks.remove(task)
                print(f"Task Removed: {description}")
                return
            else:
                print(f"{description} not found.")

    def display_tasks(self):
        if not self.tasks:
            print("No task to display.")

        else:
            priority_order = {"High" : 1, "Medium" : 2, "Low" : 3}
            sorted_task = sorted(self.tasks, key = lambda x: priority_order[x.priority])
            print("\nToDo List: ")
            for task in sorted_task:
                print(task)
    def mark_completed(self, description):
        for task in self.tasks:
            if task.description.lower() == description.lower():     
                self.tasks.remove(task)
                self.completed_task.append(task)
                print(f"Marked {description} as completed. ")
            else:
                print(f"{description} not found in list. ")

if __name__ == "__main__":
    todo = TodoList()

    todo.add_task(Task("Finishing HW", "High"))
    todo.add_task(Task("Writting Essay", "Medium"))
    todo.add_task(Task("Read AH", "Low"))

    todo.display_tasks()

    todo.mark_completed("Finishing HW")
    todo.display_tasks()