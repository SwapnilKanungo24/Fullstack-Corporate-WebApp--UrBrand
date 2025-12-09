"""
Main Flask application entry point.
Initializes the Flask app, registers blueprints, and sets up routes for serving frontend files.

This application provides:
- RESTful API endpoints for projects, clients, contacts, and newsletter
- Image upload and processing functionality
- Frontend file serving
"""

from flask import Flask, send_file, send_from_directory
from flask_cors import CORS
import os

# Import configuration
from config import (
    DEBUG, PORT, HOST,
    UPLOAD_FOLDER, PROJECTS_FOLDER, CLIENTS_FOLDER
)

# Import route blueprints
from routes.projects import projects_bp
from routes.clients import clients_bp
from routes.contacts import contacts_bp
from routes.newsletter import newsletter_bp

# Initialize Flask application
app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)  # Enable CORS for all routes

# Ensure upload directories exist
os.makedirs(PROJECTS_FOLDER, exist_ok=True)
os.makedirs(CLIENTS_FOLDER, exist_ok=True)

# Register API route blueprints
app.register_blueprint(projects_bp)
app.register_blueprint(clients_bp)
app.register_blueprint(contacts_bp)
app.register_blueprint(newsletter_bp)


# ============================================================================
# Frontend File Serving Routes
# ============================================================================

@app.route('/')
def index():
    """
    Serve the main landing page.
    
    Returns:
        HTML: Landing page (index.html)
    """
    return send_file('../frontend/index.html')


@app.route('/admin')
def admin():
    """
    Serve the admin panel page.
    
    Returns:
        HTML: Admin panel page (admin/index.html)
    """
    return send_file('../frontend/admin/index.html')


@app.route('/css/<path:filename>')
def css_files(filename):
    """
    Serve CSS files for the landing page.
    
    Args:
        filename: Name of the CSS file
        
    Returns:
        File: CSS file from frontend/css directory
    """
    return send_from_directory('../frontend/css', filename)


@app.route('/js/<path:filename>')
def js_files(filename):
    """
    Serve JavaScript files for the landing page.
    
    Args:
        filename: Name of the JavaScript file
        
    Returns:
        File: JavaScript file from frontend/js directory
    """
    return send_from_directory('../frontend/js', filename)


@app.route('/admin/css/<path:filename>')
def admin_css_files(filename):
    """
    Serve CSS files for the admin panel.
    
    Args:
        filename: Name of the CSS file
        
    Returns:
        File: CSS file from frontend/admin/css directory
    """
    return send_from_directory('../frontend/admin/css', filename)


@app.route('/admin/js/<path:filename>')
def admin_js_files(filename):
    """
    Serve JavaScript files for the admin panel.
    
    Args:
        filename: Name of the JavaScript file
        
    Returns:
        File: JavaScript file from frontend/admin/js directory
    """
    return send_from_directory('../frontend/admin/js', filename)


# ============================================================================
# Application Entry Point
# ============================================================================

if __name__ == '__main__':
    """
    Run the Flask development server.
    
    The server will start on the configured host and port,
    with debug mode enabled for development.
    """
    print(f"""
    ╔═══════════════════════════════════════════════════════════╗
    ║         Full-Stack Application Server Starting            ║
    ╠═══════════════════════════════════════════════════════════╣
    ║  Server: http://{HOST}:{PORT}                              ║
    ║  Landing Page: http://{HOST}:{PORT}/                      ║
    ║  Admin Panel: http://{HOST}:{PORT}/admin                   ║
    ║  API Base URL: http://{HOST}:{PORT}/api                   ║
    ║  Debug Mode: {'Enabled' if DEBUG else 'Disabled'}                          ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    
    app.run(debug=DEBUG, host=HOST, port=PORT)
