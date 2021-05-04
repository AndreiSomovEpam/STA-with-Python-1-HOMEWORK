from lecture6.DeadlineError import DeadlineError
from lecture6.HomeworkResult import HomeworkResult
from lecture6.Person import Person


class Student(Person):
    def do_homework(self, homework, solution):
        if homework.is_active():
            return HomeworkResult(homework, solution, self)
        else:
            raise DeadlineError
