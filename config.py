import os
from datetime import timedelta

class Config:
    # Basic Flask config
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'IRONalways17-secret-key-2025'
    
    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///students.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Session config
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)
    
    # Application config
    RECORDS_PER_PAGE = 10
    ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME', 'admin')
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'admin123')
    
    # System Info
    SYSTEM_INFO = {
        'created_by': 'IRONalways17',
        'last_updated': '2025-02-24 16:44:22'
    }