from collections import defaultdict
from multimethod import multimethod

from lecture6.Homework import Homework

from lecture6.Person import Person


class Teacher(Person):
    homework_done = defaultdict(list)

    @staticmethod
    def create_homework(text, deadline):
        return Homework(text, deadline)

    def check_homework(homework_result):
        if len(homework_result.solution) > 5:
            Teacher.homework_done[homework_result.homework].append(homework_result)
            return True
        else:
            return False

    def reset_results(*homework):
        if len(homework) == 0:
            Teacher.homework_done.clear()
        else:
            Teacher.homework_done.pop(homework, None)
