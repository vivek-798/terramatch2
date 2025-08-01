# File: app_properties.py
# A Flask server to handle property database connections and API endpoints.
#
# Prerequisites:
# 1. The 'Flask' and 'mysql-connector-python' libraries installed.
#    You can install them using pip: `pip install Flask mysql-connector-python`

import mysql.connector
from flask import Flask, request, jsonify
from flask_cors import CORS

# --- Flask App Configuration ---
app = Flask(__name__)
CORS(app)

# --- MySQL Database Configuration ---
DB_HOST = "localhost"
DB_USER = "root"  
DB_PASSWORD = ""
DB_NAME = "terramatch_properties"

def get_db_connection():
    """Establishes and returns a new MySQL database connection."""
    try:
        conn = mysql.connector.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            database=DB_NAME
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        return None

@app.route('/properties', methods=['GET'])
def get_properties():
    """
    API endpoint to fetch all property listings.
    """
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500

    cursor = conn.cursor(dictionary=True)
    try:
        query = "SELECT id, district, mandal, type_of_land, size_acres, price, description FROM properties"
        cursor.execute(query)
        properties = cursor.fetchall()
        return jsonify(properties)
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

@app.route('/properties/search', methods=['GET'])
def search_properties():
    """
    API endpoint to search and filter property listings.
    """
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500

    cursor = conn.cursor(dictionary=True)
    try:
        search_query = request.args.get('q', '').lower()
        land_type = request.args.get('type', '').lower()
        price_range = request.args.get('price_range', '')
        
        sql_query = "SELECT id, district, mandal, type_of_land, size_acres, price, description FROM properties WHERE 1=1"
        query_params = []

        if search_query:
            sql_query += " AND (LOWER(district) LIKE %s OR LOWER(mandal) LIKE %s OR LOWER(description) LIKE %s)"
            search_pattern = f"%{search_query}%"
            query_params.extend([search_pattern, search_pattern, search_pattern])

        if land_type and land_type != 'all':
            sql_query += " AND LOWER(type_of_land) = %s"
            query_params.append(land_type)

        if price_range:
            min_price, max_price = map(int, price_range.split('-'))
            sql_query += " AND price BETWEEN %s AND %s"
            query_params.extend([min_price, max_price])

        cursor.execute(sql_query, query_params)
        properties = cursor.fetchall()
        return jsonify(properties)
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)
