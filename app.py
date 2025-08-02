from flask import Flask, request, jsonify
import os
import psycopg2  # Для PostgreSQL

app = Flask(__name__)


# Подключение к базе
def get_db():
    return psycopg2.connect(os.getenv("DATABASE_URL"))


@app.route('/api/check_license', methods=['POST'])
def check_license():
    data = request.json
    key = data.get('key')

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM license_keys WHERE key_value = %s", (key,))
    license_data = cursor.fetchone()

    if not license_data:
        return jsonify({"valid": False})

    return jsonify({"valid": True})


if __name__ == '__main__':
    app.run()