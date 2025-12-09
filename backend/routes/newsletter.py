"""
Newsletter subscription routes.
Handles newsletter subscription and retrieval of subscribed emails.
"""

from flask import Blueprint, request, jsonify
from database import newsletter_collection
from config import API_BASE_URL

# Create blueprint for newsletter routes
newsletter_bp = Blueprint('newsletter', __name__)


@newsletter_bp.route(f'{API_BASE_URL}/newsletter', methods=['POST'])
def subscribe_newsletter():
    """
    Subscribe an email address to the newsletter.
    Prevents duplicate subscriptions.
    
    Expected JSON data:
        - email: Email address to subscribe (required)
    
    Returns:
        JSON: Subscription confirmation or existing subscription message
    """
    try:
        data = request.json
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        email = data.get('email', '').strip().lower()
        
        # Validate email
        if not email:
            return jsonify({'error': 'Email is required'}), 400
        
        if '@' not in email:
            return jsonify({'error': 'Invalid email format'}), 400
        
        # Check if already subscribed
        existing = newsletter_collection.find_one({'email': email})
        if existing:
            return jsonify({
                'message': 'Email is already subscribed',
                'email': email
            }), 200
        
        # Create new subscription
        subscription = {'email': email}
        result = newsletter_collection.insert_one(subscription)
        subscription['_id'] = str(result.inserted_id)
        
        return jsonify({
            'message': 'Successfully subscribed to newsletter',
            'subscription': subscription
        }), 201
        
    except Exception as e:
        return jsonify({'error': f'Error subscribing to newsletter: {str(e)}'}), 500


@newsletter_bp.route(f'{API_BASE_URL}/newsletter', methods=['GET'])
def get_subscriptions():
    """
    Retrieve all newsletter subscriptions.
    Used by the admin panel to view all subscribed email addresses.
    
    Returns:
        JSON: List of all newsletter subscriptions
    """
    try:
        subscriptions = list(newsletter_collection.find().sort('_id', -1))  # Sort by newest first
        for sub in subscriptions:
            sub['_id'] = str(sub['_id'])
        return jsonify(subscriptions), 200
    except Exception as e:
        return jsonify({'error': f'Error retrieving subscriptions: {str(e)}'}), 500

