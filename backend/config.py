"""
Configuration settings for the Flask application.
Contains all configuration constants and settings.
"""

import os

# Flask Configuration
DEBUG = True
PORT = 5000
HOST = '0.0.0.0'

# MongoDB Configuration
MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')
DATABASE_NAME = 'fullstack_db'

# Upload Configuration
UPLOAD_FOLDER = 'uploads'
PROJECTS_FOLDER = os.path.join(UPLOAD_FOLDER, 'projects')
CLIENTS_FOLDER = os.path.join(UPLOAD_FOLDER, 'clients')

# Image Processing Configuration
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
TARGET_IMAGE_SIZE = (450, 350)  # Width x Height in pixels

# API Configuration
API_BASE_URL = '/api'

