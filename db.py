from models import Student

student_db = {
    1: Student(1, 'A', 10, 'A'),
    2: Student(1, 'B', 66, 'C'),
    3: Student(1, 'C', 22, 'O'),
    4: Student(1, 'D', 33, 'B'),
    5: Student(1, 'E', 14, 'A')
}


def first_student_by_ids(ids):
    result = {k: v for (k, v) in student_db.items() if k in ids}
    return result
