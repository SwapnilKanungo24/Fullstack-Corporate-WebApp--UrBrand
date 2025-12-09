"""
Client management routes.
Handles CRUD operations for clients including image upload and processing.
"""

from flask import Blueprint, request, jsonify, send_from_directory
from bson import ObjectId
import os
from database import clients_collection
from config import CLIENTS_FOLDER, API_BASE_URL
from utils import process_uploaded_image, allowed_file

# Create blueprint for client routes
clients_bp = Blueprint('clients', __name__)


@clients_bp.route(f'{API_BASE_URL}/clients', methods=['GET'])
def get_clients():
    """
    Retrieve all clients from the database.
    
    Returns:
        JSON: List of all clients with their details
    """
    try:
        clients = list(clients_collection.find())
        for client in clients:
            client['_id'] = str(client['_id'])
        return jsonify(clients), 200
    except Exception as e:
        return jsonify({'error': f'Error retrieving clients: {str(e)}'}), 500


@clients_bp.route(f'{API_BASE_URL}/clients', methods=['POST'])
def add_client():
    """
    Add a new client with image upload.
    The image is automatically cropped to 450x350 pixels.
    
    Expected form data:
        - image: Image file (required)
        - name: Client name (required)
        - designation: Client designation, e.g., CEO, Web Developer (required)
        - description: Client description/testimonial (required)
    
    Returns:
        JSON: Created client object with ID
    """
    try:
        # Validate image file
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400
        
        file = request.files['image']
        name = request.form.get('name')
        designation = request.form.get('designation')
        description = request.form.get('description')
        
        # Validate required fields
        if file.filename == '' or not name or not designation or not description:
            return jsonify({'error': 'Missing required fields: image, name, designation, and description are required'}), 400
        
        # Validate file type
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type. Allowed types: png, jpg, jpeg, gif, webp'}), 400
        
        # Process and crop the image
        cropped_filename = process_uploaded_image(file, CLIENTS_FOLDER)
        
        # Create client document
        client = {
            'name': name,
            'designation': designation,
            'description': description,
            'image': cropped_filename
        }
        
        # Save to database
        result = clients_collection.insert_one(client)
        client['_id'] = str(result.inserted_id)
        
        return jsonify(client), 201
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Error adding client: {str(e)}'}), 500


@clients_bp.route(f'{API_BASE_URL}/clients/<client_id>', methods=['DELETE'])
def delete_client(client_id):
    """
    Delete a client by ID.
    Also removes the associated image file from the server.
    
    Args:
        client_id (str): MongoDB ObjectId of the client to delete
    
    Returns:
        JSON: Success message or error
    """
    try:
        # Validate ObjectId format
        if not ObjectId.is_valid(client_id):
            return jsonify({'error': 'Invalid client ID format'}), 400
        
        # Find the client
        client = clients_collection.find_one({'_id': ObjectId(client_id)})
        
        if not client:
            return jsonify({'error': 'Client not found'}), 404
        
        # Delete associated image file
        if 'image' in client:
            image_path = os.path.join(CLIENTS_FOLDER, client['image'])
            if os.path.exists(image_path):
                try:
                    os.remove(image_path)
                except OSError as e:
                    # Log error but continue with database deletion
                    print(f'Warning: Could not delete image file: {e}')
        
        # Delete from database
        clients_collection.delete_one({'_id': ObjectId(client_id)})
        
        return jsonify({'message': 'Client deleted successfully'}), 200
        
    except Exception as e:
        return jsonify({'error': f'Error deleting client: {str(e)}'}), 500


@clients_bp.route('/uploads/clients/<filename>')
def client_image(filename):
    """
    Serve client images.
    
    Args:
        filename (str): Name of the image file
    
    Returns:
        File: Image file from the clients upload folder
    """
    return send_from_directory(CLIENTS_FOLDER, filename)

