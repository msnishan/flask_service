from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_alchemy import Base, Student


def create_db_session():
    engine = create_engine('sqlite:///students_al.db', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


def load_data(session):
    student1 = Student(name='std1', age=12, grade='A')
    student2 = Student(name='std2', age=20, grade='B')
    student3 = Student(name='std3', age=33, grade='O')
    session.add_all([student1, student2, student3])
    session.commit()


def get_students_by_ids(session, ids):
    students = session.query(Student).filter(Student.id.in_(ids)).all()
    students_arr = []
    for std in students:
        students_arr.append({
            'id': std.id,
            'name': std.name,
            'age': std.age,
            'grade:': std.grade
        })
    return students_arr
