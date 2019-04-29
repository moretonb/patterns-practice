from app.src.data.tasks.commands.create_task import create_task

class TaskBuilder:
    def __init__(self):
        self.title = 'something'
        self.description = 'something'

    def create(self):
        return self

    def with_title(self, title):
        self.title = title
        return self

    def with_description(self, description):
        self.description = description
        return self

    def build(self):
        return create_task(self.title, self.description)
