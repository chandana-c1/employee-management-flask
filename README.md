# Employee Management System (Flask)

## 📌 Overview
This project is a simple REST API built using Flask to manage employee records. It allows users to add and retrieve employee details through HTTP endpoints.

## 🚀 Features
- Add new employees
- View all employees
- Store data using SQLite database

## 🛠 Tech Stack
- Python
- Flask
- SQLAlchemy
- SQLite

## 📂 Project Structure
- app.py → Main application file
- Database handled using SQLAlchemy ORM

## 🔗 API Endpoints

### ➤ Add Employee
POST /employees

Request:
{
  "name": "Chandana",
  "email": "test@gmail.com",
  "department": "IT"
}

Response:
{
  "message": "Employee added"
}

---

### ➤ Get All Employees
GET /employees

Response:
```json
[
  {
    "id": 1,
    "name": "Chandana",
    "email": "test@gmail.com",
    "department": "IT"
  }
]

## 💡 What I Learned
- Building REST APIs using Flask
- Handling database operations with SQLAlchemy
- Structuring backend applications

## 📌 Future Improvements
- Add update API
- Add delete API
- Add frontend UI
