from faker import Faker
import random


# Generate fake data for people
def create_fake_people(num_people, role=None):
    fake = Faker('pt_BR') # Brazilian Portuguese locale
    people = []
    for _ in range(num_people):
        person = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "role": role,
            "age": random.randint(18, 65),
            "phone_number": fake.phone_number(),
            "email": fake.email()
        }
        people.append(person)
    return people

def create_fake_courses(num_disciplines):
    fake = Faker('pt_BR') # Brazilian Portuguese locale
    disciplines = []
    cursos = ['matecmatica', 
              'lingua portuguesa', 
              'historia do brasil 1', 
              'historia do brasil 2', 
              'economia', 
              'geografia',
              'geo-politica-1',
              'geo-politica2']
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

def create_fake_grades(num_grades, num_students, num_disciplines):
    grades = []
    for _ in range(num_grades):
        grade = {
            "student_id": random.randint(1, num_students),
            "discipline_id": random.randint(1, num_disciplines),
            "grade": round(random.uniform(0, 10), 2)
        }
        grades.append(grade)
    return grades


# def create_tests_result():
#     fake = Faker('pt_BR') # Brazilian Portuguese locale
#     tests = []
#     for _ in range(100):
#         test = {
#             "student_id": random.randint(1, 5000),
#             "discipline_id": random.randint(1, 100),
#             "test_date": fake.date(),
#             "grade": round(random.uniform(0, 10), 2)
#         }
#         tests.append(test)
#     return tests

if __name__ == "__main__":
    # Example usage
    # Generate fake data for 10 people
    students = create_fake_people(5000, role="student")
    # print(students)
    techers = create_fake_people(50, role="teacher")
    # print(techers)
    principals = create_fake_people(1, role="principal")
    print(principals)
    supervisors = create_fake_people(40, role="supervisor")
    print(supervisors)