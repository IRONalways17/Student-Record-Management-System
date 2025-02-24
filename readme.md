# Student Record Management System

A Flask-based web application for managing student records with user authentication and CRUD operations.

## 🌟 Features

- User Authentication and Authorization
- Student Records Management (CRUD Operations)
- Responsive Dashboard
- Real-time Search Functionality
- Pagination
- Flash Messages for User Feedback
- Data Validation
- Clean and Modern UI with Bootstrap 5

## 📋 Prerequisites

- Python 3.9+
- pip (Python package manager)
- Git (optional)
- Web browser (Chrome/Firefox/Safari)

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite, SQLAlchemy
- **Frontend:** HTML5, CSS3, JavaScript
- **CSS Framework:** Bootstrap 5
- **Icons:** Bootstrap Icons
- **Authentication:** Flask-Login
- **Form Handling:** Flask-WTF

## 📁 Project Structure

```
student_records/
├── venv/                            # Virtual environment
├── instance/                        
│   └── students.db                  # SQLite database
├── static/                          
│   ├── css/
│   │   └── style.css               # Custom styles
│   ├── js/
│   │   └── main.js                 # JavaScript functions
│   └── images/                      
│       └── favicon.ico
├── templates/                       
│   ├── base.html                   # Base template
│   ├── dashboard.html              # Main view
│   ├── login.html                  # Login page
│   └── student_form.html           # Add/Edit form
├── app.py                          # Main application
├── config.py                       # Configuration
├── requirements.txt                # Dependencies
├── .env                           # Environment variables
├── .gitignore                     
└── README.md                      
```

## ⚙️ Installation & Setup

1. Clone the repository (or download ZIP):
```bash
git clone <repository-url>
cd student_records
```

2. Create and activate virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python -m venv venv
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create `.env` file in root directory:
```env
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///students.db
```

5. Initialize the database:
```bash
python
>>> from app import app, db
>>> with app.app_context():
...     db.create_all()
>>> exit()
```

6. Run the application:
```bash
python app.py
```

7. Access the application:
- URL: `http://localhost:5000`
- Default Admin Credentials:
  - Username: `admin`
  - Password: `admin123`

## 🔑 User Roles

- **Admin**: Full access to all features
  - Add/Edit/Delete student records
  - View all records
  - Search functionality
  - System management

## 💡 Usage

1. **Login**:
   - Use default admin credentials
   - System redirects to dashboard

2. **Dashboard**:
   - View all student records
   - Search functionality
   - Pagination controls

3. **Adding Students**:
   - Click "Add New Student"
   - Fill in required details
   - Submit form

4. **Editing Students**:
   - Click "Edit" on student record
   - Modify details
   - Save changes

5. **Deleting Students**:
   - Click "Delete" on student record
   - Confirm deletion

## 🔍 Search Functionality

- Real-time search
- Searches across:
  - Name
  - Roll Number
  - Email
  - Grade

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

- Created by: IRONalways17
- Last Updated: 2025-02-24 17:14:19 UTC

## 📞 Support

For support, please contact:
- Email: [your-email@example.com]
- Issue Tracker: [project-issues-url]

## 🔄 Version History

- v1.0.0 (2025-02-24)
  - Initial release
  - Basic CRUD operations
  - User authentication
  - Search functionality
  - Responsive design

## 🎯 Future Enhancements

1. Export data to CSV/Excel
2. Multiple user roles
3. Student attendance tracking
4. Profile image upload
5. Email notifications
6. Advanced reporting
7. API endpoints

## 🙏 Acknowledgments

- Flask Documentation
- Bootstrap Team
- SQLAlchemy Documentation
- Open Source Community

## ⚠️ Important Notes

- Change default admin credentials after first login
- Regularly backup the database
- Keep dependencies updated
- Monitor error logs
