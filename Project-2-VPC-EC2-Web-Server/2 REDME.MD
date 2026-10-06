# AWS VPC with Public Subnet and Ubuntu EC2

## 📌 Project Overview

This project demonstrates how to create a custom AWS VPC with one public subnet and deploy an Ubuntu EC2 instance.

The project includes configuring an Internet Gateway, Route Table, Security Group, installing Apache Web Server, and hosting a basic HTML webpage accessible through the EC2 public IP address.

---

## 🏗️ Architecture

```text
                    Internet
                       |
                       v
              Internet Gateway
                       |
                       v
                  AWS VPC
                10.0.0.0/16
                       |
                       v
              Public Subnet
                10.0.0.0/24
                       |
                       v
                Ubuntu EC2
                       |
                       v
              Apache Web Server
                       |
                       v
              Basic HTML Webpage
```

---

## 🛠️ AWS Services Used

* Amazon VPC
* Amazon EC2
* Internet Gateway
* Route Table
* Security Group
* Ubuntu Linux
* Apache Web Server

---

## ⚙️ Project Configuration

### 1. Create VPC

Created a custom VPC.

**VPC CIDR:**

```text
10.0.0.0/16
```

### 2. Create Public Subnet

Created one public subnet inside the VPC.

**Subnet CIDR:**

```text
10.0.0.0/24
```

### 3. Internet Gateway

Created an Internet Gateway and attached it to the custom VPC.

```text
VPC → Internet Gateway
```

### 4. Route Table

Created a route table and associated it with the public subnet.

**Route:**

```text
Destination: 0.0.0.0/0
Target: Internet Gateway
```

This route allows Internet traffic from the public subnet.

### 5. Security Group

Configured the Security Group with the following inbound rules:

| Type | Port | Source    |
| ---- | ---: | --------- |
| SSH  |   22 | 3.238.192.184    |
| HTTP |   80 | 0.0.0.0/0 |

### 6. Launch Ubuntu EC2

Launched an Ubuntu EC2 instance in the public subnet.

```text
Operating System: Ubuntu
Subnet: Public Subnet
Public IPv4: Enabled
Security Group: Web Server Security Group
```

### 7. Connect to EC2

Connected to the Ubuntu EC2 instance using SSH.

```bash
ssh -i -key.pem ubuntu@<3.238.192.184>
```

### 8. Install Apache Web Server

Updated the packages:

```bash
sudo apt update
```

Installed Apache:

```bash
sudo apt install apache2 -y
```

Checked Apache status:

```bash
sudo systemctl status apache2
```

Enabled Apache:

```bash
sudo systemctl enable apache2
```

### 9. Create HTML Webpage

Edited the Apache HTML file:

```bash
sudo nano /var/www/html/index.html
```

Added the following HTML:

```html
<!DOCTYPE html>
<html>
<head>
    <title>AWS EC2 Web Server</title>
</head>
<body>

    <h1>Welcome to My AWS Server</h1>

    <h2>Ubuntu EC2 Web Server</h2>

    <p>This webpage is hosted using Apache Web Server.</p>

    <p>AWS VPC Public Subnet Project</p>

</body>
</html>
```

Restarted Apache:

```bash
sudo systemctl restart apache2
```

---

## 🌐 Access the Website

The webpage can be accessed through the EC2 public IP address.

```text
http://<3.238.192.184>
```


```


---

## ✅ Project Outcome

Successfully created and configured:

* Custom AWS VPC
* One Public Subnet
* Internet Gateway
* Route Table
* Security Group
* Ubuntu EC2 Instance
* Apache Web Server
* Basic HTML Webpage

The webpage was successfully accessed through the EC2 public IP address.

---

## 🎯 Skills Demonstrated

* AWS VPC
* Amazon EC2
* Subnet Configuration
* Internet Gateway
* Route Tables
* Security Groups
* Ubuntu Linux
* Apache Web Server
* HTML
* SSH
* AWS Networking

---

```
## Screenshots

### VPC
![VPC](./images/vpc)


### Security Group
![Security Group](./images/security-group)

### Internet Gateway
![Internet Gateway](./images/internet-gateway)

### Server
![Server](./images/server)


### Web Page
![Web Page](./images/web-pag)




