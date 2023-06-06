"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2


with psycopg2.connect(host="localhost", database="north", user="postgres", password="P@ssw0rd") as conn:
    with conn.cursor() as cur:
        with open('north_data/customers_data.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for colon in reader:
                cur.execute("INSERT INTO customers VALUES (%s, %s, %s)",
                            (colon['customer_id'], colon['company_name'], colon['contact_name']))
        with open('north_data/employees_data.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for colon in reader:
                cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
                            (colon['employee_id'], colon['first_name'], colon['last_name'],
                             colon['title'], colon['birth_date'], colon['notes']))
        with open('north_data/orders_data.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for colon in reader:
                cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                            (colon['order_id'], colon['customer_id'], colon['employee_id'],
                             colon['order_date'], colon['ship_city']))

conn.close()
