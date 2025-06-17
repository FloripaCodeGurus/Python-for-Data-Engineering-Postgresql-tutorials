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
            "age": fake.random_int(min=18, max=80),
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

def create_states(num_states):
    fake = Faker('pt_BR') # Brazilian Portuguese locale
    states = []
    for i in range(num_states):
        state = {
            "id": i + 1,
            "name": fake.city(),
            "uf": fake.state_abbr(),
            "country_id": random.randint(1,7),
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
            "state_id": random.randint(1, 28),
        }
        cities.append(city)
    return cities

def create_addresses(num_addresses):
    fake = Faker('pt_BR') # Brazilian Portuguese locale
    cities = []
    for i in range(num_addresses):
        city = {
            "id": i + 1,
            "street": fake.street_address(),
            "number": random.randint(112, 501200),
            "city_id": random.randint(1, 112),  # Assuming we have 112 cities on cities.csv
        }
        cities.append(city)
    return cities

