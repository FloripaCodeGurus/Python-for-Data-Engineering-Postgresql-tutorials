from faker import Faker
import random

cursos = ['matecmatica', 
            'lingua portuguesa', 
            'historia do brasil 1', 
            'historia do brasil 2', 
            'economia', 
            'geografia',
            'geo-politica-1',
            'geo-politica2']

def create_fake_courses(num_disciplines):
    fake = Faker('pt_BR') # Brazilian Portuguese locale
    disciplines = []

    for _ in range(num_disciplines):
        discipline = {
            'course_name':random.choice(cursos),  # Nao usei Faker aqui... 
            'teacher_id':random.randint(1, 512),
            "description": fake.sentence(),
            'start_date':fake.date(), 
            'end_date':fake.date()
        }
        disciplines.append(discipline)
    return disciplines


# Generate fake data for people
def create_fake_people(num_people, role=None, start_id=11):
    fake = Faker('pt_BR') # Brazilian Portuguese locale
    people = []
    for i in range(num_people):
        person = {
            "id": start_id + i,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "role": role,
            "age": random.randint(18, 65),
            "phone_number": fake.phone_number(),
            "email": fake.email()
        }
        people.append(person)
    return people


# def create_fake_grades(num_grades, num_students, num_disciplines):
#     """Rada em conjunt coma a função evaluation_test"""
#     grades = []
#     for _ in range(num_grades):
#         grade = {
#             "student_id": random.randint(1, num_students),
#             "discipline_id": random.randint(1, num_disciplines),
#             "grade": round(random.uniform(0, 10), 2)
#         }
#         grades.append(grade)
#     return grades


def evaluation_test(disciplina, num_tests):
    fake = Faker('pt_BR')
    tests = []
    for _ in range(num_tests):
        teacher = create_fake_people(1, role="teacher")[0]
        test = {
            "discipline": disciplina,
            "teacher_id": teacher["id"],
            "teacher_first_name": teacher["first_name"],
            "teacher_last_name": teacher["last_name"],
            "student": create_fake_people(1, role="student"),
            "grade": random.randint(0, 10), # mais simples
            "test_date": fake.date(),
        }
        tests.append(test)
    return tests

if __name__ == "__main__":
    # Example usage
    # Generate fake data for 10 people
    students = create_fake_people(5000, role="student")
    # print(students)
    teachers = create_fake_people(50, role="teacher")
    # print(techers)
    principals = create_fake_people(1, role="principal")
    print(principals)
    supervisors = create_fake_people(40, role="supervisor")
    print(supervisors)