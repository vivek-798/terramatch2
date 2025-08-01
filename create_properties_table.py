# File: create_properties_table.py
# A script to connect to a MySQL server and create a properties table with sample data.
#
# Prerequisites:
# 1. A running MySQL server.
# 2. The 'mysql-connector-python' library installed.
#    You can install it using pip: `pip install mysql-connector-python`

import mysql.connector
from mysql.connector import errorcode
import random

# --- Configuration: Updated to work without a password. ---
DB_HOST = "localhost" 
DB_USER = "root"  
DB_PASSWORD = ""
DB_NAME = "terramatch_properties" 

TABLES = {}
TABLES['properties'] = (
    "CREATE TABLE `properties` ("
    "  `id` INT NOT NULL AUTO_INCREMENT,"
    "  `district` VARCHAR(255) NOT NULL,"
    "  `mandal` VARCHAR(255) NOT NULL,"
    "  `type_of_land` VARCHAR(255) NOT NULL,"
    "  `size_acres` DECIMAL(10, 2) NOT NULL,"
    "  `price` DECIMAL(10, 2) NOT NULL,"
    "  `description` TEXT,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

SAMPLE_DATA = [
    {"district": "Hyderabad", "mandal": "Gachibowli", "type_of_land": "Residential", "size_acres": 2.5, "price_min": 1500000, "price_max": 2500000},
    {"district": "Hyderabad", "mandal": "Manikonda", "type_of_land": "Commercial", "size_acres": 1.0, "price_min": 2000000, "price_max": 3000000},
    {"district": "Karimnagar", "mandal": "Thimmapur", "type_of_land": "Agricultural", "size_acres": 5.0, "price_min": 500000, "price_max": 800000},
    {"district": "Karimnagar", "mandal": "Jagityal", "type_of_land": "Residential", "size_acres": 0.5, "price_min": 200000, "price_max": 400000},
    {"district": "Warangal", "mandal": "Hanamkonda", "type_of_land": "Commercial", "size_acres": 1.2, "price_min": 1000000, "price_max": 1800000},
    {"district": "Warangal", "mandal": "Parkal", "type_of_land": "Agricultural", "size_acres": 7.0, "price_min": 600000, "price_max": 950000},
    {"district": "Medchal", "mandal": "Keesara", "type_of_land": "Residential", "size_acres": 0.8, "price_min": 750000, "price_max": 1200000},
    {"district": "Medchal", "mandal": "Balnagar", "type_of_land": "Industrial", "size_acres": 3.0, "price_min": 2500000, "price_max": 3500000},
    {"district": "Ranga Reddy", "mandal": "Ibrahimpatnam", "type_of_land": "Agricultural", "size_acres": 10.0, "price_min": 900000, "price_max": 1500000},
    {"district": "Ranga Reddy", "mandal": "Rajendranagar", "type_of_land": "Residential", "size_acres": 1.5, "price_min": 1200000, "price_max": 2200000},
]

def create_database_and_table():
    """
    Connects to a MySQL server, creates a database if it doesn't exist,
    and then creates the `properties` table.
    """
    cnx = None
    cursor = None
    try:
        # First, connect to the MySQL server without specifying a database.
        cnx = mysql.connector.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
        cursor = cnx.cursor()

        try:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}` DEFAULT CHARACTER SET 'utf8'")
            print(f"Database '{DB_NAME}' checked/created successfully.")
        except mysql.connector.Error as err:
            print(f"Failed to create database: {err}")
            return

        cursor.close()
        cnx.close()
        
        cnx = mysql.connector.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            database=DB_NAME
        )
        cursor = cnx.cursor()

        for table_name in TABLES:
            table_description = TABLES[table_name]
            try:
                print(f"Creating table {table_name}: ", end='')
                cursor.execute(table_description)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")
                insert_sample_data(cursor, cnx)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(f"An error occurred: {err}")
    finally:
        if cursor:
            cursor.close()
        if cnx and cnx.is_connected():
            cnx.close()
            print("MySQL connection is closed.")


def insert_sample_data(cursor, cnx):
    """
    Inserts sample property data into the database.
    """
    print("Inserting sample data...")
    insert_query = ("INSERT INTO `properties` "
                    "(`district`, `mandal`, `type_of_land`, `size_acres`, `price`, `description`) "
                    "VALUES (%s, %s, %s, %s, %s, %s)")
    
    descriptions = [
        "A large plot with excellent road access, perfect for residential development.",
        "Prime commercial land with high visibility, located near the main highway.",
        "Fertile agricultural land with a reliable water source, ideal for farming.",
        "Spacious residential plot in a quiet and developing neighborhood.",
        "Well-located commercial land in a bustling town center.",
        "Extensive agricultural land suitable for large-scale crop cultivation.",
        "A small residential plot in a fast-growing suburban area.",
        "Industrial-zoned land with easy access to transport and utilities.",
        "Vast agricultural property with a mix of arable and grazing land.",
        "A premium residential plot in a prime urban location with excellent amenities."
    ]

    for data in SAMPLE_DATA:
        random_price = random.uniform(data["price_min"], data["price_max"])
        random_price = round(random_price, 2)
        
        description_index = random.randint(0, len(descriptions) - 1)
        description = descriptions[description_index]

        record = (data["district"], data["mandal"], data["type_of_land"], data["size_acres"], random_price, description)
        try:
            cursor.execute(insert_query, record)
        except mysql.connector.Error as err:
            print(f"Error inserting data: {err}")

    cnx.commit()
    print("Sample data insertion complete.")


if __name__ == '__main__':
    create_database_and_table()
