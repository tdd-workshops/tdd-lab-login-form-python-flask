import csv
import os


CSV_OPTIONS = dict(
    delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL
)


def get_db():
    root = os.path.dirname(os.path.realpath(__file__))
    directory = 'db'
    filename = 'user_db.csv'
    return f'{root}/{directory}/{filename}'


def get_all_employees():
    with open(get_db(), mode='r') as employee_file:
        employee_reader = csv.reader(employee_file, **CSV_OPTIONS)
        for username, email, password in employee_reader:
            yield username, email, password


def insert_employee(username, email, password):
    with open(get_db(), mode='a') as employee_file:
        employee_writer = csv.writer(employee_file, **CSV_OPTIONS)
        employee_writer.writerow([username, email, password])