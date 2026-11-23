# 🏡 Homely – Full Stack E-Commerce Web Application

Homely is a full-stack e-commerce web application built using **Django (Backend)** and **HTML, CSS, JavaScript (Frontend)**. The platform allows users to browse dry fruits, nuts, seeds, and related products, add them to cart, and complete checkout with delivery and payment options.

This project demonstrates real-world full-stack development including frontend UI, backend APIs, database integration, authentication, and cloud image storage.

---

# 📌 Project Features

## 👤 User Features

* Browse products by category
* View product details
* Add products to cart
* Update cart quantity
* Remove products from cart
* Checkout with delivery address
* Select payment method (Cash on Delivery / UPI)
* Responsive modern UI
* Search functionality

---

## ⚙️ Backend Features

* REST API built using Django REST Framework
* Product management system
* Order management system
* User management system
* JWT Authentication support
* Cloudinary cloud image storage
* Environment variable protection using .env

---

# 🧱 Tech Stack

## Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap

## Backend

* Django 4.2.7
* Django REST Framework
* SimpleJWT Authentication

## Database

* SQLite (development)
* MySQL (production supported)

## Cloud Storage

* Cloudinary
* django-cloudinary-storage

## Deployment

* Netlify (Frontend)

---

# 📁 Project Structure

```
Homely/
│
├── backend/
│   ├── admin_api/
│   ├── products/
│   ├── users/
│   ├── orders/
│   ├── backend/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── __init__.py
│   ├── manage.py
│   ├── requirements.txt
│   ├── db.sqlite3
│   └── .env
│
└── frontend/
    ├── assets/
    │   ├── images/
    │   └── logo.png
    │
    ├── css/
    │   ├── home.css
    │   ├── cart.css
    │   ├── checkout.css
    │   └── products.css
    │
    ├── js/
    │   ├── home.js
    │   ├── cart.js
    │   ├── products.js
    │   ├── login.js
    │   └── utils.js
    │
    ├── index.html
    ├── cart.html
    ├── checkout.html
    ├── login.html
    └── about-us.html
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone the Repository

```
git clone https://github.com/Addy12076/Homely
cd homely/backend
```

---

## 2️⃣ Create Virtual Environment

```
python -m venv venv
```

Activate environment:

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

---

## 3️⃣ Install Requirements

```
pip install -r requirements.txt
```

---

## 4️⃣ Setup Database

Run migrations:

```
python manage.py migrate
```

---

## 5️⃣ Run Backend Server

```
python manage.py runserver
```

Backend will run on:

```
http://127.0.0.1:8000/
```

---

## 6️⃣ Run Frontend

Open:

```
frontend/index.html
```

OR run using Live Server extension in VS Code.

---

# 🔐 Environment Variables (.env)

Example .env file:

```
# ===============================
# DATABASE CONFIG (MySQL)
# ===============================
DB_NAME=homely
DB_USER=root
DB_PASSWORD=aditya@11
DB_HOST=127.0.0.1
DB_PORT=3306

# ===============================
# DJANGO SECRET KEY
# ===============================
SECRET_KEY=django-insecure-homely-secret-key


CLOUDINARY_CLOUD_NAME=dttcujeop
CLOUDINARY_API_KEY=834118361411876
CLOUDINARY_API_SECRET=cQptdNbol9s7r9fw1e5rIfBfljA

---

# 🗄️ Database Models

Your project contains:

## Products Model

* id
* name
* description
* price
* category
* image
* stock

## Users Model

* id
* username
* email
* password

## Orders Model

* id
* user
* product
* quantity
* total price
* delivery address
* payment method

---

# 🔌 API Endpoints

Example endpoints:

```
/api/products/
/api/users/
/api/orders/
/api/admin/
```

---

# ☁️ Cloudinary Integration

Used for storing product images securely in cloud.

Benefits:

* Fast image delivery
* Reduced server load
* Scalable

---

# 🛒 Cart System

Cart supports:

* Add product
* Remove product
* Update quantity
* Calculate total price

Handled using:

```
frontend/js/cart.js
```

---

# 💳 Checkout System

Checkout includes:

Step 1: Delivery Address
Step 2: Payment Method

Payment options:

* Cash on Delivery
* UPI

---

# 🚀 Deployment

Frontend:

Deploy on Netlify

Backend:

Deploy on Render or Railway

---

# 🎯 Learning Outcomes

This project demonstrates:

* Full stack development
* Django REST API development
* Frontend development
* Database integration
* Cloud storage integration
* Deployment process

---

# 📄 License

This project is developed for educational purposes.
