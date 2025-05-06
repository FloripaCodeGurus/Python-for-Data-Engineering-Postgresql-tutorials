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