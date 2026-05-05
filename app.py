from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    department = db.Column(db.String(100))

with app.app_context():
    db.create_all()

@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.json
    emp = Employee(name=data['name'], email=data['email'], department=data['department'])
    db.session.add(emp)
    db.session.commit()
    return jsonify({"message": "Employee added"})

@app.route('/employees', methods=['GET'])
def get_all():
    employees = Employee.query.all()
    return jsonify([{
        "id": e.id,
        "name": e.name,
        "email": e.email,
        "department": e.department
    } for e in employees])

app.run()
