"""
Database connection and collection management.
Handles MongoDB connection and provides access to collections.
"""

from pymongo import MongoClient
from config import MONGODB_URI, DATABASE_NAME

# MongoDB connection
client = MongoClient(MONGODB_URI)
db = client[DATABASE_NAME]

# Collections
projects_collection = db['projects']
clients_collection = db['clients']
contact_collection = db['contacts']
newsletter_collection = db['newsletter']


def get_database():
    """
    Get the database instance.
    
    Returns:
        Database: MongoDB database instance
    """
    return db


def get_collections():
    """
    Get all collection references.
    
    Returns:
        dict: Dictionary containing all collection references
    """
    return {
        'projects': projects_collection,
        'clients': clients_collection,
        'contacts': contact_collection,
        'newsletter': newsletter_collection
    }

