# create
from insert_people_data import insert_people_data
from insert_courses_data import insert_courses_data
from utils.gen_people_fake_data import create_fake_people, create_fake_courses, evaluation_test
from database_conn import connect_to_university_db
from list_objects import list_tables
from reading_data import reading_tables_data
from insert_evaluation_results import test_results
from update_record import updateRecord
from delete_record import deleteRecord
from selct_on import getRecord
import logging

# CREATE
economy_test = evaluation_test("economia", 127)  # cria 127 avaliaçoes de economia
insert_data_economy_test = test_results(economy_test) #insere os dados do teste de economia

# RETRIEVE
## 1. Liste os objetos
university_tables = list_tables('university')
print(university_tables)

## 2.Leia dados de uma tabela
econmy_test_results = reading_tables_data('university', 'evaluation_test')
print(econmy_test_results)

# UPDATE
update_economy_results = updateRecord('evaluation_test', 'grade', 10, "student_id = 100")

# DELETE
delete_econmy_record = deleteRecord('evaluation_test', "student_id = 100")

# Check
check_deleted_record = getRecord('evaluation_test', "student_id = 100")
print(check_deleted_record)