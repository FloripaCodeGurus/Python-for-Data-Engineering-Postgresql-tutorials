from utils.gen_people_fake_data import create_fake_people
from database_conn import connect_to_university_db

students = create_fake_people(5000, role="student")
techers = create_fake_people(50, role="teacher")
principals = create_fake_people(1, role="principal")
supervisors = create_fake_people(40, role="supervisor")


for super in  supervisors:
    print(super)