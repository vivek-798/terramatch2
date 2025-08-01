# File: create_site_visit_table.py
# A script to connect to the MySQL server and create a new table
# for storing site visit requests.
#
# Prerequisites:
# 1. A running MySQL server.
# 2. The 'mysql-connector-python' library installed.
#    You can install it using pip: `pip install mysql-connector-python`

import mysql.connector
from mysql.connector import errorcode

# --- Configuration ---
# Uses the same configuration as your other backend files.
DB_HOST = "localhost" 
DB_USER = "root"  
DB_PASSWORD = ""
DB_NAME = "terramatch_properties" 

TABLES = {}
TABLES['siteVisitRequests'] = (
    "CREATE TABLE `siteVisitRequests` ("
    "  `id` INT NOT NULL AUTO_INCREMENT,"
    "  `user_id` INT NOT NULL,"
    "  `property_id` INT NOT NULL,"
    "  `status` VARCHAR(50) NOT NULL DEFAULT 'pending',"
    "  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    "  PRIMARY KEY (`id`),"
    "  FOREIGN KEY (`property_id`) REFERENCES `properties`(`id`)"
    ") ENGINE=InnoDB")

def create_table():
    """
    Connects to the database and creates the `siteVisitRequests` table.
    """
    cnx = None
    cursor = None
    try:
        cnx = mysql.connector.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            database=DB_NAME
        )
        cursor = cnx.cursor()

        table_name = 'siteVisitRequests'
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

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print(f"Database '{DB_NAME}' does not exist. Please run create_properties_table.py first.")
        else:
            print(f"An error occurred: {err}")
    finally:
        if cursor:
            cursor.close()
        if cnx and cnx.is_connected():
            cnx.close()
            print("MySQL connection is closed.")


if __name__ == '__main__':
    create_table()
