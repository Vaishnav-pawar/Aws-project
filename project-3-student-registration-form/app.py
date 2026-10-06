```python
from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# RDS MySQL Configuration
DB_HOST = "YOUR-RDS-ENDPOINT"
DB_PORT = 3306
DB_NAME = "studentdb"
DB_USER = "admin"
DB_PASSWORD = "YOUR-RDS-PASSWORD"


def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Register Student
@app.route("/register", methods=["POST"])
def register():

    name = request.form["name"]
    email = request.form["email"]
    course = request.form["course"]
    phone = request.form["phone"]

    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO students (name, email, course, phone)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (name, email, course, phone))
    connection.commit()

    cursor.close()
    connection.close()

    return """
    <h2>Student Registered Successfully!</h2>
    <a href="/">Register Another Student</a>
    """


# Display Students
@app.route("/students")
def students():

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    cursor.close()
    connection.close()

    return records


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
```
