# Full-Stack Project Management Application

A professional full-stack web application with a landing page and admin panel for managing projects, clients, contact forms, and newsletter subscriptions.

## Features

### Landing Page
- **Hero Section** with consultation contact form
- **Why Choose Us** section with features grid
- **Our Projects** section - dynamically displays projects from backend
- **Happy Clients** section - displays client testimonials
- **Contact Form** - Full Name, Email, Mobile, City
- **Newsletter Subscription** - Email subscription widget

### Admin Panel
- **Project Management** - Add/Delete projects with image upload and cropping (450x350)
- **Client Management** - Add/Delete clients with image upload and cropping (450x350)
- **Contact Form Management** - View all contact form submissions
- **Newsletter Management** - View all subscribed email addresses

## Technology Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **Database**: MongoDB
- **Image Processing**: Pillow (PIL)

## Prerequisites

- Python 3.7 or higher
- MongoDB installed and running
- pip (Python package manager)

## Installation

1. **Clone or navigate to the project directory**

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start MongoDB**
   - Make sure MongoDB is running on `localhost:27017`
   - If MongoDB is installed as a service, it should start automatically
   - For manual start: `mongod` (on Linux/Mac) or start MongoDB service (on Windows)

4. **Run the Flask application**
   ```bash
   cd backend
   python app.py
   ```

5. **Open the application**
   - Landing Page: Open `frontend/index.html` in your browser or access via Flask server
   - Admin Panel: Navigate to `frontend/admin/index.html` or use the "Admin" link in navigation

## Project Structure

```
fullstack project/
├── backend/
│   ├── app.py                 # Main Flask application entry point
│   ├── config.py             # Configuration settings
│   ├── database.py           # MongoDB connection and collections
│   ├── utils.py              # Utility functions (image processing, etc.)
│   ├── routes/               # API route handlers (modular structure)
│   │   ├── __init__.py
│   │   ├── projects.py       # Project management routes
│   │   ├── clients.py        # Client management routes
│   │   ├── contacts.py       # Contact form routes
│   │   └── newsletter.py     # Newsletter routes
│   ├── README.md             # Backend documentation
│   └── uploads/              # Uploaded images
│       ├── projects/          # Project images
│       └── clients/           # Client images
├── frontend/
│   ├── index.html            # Landing page
│   ├── css/
│   │   └── style.css         # Landing page styles
│   ├── js/
│   │   └── main.js           # Landing page JavaScript
│   └── admin/
│       ├── index.html        # Admin panel
│       ├── css/
│       │   └── admin.css     # Admin panel styles
│       └── js/
│           └── admin.js      # Admin panel JavaScript
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

### Backend Architecture

The backend follows a **modular architecture** for clean code organization:

- **`config.py`**: Centralized configuration (database, uploads, image settings)
- **`database.py`**: MongoDB connection and collection management
- **`utils.py`**: Reusable utility functions (image cropping, file validation)
- **`routes/`**: Organized route handlers using Flask blueprints
  - Each resource (projects, clients, contacts, newsletter) has its own route file
  - Better separation of concerns and maintainability
- **`app.py`**: Main application file that ties everything together

This structure makes the code:
- ✅ Easier to understand and navigate
- ✅ More maintainable and scalable
- ✅ Better organized with clear responsibilities
- ✅ Well-documented with docstrings

## API Endpoints

### Projects
- `GET /api/projects` - Get all projects
- `POST /api/projects` - Add a new project (multipart/form-data)
- `DELETE /api/projects/<id>` - Delete a project

### Clients
- `GET /api/clients` - Get all clients
- `POST /api/clients` - Add a new client (multipart/form-data)
- `DELETE /api/clients/<id>` - Delete a client

### Contact Forms
- `GET /api/contact` - Get all contact form submissions
- `POST /api/contact` - Submit a contact form (JSON)

### Newsletter
- `GET /api/newsletter` - Get all newsletter subscriptions
- `POST /api/newsletter` - Subscribe to newsletter (JSON)

## Image Cropping

When uploading images through the admin panel:
- Images are automatically cropped to 450x350 pixels (width x height)
- The cropping maintains the target aspect ratio (450:350) and centers the image
- Images are cropped from the center, then resized to exactly 450x350 pixels
- Original images are replaced with cropped versions
- Works with any input image size (e.g., 700x700 will be cropped and resized to 450x350)

## Usage

### Adding a Project
1. Go to Admin Panel → Projects
2. Click "+ Add Project"
3. Upload an image (will be cropped to 450x350)
4. Enter project name and description
5. Click "Add Project"

### Adding a Client
1. Go to Admin Panel → Clients
2. Click "+ Add Client"
3. Upload an image (will be cropped to 450x350)
4. Enter client name, designation, and description
5. Click "Add Client"

### Viewing Contact Forms
1. Go to Admin Panel → Contact Forms
2. View all submitted contact forms with details

### Viewing Newsletter Subscriptions
1. Go to Admin Panel → Newsletter
2. View all subscribed email addresses

## Configuration

### MongoDB Connection
The default MongoDB connection is set to `mongodb://localhost:27017/`. To change this, modify the connection string in `backend/app.py`:

```python
client = MongoClient('mongodb://localhost:27017/')
```

### API Base URL
The frontend JavaScript uses `http://localhost:5000/api` as the base URL. If you change the Flask port, update the `API_BASE_URL` in:
- `frontend/js/main.js`
- `frontend/admin/js/admin.js`

## Troubleshooting

### MongoDB Connection Error
- Ensure MongoDB is running: `mongod` or check MongoDB service
- Verify MongoDB is listening on port 27017
- Check MongoDB connection string in `app.py`

### Image Upload Issues
- Ensure `uploads/projects` and `uploads/clients` directories exist
- Check file permissions for upload directories
- Verify image file format (png, jpg, jpeg, gif, webp)

### CORS Issues
- Flask-CORS is configured to allow all origins
- If issues persist, check browser console for CORS errors

## Development

### Running in Development Mode
The Flask app runs in debug mode by default. For production:
- Set `debug=False` in `app.py`
- Use a production WSGI server (e.g., Gunicorn)
- Configure proper CORS settings

## License

This project is open source and available for use.

## Support

For issues or questions, please check the code comments or refer to the Flask and MongoDB documentation.

