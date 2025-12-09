"""
Contact form routes.
Handles submission and retrieval of contact form data.
"""

from flask import Blueprint, request, jsonify
from database import contact_collection
from config import API_BASE_URL

# Create blueprint for contact routes
contacts_bp = Blueprint('contacts', __name__)


@contacts_bp.route(f'{API_BASE_URL}/contact', methods=['POST'])
def submit_contact():
    """
    Submit a contact form.
    
    Expected JSON data:
        - fullName: Full name of the contact (required)
        - email: Email address (required)
        - mobile: Mobile phone number (required)
        - city: City name (required)
    
    Returns:
        JSON: Created contact object with ID
    """
    try:
        data = request.json
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Extract and validate contact information
        contact = {
            'fullName': data.get('fullName', '').strip(),
            'email': data.get('email', '').strip(),
            'mobile': data.get('mobile', '').strip(),
            'city': data.get('city', '').strip()
        }
        
        # Validate required fields
        if not all(contact.values()):
            return jsonify({'error': 'All fields are required: fullName, email, mobile, and city'}), 400
        
        # Basic email validation
        if '@' not in contact['email']:
            return jsonify({'error': 'Invalid email format'}), 400
        
        # Save to database
        result = contact_collection.insert_one(contact)
        contact['_id'] = str(result.inserted_id)
        
        return jsonify({
            'message': 'Contact form submitted successfully',
            'contact': contact
        }), 201
        
    except Exception as e:
        return jsonify({'error': f'Error submitting contact form: {str(e)}'}), 500


@contacts_bp.route(f'{API_BASE_URL}/contact', methods=['GET'])
def get_contacts():
    """
    Retrieve all contact form submissions.
    Used by the admin panel to view all contact form entries.
    
    Returns:
        JSON: List of all contact form submissions
    """
    try:
        contacts = list(contact_collection.find().sort('_id', -1))  # Sort by newest first
        for contact in contacts:
            contact['_id'] = str(contact['_id'])
        return jsonify(contacts), 200
    except Exception as e:
        return jsonify({'error': f'Error retrieving contacts: {str(e)}'}), 500

