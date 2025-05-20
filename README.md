# Python for Data Engineering - PostgreSQL Tutorial One

This project demonstrates how to use Python for basic data engineering tasks with PostgreSQL, including database connection, table creation, data insertion, and querying, using the `psycopg2` and `faker` libraries.

## Project Structure

```
tutorial_1/
│
├── postgres_connector.py
├── database_conn.py
├── create_database.py
├── create_tables.py
├── alter_table.py
├── insert_people_data.py
├── insert_courses_data.py
├── insert_evaluation_results.py
├── list_objects.py
├── reading_data.py
├── reading_data_as_dataframe.py
└── utils/
    └── gen_people_fake_data.py
```

---

## About `tutorial_1` 

The `tutorial_1` folder contains all the scripts and utilities needed to demonstrate a typical data engineering workflow with PostgreSQL and Python. Below is a description of each main file:

- **`postgres_connector.py`**  
  Handles the low-level connection to PostgreSQL using `psycopg2`. Allows flexible database selection via parameters.

- **`database_conn.py`**  
  Provides a higher-level function to connect specifically to the `university` database, often returning a SQLAlchemy engine for use with pandas.

- **`create_database.py`**  
  Script to create the `university` database if it does not exist.

- **`create_tables.py`**  
  Creates the main tables (`people`, `courses`, `grades`, `classes`) in the `university` database. Uses `CREATE TABLE IF NOT EXISTS` to avoid errors.

- **`alter_table.py`**  
  Alters existing tables, such as increasing the size of the `phone_number` column in the `people` table.

- **`insert_people_data.py`**  
  Generates and inserts fake people data into the `people` table using the `Faker` library.

- **`insert_courses_data.py`**  
  Generates and inserts fake course data into the `courses` table.

- **`insert_evaluation_results.py`**  
  Inserts fake evaluation/test results, linking students, teachers, and courses.

- **`list_objects.py`**  
  Lists all databases and tables, useful for verifying your schema and data.

- **`reading_data.py`**  
  Reads and prints all rows from a specified table in the database.

- **`reading_data_as_dataframe.py`**  
  Reads a table from the database and loads it into a pandas DataFrame for analysis and exploration.

- **`utils/gen_people_fake_data.py`**  
  Contains utility functions for generating fake data for people, courses, and grades using `Faker`.

---

## Steps Covered

### 1. PostgreSQL Connection

- **File:** `postgres_connector.py`
- Connects to PostgreSQL using `psycopg2`.
- Supports connecting to different databases by passing the `dbname` parameter.

### 2. Creating a Database

- **File:** `create_database.py`
- Uses the connection to create a new database called `university`.

### 3. Creating Tables

- **File:** `create_tables.py`
- Creates tables: `people`, `courses`, `grades`, and `classes` in the `university` database.
- Uses `CREATE TABLE IF NOT EXISTS` to avoid duplicate table errors.

### 4. Altering Tables

- **File:** `alter_table.py`
- Alters the `people` table to increase the `phone_number` column size to `VARCHAR(30)` to avoid data truncation errors.

### 5. Generating Fake Data

- **File:** `utils/gen_people_fake_data.py`
- Uses `Faker` with the `pt_BR` locale to generate realistic Brazilian Portuguese data for people and courses.
- Functions:
  - `create_fake_people(num_people, role)`
  - `create_fake_courses(num_courses)`
  - `create_fake_grades(num_grades, num_students, num_courses)`

### 6. Inserting Data

- **Files:** `insert_people_data.py`, `insert_courses_data.py`
- Inserts generated fake data into the `people` and `courses` tables.
- Handles bulk inserts and logs success.

### 7. Listing Databases and Tables

- **File:** `list_objects.py`
- Functions to list all databases and all tables in a specified database.

### 8. Reading Data

- **File:** `reading_data.py`
- Reads and prints all rows from a specified table in a specified database.

### 9. Reading Data as DataFrame

- **File:** `reading_data_as_dataframe.py`
- Loads table data directly into a pandas DataFrame for further analysis, statistics, and data exploration.

---

## Common Issues & Fixes

- **UndefinedTable / UndefinedColumn:** Make sure you are connecting to the correct database and using the correct column names.
- **StringDataRightTruncation:** Increase the column size in your table if your data is too long.
- **DuplicateTable:** Use `CREATE TABLE IF NOT EXISTS` to avoid errors when tables already exist.

## Usage

1. **Create the database:**
    ```bash
    python tutorial_1/create_database.py
    ```

2. **Create tables:**
    ```bash
    python tutorial_1/create_tables.py
    ```

3. **Alter tables if needed:**
    ```bash
    python tutorial_1/alter_table.py
    ```

4. **Insert fake data:**
    ```bash
    python tutorial_1/insert_people_data.py
    python tutorial_1/insert_courses_data.py
    ```

5. **List databases and tables:**
    ```bash
    python tutorial_1/list_objects.py
    ```

6. **Read data from tables:**
    ```bash
    python tutorial_1/reading_data.py
    ```

7. **Read data as pandas DataFrame:**
    ```bash
    python tutorial_1/reading_data_as_dataframe.py
    ```

## Requirements

- Python 3.x
- `psycopg2`
- `Faker`
- `pandas`
- `SQLAlchemy`

Install requirements:
```bash
pip install -r requirements.txt
```

---

**Note:**  
- Update your database credentials in `postgres_connector.py` as needed.
- Make sure PostgreSQL is running and accessible on your machine.