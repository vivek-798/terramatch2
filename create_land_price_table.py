# A script to connect to a MySQL server and create a land prices database and table.
# It now also inserts an expanded set of sample data with a random price per acre.
#
# Prerequisites:
# 1. A running MySQL server.
# 2. The 'mysql-connector-python' library installed.
#    You can install it using pip: `pip install mysql-connector-python`

import mysql.connector
from mysql.connector import errorcode
import random

# --- Configuration: Updated to work without a password. ---
# Using 'root' as the default user for local development.
DB_HOST = "localhost" # The host where your MySQL server is running (e.g., "localhost")
DB_USER = "root"  
DB_PASSWORD = "" # An empty string for the password.
DB_NAME = "terramatch_prices" # The name of the database to be created

TABLES = {}
TABLES['landPrices'] = (
    "CREATE TABLE `landPrices` ("
    "  `id` INT NOT NULL AUTO_INCREMENT,"
    "  `district` VARCHAR(255) NOT NULL,"
    "  `mandal` VARCHAR(255) NOT NULL,"
    "  `pricePerAcre` DECIMAL(10, 2) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

# Expanded sample data to be inserted into the landPrices table.
# We'll generate a random price per acre within a specified range.
SAMPLE_DATA = [
    {"district": "karimnagar", "mandal": "thimmapur", "price_range_min": 25000, "price_range_max": 50000},
    {"district": "karimnagar", "mandal": "jagityal", "price_range_min": 30000, "price_range_max": 60000},
    {"district": "karimnagar", "mandal": "husnabad", "price_range_min": 28000, "price_range_max": 55000},
    {"district": "karimnagar", "mandal": "manakondur", "price_range_min": 27000, "price_range_max": 53000},
    {"district": "karimnagar", "mandal": "gangadhara", "price_range_min": 26000, "price_range_max": 52000},
    {"district": "karimnagar", "mandal": "choppadandi", "price_range_min": 29000, "price_range_max": 58000},
    {"district": "karimnagar", "mandal": "huzurabad", "price_range_min": 32000, "price_range_max": 65000},
    {"district": "karimnagar", "mandal": "veenavanka", "price_range_min": 24000, "price_range_max": 48000},
    {"district": "karimnagar", "mandal": "jammikunta", "price_range_min": 35000, "price_range_max": 70000},

    {"district": "warangal", "mandal": "hanamkonda", "price_range_min": 70000, "price_range_max": 150000},
    {"district": "warangal", "mandal": "parkal", "price_range_min": 45000, "price_range_max": 80000},
    {"district": "warangal", "mandal": "narsampet", "price_range_min": 50000, "price_range_max": 95000},
    {"district": "warangal", "mandal": "wardhannapet", "price_range_min": 55000, "price_range_max": 100000},
    {"district": "warangal", "mandal": "chennaraopet", "price_range_min": 40000, "price_range_max": 75000},
    {"district": "warangal", "mandal": "duggondi", "price_range_min": 42000, "price_range_max": 78000},
    {"district": "warangal", "mandal": "atmakur", "price_range_min": 48000, "price_range_max": 85000},
    {"district": "warangal", "mandal": "ghanpur(mulug)", "price_range_min": 38000, "price_range_max": 70000},

    {"district": "hyderabad", "mandal": "gachibowli", "price_range_min": 200000, "price_range_max": 500000},
    {"district": "hyderabad", "mandal": "manikonda", "price_range_min": 180000, "price_range_max": 450000},
    {"district": "hyderabad", "mandal": "shamshabad", "price_range_min": 150000, "price_range_max": 300000},
    {"district": "hyderabad", "mandal": "secunderabad", "price_range_min": 220000, "price_range_max": 550000},
    {"district": "hyderabad", "mandal": "banjara hills", "price_range_min": 250000, "price_range_max": 600000},
    {"district": "hyderabad", "mandal": "jubilee hills", "price_range_min": 280000, "price_range_max": 700000},
    {"district": "hyderabad", "mandal": "mehdipatnam", "price_range_min": 190000, "price_range_max": 480000},
    {"district": "hyderabad", "mandal": "musheerabad", "price_range_min": 170000, "price_range_max": 420000},
    {"district": "hyderabad", "mandal": "amberpet", "price_range_min": 160000, "price_range_max": 400000},

    {"district": "medchal", "mandal": "quthbullapur", "price_range_min": 120000, "price_range_max": 250000},
    {"district": "medchal", "mandal": "balanagar", "price_range_min": 130000, "price_range_max": 260000},
    {"district": "medchal", "mandal": "medchal", "price_range_min": 110000, "price_range_max": 240000},
    {"district": "medchal", "mandal": "shamirpet", "price_range_min": 100000, "price_range_max": 220000},
    {"district": "medchal", "mandal": "keesara", "price_range_min": 90000, "price_range_max": 200000},
    {"district": "medchal", "mandal": "ghatkesar", "price_range_min": 85000, "price_range_max": 180000},

    {"district": "ranga reddy", "mandal": "ibrahimpatnam", "price_range_min": 60000, "price_range_max": 120000},
    {"district": "ranga reddy", "mandal": "shahbad", "price_range_min": 55000, "price_range_max": 110000},
    {"district": "ranga reddy", "mandal": "moinabad", "price_range_min": 70000, "price_range_max": 130000},
    {"district": "ranga reddy", "mandal": "rajendranagar", "price_range_min": 80000, "price_range_max": 150000},
    {"district": "ranga reddy", "mandal": "chevella", "price_range_min": 65000, "price_range_max": 125000},
    {"district": "ranga reddy", "mandal": "kandukur", "price_range_min": 75000, "price_range_max": 140000},

    {"district": "nizamabad", "mandal": "armur", "price_range_min": 40000, "price_range_max": 80000},
    {"district": "nizamabad", "mandal": "bodhan", "price_range_min": 35000, "price_range_max": 75000},
    {"district": "nizamabad", "mandal": "nizamabad(urban)", "price_range_min": 45000, "price_range_max": 90000},
    {"district": "nizamabad", "mandal": "nizamabad(rural)", "price_range_min": 42000, "price_range_max": 85000},
    {"district": "nizamabad", "mandal": "dichpally", "price_range_min": 38000, "price_range_max": 78000},
    {"district": "nizamabad", "mandal": "makloor", "price_range_min": 36000, "price_range_max": 76000},

    {"district": "adilabad", "mandal": "ichoda", "price_range_min": 20000, "price_range_max": 45000},
    {"district": "adilabad", "mandal": "gudihatnoor", "price_range_min": 18000, "price_range_max": 40000},
    {"district": "adilabad", "mandal": "adilabad", "price_range_min": 22000, "price_range_max": 50000},
    {"district": "adilabad", "mandal": "talamadugu", "price_range_min": 19000, "price_range_max": 42000},
    {"district": "adilabad", "mandal": "boath", "price_range_min": 21000, "price_range_max": 47000},
    {"district": "adilabad", "mandal": "bazarhathnoor", "price_range_min": 17000, "price_range_max": 38000},

    {"district": "mahbubnagar", "mandal": "jadcherla", "price_range_min": 45000, "price_range_max": 90000},
    {"district": "mahbubnagar", "mandal": "mahbubnagar", "price_range_min": 50000, "price_range_max": 100000},
    {"district": "mahbubnagar", "mandal": "badepally", "price_range_min": 48000, "price_range_max": 95000},
    {"district": "mahbubnagar", "mandal": "kothakota", "price_range_min": 42000, "price_range_max": 85000},
    {"district": "mahbubnagar", "mandal": "deverakadra", "price_range_min": 40000, "price_range_max": 80000},

    {"district": "nalgonda", "mandal": "nalgonda", "price_range_min": 60000, "price_range_max": 120000},
    {"district": "nalgonda", "mandal": "miryalaguda", "price_range_min": 55000, "price_range_max": 110000},
    {"district": "nalgonda", "mandal": "suryapet", "price_range_min": 65000, "price_range_max": 130000},
    {"district": "nalgonda", "mandal": "kodad", "price_range_min": 58000, "price_range_max": 115000},
    {"district": "nalgonda", "mandal": "huzurnagar", "price_range_min": 52000, "price_range_max": 105000},
]

def create_database_and_table():
    """
    Connects to a MySQL server, creates a database if it doesn't exist,
    and then creates the `landPrices` table.
    """
    cnx = None
    cursor = None
    try:
        # First, connect to the MySQL server without specifying a database.
        # This connection is for creating the database itself.
        cnx = mysql.connector.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
        cursor = cnx.cursor()

        # Create the database if it doesn't exist.
        try:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}` DEFAULT CHARACTER SET 'utf8'")
            print(f"Database '{DB_NAME}' checked/created successfully.")
        except mysql.connector.Error as err:
            print(f"Failed to create database: {err}")
            return

        # Close the initial connection and reconnect with the new database selected.
        cursor.close()
        cnx.close()
        
        # Now, connect to the specific database.
        cnx = mysql.connector.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            database=DB_NAME
        )
        cursor = cnx.cursor()

        # Create the table.
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
                # If the table was just created, insert some sample data
                insert_sample_data(cursor, cnx)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(f"An error occurred: {err}")
    finally:
        # Close the cursor and connection to free up resources.
        if cursor:
            cursor.close()
        if cnx and cnx.is_connected():
            cnx.close()
            print("MySQL connection is closed.")


def insert_sample_data(cursor, cnx):
    """
    Inserts sample land price data into the database.
    """
    print("Inserting sample data...")
    insert_query = ("INSERT INTO `landPrices` "
                    "(`district`, `mandal`, `pricePerAcre`) "
                    "VALUES (%s, %s, %s)")
    
    for data in SAMPLE_DATA:
        # Generate a random price within the specified range
        random_price = random.uniform(data["price_range_min"], data["price_range_max"])
        # Round to two decimal places
        random_price = round(random_price, 2)
        
        record = (data["district"], data["mandal"], random_price)
        try:
            cursor.execute(insert_query, record)
            print(f"Inserted: {data['district']}, {data['mandal']} with price {random_price}")
        except mysql.connector.Error as err:
            print(f"Error inserting data: {err}")

    # Commit the changes to the database
    cnx.commit()
    print("Sample data insertion complete.")


if __name__ == '__main__':
    create_database_and_table()
