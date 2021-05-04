class DeadlineError(Exception):
    def __init__(self):
        self.message = "You are late"
