from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

def get_connection():
    return pymysql.connect(
        host="yoshida-test-database.cos6yk8rcmir.ap-northeast-1.rds.amazonaws.com",
        user="admin",
        password="tiger123",
        database="yoshida_db",
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route("/")
def index():
    return "Ec2 Flack OK"

@app.route("/users")
def users():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, value FROM yoshida_test_table LIMIT 1")
            result = cursor.fetchall()
            return jsonify(result)
    finally:
        conn.close()

if __name__ == "__main__":
    app.run()
