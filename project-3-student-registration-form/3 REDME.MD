# 🎓 Student Registration Application using Amazon EC2 & Amazon RDS

## 📌 Project Overview

This project demonstrates the deployment of a **Student Registration Application** using **Amazon EC2** as the web/application server and **Amazon RDS MySQL** as the database server.

The application allows users to enter student details through a web form. The submitted student information is securely stored in the RDS MySQL database and can be retrieved and displayed from the application.

---

## 🏗️ Architecture

```text
                Internet
                    |
                    |
              Public IP / DNS
                    |
                    ▼
              Amazon EC2
          Web/Application Server
                    |
                    |
          Secure Database Connection
                    |
                    ▼
             Amazon RDS
              MySQL Database
                    |
                    ▼
            Student Records
```

---

## ☁️ AWS Services Used

* **Amazon EC2** – Hosts the student registration application
* **Amazon RDS** – Hosts the MySQL database
* **Amazon VPC** – Provides network isolation
* **Security Groups** – Controls inbound and outbound traffic
* **MySQL** – Stores student registration records
* **Linux** – Operating system for the EC2 instance

---

## 🛠️ Technologies Used

* AWS EC2
* AWS RDS
* MySQL
* HTML
* CSS
* Python / Flask
* Linux
* Git & GitHub

---

# 🚀 Project Setup

## 1. Launch EC2 Instance

Create an EC2 instance with:

* Operating System: Amazon Linux / Ubuntu
* Instance Type: Free Tier eligible instance
* Security Group:

  * SSH – Port `22`
  * HTTP – Port `80`
  

Example:

```text
EC2 Instance
Public IP: <# 🎓 Student Registration Application using Amazon EC2 & Amazon RDS

## 📌 Project Overview

This project demonstrates the deployment of a **Student Registration Application** using **Amazon EC2** as the web/application server and **Amazon RDS MySQL** as the database server.

The application allows users to enter student details through a web form. The submitted student information is securely stored in the RDS MySQL database and can be retrieved and displayed from the application.

---

## 🏗️ Architecture

```text
                Internet
                    |
                    |
              Public IP / DNS
                    |
                    ▼
              Amazon EC2
          Web/Application Server
                    |
                    |
          Secure Database Connection
                    |
                    ▼
             Amazon RDS
              MySQL Database
                    |
                    ▼
            Student Records
```

---

## ☁️ AWS Services Used

* **Amazon EC2** – Hosts the student registration application
* **Amazon RDS** – Hosts the MySQL database
* **Amazon VPC** – Provides network isolation
* **Security Groups** – Controls inbound and outbound traffic
* **MySQL** – Stores student registration records
* **Linux** – Operating system for the EC2 instance

---

## 🛠️ Technologies Used

* AWS EC2
* AWS RDS
* MySQL
* HTML
* CSS
* Python / Flask
* Linux
* Git & GitHub

---

# 🚀 Project Setup

## 1. Launch EC2 Instance

Create an EC2 instance with:

* Operating System: Amazon Linux / Ubuntu
* Instance Type: Free Tier eligible instance
* Security Group:

  * SSH – Port `22`
  * HTTP – Port `80`


Example:

```text
EC2 Instance
Public IP: <3.144.121.61>
```

---

## 2. Connect to EC2

Connect to the EC2 instance using SSH.

```bash
ssh -i "aws-key.pem" ec2-user@<3.144.121.61>

```

---

## 3. Install Required Packages



```bash
sudo dnf update -y
sudo dnf install python3 -y
sudo dnf install git -y
```

Install Flask and MySQL connector:

```bash
pip3 install flask mysql-connector-python
```

---

# 🗄️ 4. Create Amazon RDS MySQL Database

Create an RDS MySQL database with:

```text
Engine       : MySQL
Database     : studentdb
Username     : admin
Password     : ********
Port         : 3306
```

Make sure the RDS Security Group allows MySQL traffic:

```text
Type       : MySQL/Aurora
Port       : 3306
Source     : EC2 Security Group
```

> For better security, allow port `3306` from the EC2 Security Group instead of allowing `0.0.0.0/0`.

---

# 🔐 5. Configure Database Connection

Get the RDS endpoint from:

**AWS Console → RDS → Databases →  Database → Connectivity & security**


```

Application database configuration:

```python
DB_HOST = "student-database.xxxxxxxxx.us-east-2.rds.amazonaws.com"
DB_PORT = 3306
DB_NAME = "studentdb"
DB_USER = "admin"
DB_PASSWORD = "-password"
```

---

# 🗃️ 6. Create Database and Table

Connect to the RDS MySQL database:

```bash
mysql -h <RDS-ENDPOINT> -P 3306 -u admin -p
```

Create the database:

```sql
CREATE DATABASE studentdb;
```

Select the database:

```sql
USE studentdb;
```

Create the student table:

```sql
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    course VARCHAR(100),
    phone VARCHAR(15)
);
```

Check the table:

```sql
SHOW TABLES;
```

---

# 💻 7. git clone

git clone https://github.com/xyz-GITHUB-USERNAME/student-registration-app.git

```

---


```


---

# ▶️ 8. Run the Application

Start the Flask application:

```bash
sudo python3 app.py
```

The application will run on:

```text
http://<EC2-PUBLIC-IP>
```

Open the EC2 public IP in a web browser.

---

# ➕ 9. Insert Student Record

Enter student details in the registration form.


```text
Name    : Rahul 
Email   : rahul@gmail.com
Course  : AWS Cloud
```

Click:

```text
Register Student
```

Expected result:

```text
Student registered successfully!
```

---

# 🔍 10. Verify Data in RDS MySQL

Connect to the RDS database:

```bash
mysql -h <RDS-ENDPOINT> -P 3306 -u admin -p
```

Select the database:

```sql
USE studentdb;
```

Retrieve student records:

```sql
SELECT * FROM students;
```

Example output:

```text
+----+-------------+---------------------+-----------+
| id | name        | email               | course    |       |
+----+-------------+---------------------+-----------+
|  1 | Rahul       | rahul@gmail.com     | AWS Cloud | 
+----+-------------+---------------------+-----------+
```

This confirms that the student data was
>
```

---
```

### Registration form

![Registration-form](./images/Registration-form) 


![Student Records](./images/database)

![Student Records](./images/data)







