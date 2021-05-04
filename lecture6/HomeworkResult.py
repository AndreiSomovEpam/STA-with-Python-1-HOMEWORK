from lecture6.Homework import Homework


class HomeworkResult:
    def __init__(self, homework, solution, author):
        if type(homework) is Homework:
            self.homework = homework
        else:
            raise TypeError("You gave a not Homework object")
        self.solution = solution
        self.author = author
        self.created = homework.created
