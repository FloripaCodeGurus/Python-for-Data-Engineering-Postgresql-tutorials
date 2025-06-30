--Countries
INSERT INTO countries (name) VALUES ('Brazil');

--States
INSERT INTO states (name, uf, country_id) VALUES ('São Paulo', 'SP', 1);

-- Cities
INSERT INTO cities (city_name, state_id) VALUES ('São Paulo', 1);

-- Addresses
INSERT INTO addresses (street, number, city_id) VALUES ('Av. Paulista', '1000', 1);
INSERT INTO addresses (street, number, city_id) VALUES ('Rua Augusta', '200', 1);

-- People
INSERT INTO people (first_name, last_name, age, address_id) 
VALUES ('João', 'Silva', 30, 1);

-- Contacts
INSERT INTO people_contacts (mobile_phone_number,professional_phone_number,email, type, person_id) 
VALUES ('(11) 99999-9999', '(11) 99999-9999', 'joao.silva@example.com', 'mobile', 1);

-- Stores
INSERT INTO stores (name, address_id) VALUES ('Supermercado Central', 2);

-- Products
INSERT INTO products (name, price, stock, store_id) 
VALUES ('Arroz', 20.00, 100, 1),
       ('Feijão', 8.50, 200, 1);

-- Orders
INSERT INTO orders (person_id, store_id, total_amount) VALUES (1, 1, 57.00);

-- Orders
INSERT INTO orders (person_id, store_id, total_amount) VALUES
(1, 1, 150.00),
(2, 2, 250.50),
(3, 1, 320.75),
(4, 3, 180.00),
(5, 2, 499.99),
(6, 1, 75.25),
(7, 3, 640.10),
(8, 2, 89.90),
(9, 3, 100.00),
(10, 1, 215.00);

-- Order Items
INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
(1, 1, 3, 50.00),
(2, 2, 5, 50.10),
(3, 3, 2, 160.37),
(4, 4, 4, 45.00),
(5, 5, 1, 499.99),
(6, 6, 5, 15.05),
(7, 7, 2, 320.05),
(8, 8, 1, 89.90),
(9, 9, 2, 50.00),
(10, 10, 1, 215.00);

-- Order Items
INSERT INTO order_items (order_id, product_id, quantity, unit_price) 
VALUES (1, 1, 2, 20.00),  -- Arroz
       (1, 2, 2, 8.50);   -- Feijão