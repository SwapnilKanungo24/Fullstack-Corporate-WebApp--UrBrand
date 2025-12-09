# 🌐 Fullstack Web Application – Portfolio, Projects & Admin CMS  
*A Production-ready Full-Stack Application featuring a modern landing page, modular API architecture, secure admin CMS, and MongoDB persistence.*

---

## 📘 Overview  
This project is a **complete fullstack web application** built using:

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Flask (Python)  
- **Database:** MongoDB Atlas  
- **Admin Panel:** JWT-secured CMS  
- **Image Processing:** Pillow  
- **Deployment:** Render (Backend) + Vercel/Netlify (Frontend)

It includes a public landing page and a fully-functional Admin Content Management System (CMS) to manage **projects**, **testimonials**, **contacts**, and **newsletter subscribers**.

---

## ✨ Features

### 🌍 Public Website
- Responsive landing page  
- Dynamic projects section (fetched from API)  
- Client testimonials  
- Newsletter subscription  
- Contact form  
- Smooth UI/UX with modern styling  

### 🔐 Admin Panel (CMS)
- Secure JWT authentication  
- Add / Edit / Delete Projects  
- Add / Edit / Delete Client Testimonials  
- Manage contacts & subscribers  
- Image upload with auto-cropping  
- Fully modular and scalable codebase  

### ⚙️ Backend Features
- Built with Flask 3.x  
- Modular route architecture  
- MongoDB Atlas integration  
- Secure password hashing & token-based auth  
- CORS-enabled for multi-origin deployments  
- Image resizing, cropping & compression  

---

## 🧱 Tech Stack

### Frontend
- HTML5  
- CSS3  
- JavaScript (ES6)

### Backend
- Python 3.10+  
- Flask  
- PyMongo  
- Flask-CORS  
- PyJWT  
- Pillow  

### Database
- MongoDB Atlas  

### Deployment
- Render (Backend)  
- Vercel / Netlify (Frontend)

---

## 📂 Project Structure

```bash
fullstack-project/
├── backend/
│   ├── app.py                 # Application entry point
│   ├── config.py              # Environment configurations
│   ├── database.py            # MongoDB connection
│   ├── utils.py               # Image processing, helpers
│   ├── routes/                # Modular API routes
│   │   ├── __init__.py
│   │   ├── projects.py
│   │   ├── clients.py
│   │   ├── contacts.py
│   │   └── newsletter.py
│   ├── uploads/               # Runtime media storage
│   │   ├── projects/
│   │   └── clients/
│   └── README.md
│
├── frontend/
│   ├── index.html             # Landing page
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── admin/
│       ├── index.html         # Admin CMS
│       ├── css/admin.css
│       └── js/admin.js
│
├── requirements.txt           # Python dependencies
└── README.md                  # (This file)
```
### API Overview
Public Endpoints
Method	Route	Description
GET	/api/projects	Fetch projects
GET	/api/clients	Fetch testimonials
POST	/api/contact	Submit contact form
POST	/api/subscribe	Newsletter subscription
Admin Endpoints (JWT Required)
Method	Route	Description
POST	/api/admin/login	Admin login
POST	/api/admin/projects	Create project
PUT	/api/admin/projects/:id	Update project
DELETE	/api/admin/projects/:id	Delete project
POST	/api/admin/clients	Create client testimonial
...	...	More in /routes/ folder
