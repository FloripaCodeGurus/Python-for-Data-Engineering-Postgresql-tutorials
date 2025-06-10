from faker import Faker
import random


# Generate fake data for people
def create_fake_people(num_people, role=None, start_id=1):
    fake = Faker('pt_BR') # Brazilian Portuguese locale
    people = []
    for i in range(num_people):
        person = {
            "id": start_id + i,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "age": role,
            "city_id": random.randint(1, 512),  
        }
        people.append(person)
    return people

def create_countries(num_cities):
    fake = Faker('pt_BR') # Brazilian Portuguese locale
    countries = []
    for i in range(num_cities):
        countrie = {
            "id": i + 1,
            "name": fake.country(),
        }
        countries.append(countrie)
    return countries

def create_states(num_cities):
    fake = Faker('pt_BR') # Brazilian Portuguese locale
    states = []
    for i in range(num_cities):
        state = {
            "id": i + 1,
            "name": fake.city(),
            "uf": fake.state_abbr(),
            "country_id": random.randint(1, 424),
        }
        states.append(state)
    return states

def create_cities(num_cities):
    fake = Faker('pt_BR') # Brazilian Portuguese locale
    cities = []
    for i in range(num_cities):
        city = {
            "id": i + 1,
            "city_name": fake.city(),
            "state_id": random.randint(1, 51212),
        }
        cities.append(city)
    return cities

def create_addresses(num_cities):
    fake = Faker('pt_BR') # Brazilian Portuguese locale
    cities = []
    for i in range(num_cities):
        city = {
            "id": i + 1,
            "street": fake.street_address(),
            "number": random.randint(112, 501200),
            "city_id": random.randint(1, 51212),
        }
        cities.append(city)
    return cities

if __name__ == "__main__":
    # Example usage
    # Generate fake data for 10 people
    fake_people = create_fake_people(10)
    for person in fake_people:
        print(person)
    print("--------------------------------------------------")
    create_cities = create_cities(10)
    for city in create_cities:
        print(city)