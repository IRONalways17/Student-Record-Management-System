from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    roll_number = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    grade = db.Column(db.String(10))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by = db.Column(db.String(80))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    students = Student.query.order_by(Student.created_at.desc()).paginate(
        page=page, per_page=app.config['RECORDS_PER_PAGE']
    )
    return render_template('dashboard.html', students=students)

@app.route('/add_student', methods=['GET', 'POST'])
@login_required
def add_student():
    if request.method == 'POST':
        try:
            student = Student(
                name=request.form['name'],
                roll_number=request.form['roll_number'],
                email=request.form['email'],
                grade=request.form['grade'],
                created_by=current_user.username
            )
            db.session.add(student)
            db.session.commit()
            flash('Student added successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error adding student: {str(e)}', 'error')
            return redirect(url_for('add_student'))

    return render_template('student_form.html')

@app.route('/edit_student/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_student(id):
    student = Student.query.get_or_404(id)
    if request.method == 'POST':
        try:
            student.name = request.form['name']
            student.roll_number = request.form['roll_number']
            student.email = request.form['email']
            student.grade = request.form['grade']
            db.session.commit()
            flash('Student updated successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error updating student: {str(e)}', 'error')
            return redirect(url_for('edit_student', id=id))

    return render_template('student_form.html', student=student)

@app.route('/delete_student/<int:id>')
@login_required
def delete_student(id):
    student = Student.query.get_or_404(id)
    try:
        db.session.delete(student)
        db.session.commit()
        flash('Student deleted successfully!', 'success')
    except Exception as e:
        flash(f'Error deleting student: {str(e)}', 'error')
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
        
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            user.last_login = datetime.utcnow()
            db.session.commit()
            login_user(user)
            return redirect(url_for('index'))
        flash('Invalid username or password', 'error')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/search')
@login_required
def search():
    query = request.args.get('query', '')
    students = Student.query.filter(
        (Student.name.ilike(f'%{query}%')) |
        (Student.roll_number.ilike(f'%{query}%')) |
        (Student.email.ilike(f'%{query}%'))
    ).all()
    return jsonify([{
        'id': s.id,
        'name': s.name,
        'roll_number': s.roll_number,
        'email': s.email,
        'grade': s.grade
    } for s in students])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Create admin user if not exists
        if not User.query.filter_by(username=app.config['ADMIN_USERNAME']).first():
            admin = User(
                username=app.config['ADMIN_USERNAME'],
                password_hash=generate_password_hash(app.config['ADMIN_PASSWORD']),
                is_admin=True
            )
            db.session.add(admin)
            db.session.commit()
    app.run(debug=True)