from faker import Faker
import random

import faker_commerce

fake = Faker()
fake.add_provider(faker_commerce.Provider)


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

def create_stores(num_stores):
    fake = Faker('pt_BR') # Brazilian Portuguese locale
    stores = []
    for i in range(num_stores):
        store = {
            "id": i + 1,
            "name": fake.Provider.ecommerce_name(), # company name as store name
            "address_id": random.randint(1, num_stores),  # Assuming we have 112 addresses on addresses.csv
        }
        stores.append(store)
    return stores


def create_prducts(num_products):
    fake = Faker('pt_BR') # Brazilian Portuguese locale
    products = []
    for i in range(num_products):
        product = {
            "id": i + 1,
            "name": fake.city(),
            "price": fake.Provider.ecommerce_price(),
            "stock":random.random("True", "False"),
            "store_id": random.randint(1, 112),  # Assuming we have 112 addresses on addresses.csv
            }
        products.append(product)
    return products

def create_orders(num_orders):
    fake = Faker('pt_BR') # Brazilian Portuguese locale
    orders = []
    for i in range(num_orders):
        order = {
            "id": random.randint(1, 1000),  # Random ID for the order item
            "order_date": fake.date_time(),
            "person_id": random.randint(1, 1000),
            "store_id":random.randint(1, 112), # Assuming we have 112 stores on stores.csv
            "total_amount": float(random.random(10.99, 20112.99))
        }
        orders.append(order)
    return orders

def create_order_item():
    fake = Faker('pt_BR') # Brazilian Portuguese locale
    item = {
        "id": random.randint(1, 1000),  # Random ID for the order item
        "order_id": fake.city(),
        "product_id": fake.items(),
        "quantity":random.random("True", "False"),
        "unit_price": fake.Provider.ecommerce_price()
        }
    return item