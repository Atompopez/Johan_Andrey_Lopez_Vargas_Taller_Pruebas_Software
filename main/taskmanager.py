class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = {"title": title, "completed": False}
        self.tasks.append(task)
        return task

    def edit_task(self, index, new_title):
        self.tasks[index]["title"] = new_title
        return self.tasks[index]

    def delete_task(self, index):
        self.tasks.pop(index)
