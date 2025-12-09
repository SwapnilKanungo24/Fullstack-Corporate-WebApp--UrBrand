"""
Project management routes.
Handles CRUD operations for projects including image upload and processing.
"""

from flask import Blueprint, request, jsonify, send_from_directory
from bson import ObjectId
import os
from database import projects_collection
from config import PROJECTS_FOLDER, API_BASE_URL
from utils import process_uploaded_image, allowed_file

# Create blueprint for project routes
projects_bp = Blueprint('projects', __name__)


@projects_bp.route(f'{API_BASE_URL}/projects', methods=['GET'])
def get_projects():
    """
    Retrieve all projects from the database.
    
    Returns:
        JSON: List of all projects with their details
    """
    try:
        projects = list(projects_collection.find())
        for project in projects:
            project['_id'] = str(project['_id'])
        return jsonify(projects), 200
    except Exception as e:
        return jsonify({'error': f'Error retrieving projects: {str(e)}'}), 500


@projects_bp.route(f'{API_BASE_URL}/projects', methods=['POST'])
def add_project():
    """
    Add a new project with image upload.
    The image is automatically cropped to 450x350 pixels.
    
    Expected form data:
        - image: Image file (required)
        - name: Project name (required)
        - description: Project description (required)
    
    Returns:
        JSON: Created project object with ID
    """
    try:
        # Validate image file
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400
        
        file = request.files['image']
        name = request.form.get('name')
        description = request.form.get('description')
        
        # Validate required fields
        if file.filename == '' or not name or not description:
            return jsonify({'error': 'Missing required fields: image, name, and description are required'}), 400
        
        # Validate file type
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type. Allowed types: png, jpg, jpeg, gif, webp'}), 400
        
        # Process and crop the image
        cropped_filename = process_uploaded_image(file, PROJECTS_FOLDER)
        
        # Create project document
        project = {
            'name': name,
            'description': description,
            'image': cropped_filename
        }
        
        # Save to database
        result = projects_collection.insert_one(project)
        project['_id'] = str(result.inserted_id)
        
        return jsonify(project), 201
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Error adding project: {str(e)}'}), 500


@projects_bp.route(f'{API_BASE_URL}/projects/<project_id>', methods=['DELETE'])
def delete_project(project_id):
    """
    Delete a project by ID.
    Also removes the associated image file from the server.
    
    Args:
        project_id (str): MongoDB ObjectId of the project to delete
    
    Returns:
        JSON: Success message or error
    """
    try:
        # Validate ObjectId format
        if not ObjectId.is_valid(project_id):
            return jsonify({'error': 'Invalid project ID format'}), 400
        
        # Find the project
        project = projects_collection.find_one({'_id': ObjectId(project_id)})
        
        if not project:
            return jsonify({'error': 'Project not found'}), 404
        
        # Delete associated image file
        if 'image' in project:
            image_path = os.path.join(PROJECTS_FOLDER, project['image'])
            if os.path.exists(image_path):
                try:
                    os.remove(image_path)
                except OSError as e:
                    # Log error but continue with database deletion
                    print(f'Warning: Could not delete image file: {e}')
        
        # Delete from database
        projects_collection.delete_one({'_id': ObjectId(project_id)})
        
        return jsonify({'message': 'Project deleted successfully'}), 200
        
    except Exception as e:
        return jsonify({'error': f'Error deleting project: {str(e)}'}), 500


@projects_bp.route('/uploads/projects/<filename>')
def project_image(filename):
    """
    Serve project images.
    
    Args:
        filename (str): Name of the image file
    
    Returns:
        File: Image file from the projects upload folder
    """
    return send_from_directory(PROJECTS_FOLDER, filename)

