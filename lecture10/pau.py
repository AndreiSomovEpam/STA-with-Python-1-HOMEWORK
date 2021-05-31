from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

engine = create_engine("sqlite:///main.db", echo=True)
base = declarative_base()


class Student(base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    def __repl__(self):
        return "<User(name='{}', fullname='{}')>".format(self.name, self.fullname)


# base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()
# print(session)
student1 = Student(name="st1", fullname="st2")
# session.add(student1)
# session.commit()
q = session.query(Student).filter_by(name="st1")
st2 = q.first()
print(st2)