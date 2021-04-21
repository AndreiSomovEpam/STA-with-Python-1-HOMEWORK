from datetime import datetime


class Homework:
    def __init__(self, text, deadline, created=datetime.today()):
        self.text = text
        self.deadline = deadline
        self.created = created

    def is_active(self):
        return (datetime.now() - self.created) < self.deadline