from datetime import timedelta

from lecture5.Student import Student
from lecture5.Teacher import Teacher

homework = Teacher.create_homework("text", timedelta(4))
student = Student("first", "last")
student.do_homework(homework)
