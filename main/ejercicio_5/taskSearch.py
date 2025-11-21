class TaskSearchService:
    def __init__(self, tasks):
        self.tasks = tasks

    def search(self, query):
        return [t for t in self.tasks if query.lower() in t["title"].lower()]
