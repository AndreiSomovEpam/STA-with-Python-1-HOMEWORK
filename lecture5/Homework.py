from datetime import datetime


class Homework:
    def __init__(self, text, deadline):
        self.text = text
        self.deadline = deadline
        self.created = datetime.today()

    def is_active(self):
        return datetime.now() - self.created < self.deadline
