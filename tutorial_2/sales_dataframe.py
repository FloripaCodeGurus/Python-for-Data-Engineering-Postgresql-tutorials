import pandas as pd
import numpy as np
from faker import Faker

fake = Faker('pt_BR')

# Generating data for each table
countries = pd.DataFrame({
    'id': [1],
    'name': ['Brazil']
})


states = pd.DataFrame({
    'id': np.arange(1, 3),
    'name': ['São Paulo', 'Rio de Janeiro'],
    'uf': ['SP', 'RJ'],
    'country_id': [1, 1]
})

cities = pd.DataFrame({
    'id': np.arange(1, 5),
    'city_name': ['São Paulo', 'Campinas', 'Rio de Janeiro', 'Niterói'],
    'state_id': [1, 1, 2, 2]
})
addresses = pd.DataFrame({
    'id': np.arange(1, 51),
    'street': [fake.street_name() for _ in range(50)],
    'number': [str(fake.building_number()) for _ in range(50)],
    'city_id': np.random.randint(1, 5, 50)
})

people = pd.DataFrame({
    'id': np.arange(1, 51),
    'first_name': [fake.first_name() for _ in range(50)],
    'last_name': [fake.last_name() for _ in range(50)],
    'age': np.random.randint(18, 70, 50),
    'address_id': np.random.randint(1, 51, 50)
})

people_contacts = pd.DataFrame({
    'id': np.arange(1, 51),
    'email': [fake.email() for _ in range(50)],
    'phone_number': [fake.phone_number() for _ in range(50)],
    'type': np.random.choice(['mobile', 'home', 'work'], 50),
    'people_id': np.arange(1, 51)
})

stores = pd.DataFrame({
    'id': np.arange(1, 11),
    'name': [fake.company() for _ in range(10)],
    'address_id': np.random.randint(1, 51, 10)
})

products = pd.DataFrame({
    'id': np.arange(1, 21),
    'name': [fake.word().title() for _ in range(20)],
    'price': np.round(np.random.uniform(5, 500, 20), 2),
    'stock': np.random.randint(10, 200, 20),
    'store_id': np.random.randint(1, 11, 20)
})

orders = pd.DataFrame({
    'id': np.arange(1, 31),
    'people_id': np.random.randint(1, 51, 30),
    'store_id': np.random.randint(1, 11, 30),
    'total_amount': np.round(np.random.uniform(50, 2000, 30), 2)
})

order_items = pd.DataFrame({
    'id': np.arange(1, 61),
    'order_id': np.random.randint(1, 31, 60),
    'product_id': np.random.randint(1, 21, 60),
    'quantity': np.random.randint(1, 5, 60)
})

order_items['unit_price'] = order_items['product_id'].apply(lambda x: products.loc[x-1, 'price'])

print(people.columns)
print(orders.columns)
print()
sale_records_df = (
    people.join(orders.set_index('people_id'), on='id', rsuffix='_order')
          .join(stores.set_index('id'), on='store_id', rsuffix='_store')
          .join(order_items.set_index('order_id'), on='id_order', rsuffix='_item')
          .join(products.set_index('id'), on='product_id', rsuffix='_product')
          .join(addresses.set_index('id'), on='address_id', rsuffix='_address')
          .join(cities.set_index('id'), on='city_id', rsuffix='_city')
          .join(states.set_index('id'), on='state_id', rsuffix='_state')
          .join(countries.set_index('id'), on='country_id', rsuffix='_country')
          .join(people_contacts.set_index('people_id'), on='id', rsuffix='_contact')
)

print(sale_records_df.head())