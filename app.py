# File: app.py
# A Flask server to handle database connections and serve data to the frontend.
#
# Prerequisites:
# 1. The 'Flask' and 'mysql-connector-python' libraries installed.
#    You can install them using pip: `pip install Flask mysql-connector-python`

import mysql.connector
from flask import Flask, request, jsonify
from flask_cors import CORS

# --- Flask App Configuration ---
app = Flask(__name__)
CORS(app)  # This is important for allowing the frontend to make requests.

# --- MySQL Database Configuration ---
# Updated to work without a password, as requested.
# Please ensure your MySQL user (e.g., 'root') is configured for this.
DB_HOST = "localhost"
DB_USER = "root"  # Using 'root' as the default user for local development.
DB_PASSWORD = "" # An empty string for the password.
DB_NAME = "terramatch_prices"

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

@app.route('/districts', methods=['GET'])
def get_districts():
    """
    API endpoint to fetch all unique districts from the landPrices table.
    """
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500

    cursor = conn.cursor()
    try:
        cursor.execute("SELECT DISTINCT district FROM landPrices ORDER BY district")
        districts = [row[0] for row in cursor.fetchall()]
        return jsonify(districts)
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

@app.route('/mandals/<district>', methods=['GET'])
def get_mandals(district):
    """
    API endpoint to fetch all mandals for a given district.
    """
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500

    cursor = conn.cursor()
    try:
        # The district is case-insensitive in the comparison
        query = "SELECT mandal FROM landPrices WHERE LOWER(district) = LOWER(%s) ORDER BY mandal"
        cursor.execute(query, (district,))
        mandals = [row[0] for row in cursor.fetchall()]
        return jsonify(mandals)
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

@app.route('/price/<district>/<mandal>', methods=['GET'])
def get_price(district, mandal):
    """
    API endpoint to fetch the price per acre for a given district and mandal.
    """
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500

    cursor = conn.cursor(dictionary=True)
    try:
        # The district and mandal are case-insensitive in the comparison
        query = "SELECT pricePerAcre FROM landPrices WHERE LOWER(district) = LOWER(%s) AND LOWER(mandal) = LOWER(%s)"
        cursor.execute(query, (district, mandal))
        result = cursor.fetchone()
        if result:
            return jsonify({"pricePerAcre": float(result['pricePerAcre'])})
        else:
            return jsonify({"error": "Price not found"}), 404
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

if __name__ == '__main__':
    # Ensure you are not running in production with debug=True.
    app.run(debug=True)
