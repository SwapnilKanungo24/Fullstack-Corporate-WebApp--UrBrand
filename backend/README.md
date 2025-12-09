# Backend Documentation

## Project Structure

The backend is organized into a modular structure for better maintainability and code organization:

```
backend/
├── app.py                 # Main Flask application entry point
├── config.py             # Configuration settings and constants
├── database.py           # MongoDB connection and collections
├── utils.py              # Utility functions (image processing, file handling)
├── routes/               # API route handlers
│   ├── __init__.py       # Routes package initialization
│   ├── projects.py       # Project management routes
│   ├── clients.py        # Client management routes
│   ├── contacts.py       # Contact form routes
│   └── newsletter.py     # Newsletter subscription routes
└── uploads/              # Uploaded files directory
    ├── projects/         # Project images
    └── clients/          # Client images
```

## Module Descriptions

### `app.py`
Main application file that:
- Initializes the Flask application
- Registers all route blueprints
- Sets up CORS
- Serves frontend static files
- Creates necessary upload directories

### `config.py`
Centralized configuration file containing:
- Flask server settings (host, port, debug mode)
- MongoDB connection settings
- Upload folder paths
- Image processing settings (target size, allowed extensions)
- API base URL

### `database.py`
Database connection module that:
- Establishes MongoDB connection
- Provides access to all collections (projects, clients, contacts, newsletter)
- Exports helper functions for database access

### `utils.py`
Utility functions for:
- File validation (checking allowed extensions)
- Image cropping and resizing
- Secure file path generation
- Image upload processing

### `routes/`
Route handlers organized by resource:

#### `projects.py`
- `GET /api/projects` - Retrieve all projects
- `POST /api/projects` - Add a new project with image
- `DELETE /api/projects/<id>` - Delete a project
- `GET /uploads/projects/<filename>` - Serve project images

#### `clients.py`
- `GET /api/clients` - Retrieve all clients
- `POST /api/clients` - Add a new client with image
- `DELETE /api/clients/<id>` - Delete a client
- `GET /uploads/clients/<filename>` - Serve client images

#### `contacts.py`
- `POST /api/contact` - Submit a contact form
- `GET /api/contact` - Retrieve all contact submissions

#### `newsletter.py`
- `POST /api/newsletter` - Subscribe to newsletter
- `GET /api/newsletter` - Retrieve all subscriptions

## Code Organization Principles

1. **Separation of Concerns**: Each module has a single, well-defined responsibility
2. **DRY (Don't Repeat Yourself)**: Common functionality is extracted to utility functions
3. **Configuration Management**: All settings are centralized in `config.py`
4. **Blueprint Pattern**: Routes are organized using Flask blueprints for modularity
5. **Documentation**: All functions include docstrings explaining their purpose

## Adding New Features

### Adding a New Route Module

1. Create a new file in `routes/` directory (e.g., `routes/blog.py`)
2. Import necessary modules and create a blueprint:
   ```python
   from flask import Blueprint
   from config import API_BASE_URL
   
   blog_bp = Blueprint('blog', __name__)
   ```
3. Define routes using the blueprint
4. Register the blueprint in `app.py`:
   ```python
   from routes.blog import blog_bp
   app.register_blueprint(blog_bp)
   ```

### Adding New Configuration

Add new settings to `config.py` and import them where needed.

### Adding New Utility Functions

Add helper functions to `utils.py` with proper documentation.

## Error Handling

All routes include try-except blocks to handle errors gracefully and return appropriate HTTP status codes:
- `200` - Success
- `201` - Created
- `400` - Bad Request (validation errors)
- `404` - Not Found
- `500` - Internal Server Error

## Image Processing

Images are automatically processed when uploaded:
1. File is validated (type and size)
2. Saved temporarily
3. Cropped to target aspect ratio (centered)
4. Resized to exact dimensions (450x350)
5. Original file is removed
6. Cropped file is saved with "cropped_" prefix

## Database Schema

### Projects Collection
```json
{
  "_id": "ObjectId",
  "name": "string",
  "description": "string",
  "image": "string (filename)"
}
```

### Clients Collection
```json
{
  "_id": "ObjectId",
  "name": "string",
  "designation": "string",
  "description": "string",
  "image": "string (filename)"
}
```

### Contacts Collection
```json
{
  "_id": "ObjectId",
  "fullName": "string",
  "email": "string",
  "mobile": "string",
  "city": "string"
}
```

### Newsletter Collection
```json
{
  "_id": "ObjectId",
  "email": "string"
}
```

## Testing

To test the API endpoints, you can use:
- Postman
- cURL
- Browser (for GET requests)
- Frontend application

Example cURL commands:

```bash
# Get all projects
curl http://localhost:5000/api/projects

# Add a project
curl -X POST http://localhost:5000/api/projects \
  -F "image=@path/to/image.jpg" \
  -F "name=Project Name" \
  -F "description=Project Description"

# Submit contact form
curl -X POST http://localhost:5000/api/contact \
  -H "Content-Type: application/json" \
  -d '{"fullName":"John Doe","email":"john@example.com","mobile":"1234567890","city":"New York"}'
```

## Maintenance

- Keep routes focused on a single resource
- Use utility functions for common operations
- Update documentation when adding new features
- Follow the existing code style and patterns
- Test all endpoints after making changes

