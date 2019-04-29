class Task:
    def __init__(self, id=0, title='', description=''):
        self.id = id
        self.title = title
        self.description = description

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
        }