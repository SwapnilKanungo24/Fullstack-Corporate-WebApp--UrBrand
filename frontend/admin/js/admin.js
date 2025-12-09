const API_BASE_URL = 'http://localhost:5000/api';

// Initialize admin panel
document.addEventListener('DOMContentLoaded', () => {
    setupNavigation();
    loadAllData();
    setupForms();
});

// Setup navigation
function setupNavigation() {
    const navItems = document.querySelectorAll('.nav-item[data-section]');
    navItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            const section = item.getAttribute('data-section');
            
            // Update active nav item
            navItems.forEach(nav => nav.classList.remove('active'));
            item.classList.add('active');
            
            // Show corresponding section
            document.querySelectorAll('.content-section').forEach(sec => {
                sec.classList.remove('active');
            });
            document.getElementById(`${section}-section`).classList.add('active');
            
            // Load data for the section
            if (section === 'projects') {
                loadProjects();
            } else if (section === 'contacts') {
                loadContacts();
            } else if (section === 'newsletter') {
                loadNewsletter();
            } else if (section === 'clients') {
                loadClients();
            }
        });
    });
}

// Load all data on page load
function loadAllData() {
    loadProjects();
    loadClients();
    loadContacts();
    loadNewsletter();
}

// Load projects
async function loadProjects() {
    try {
        const response = await fetch(`${API_BASE_URL}/projects`);
        const projects = await response.json();
        
        const projectsList = document.getElementById('projectsList');
        projectsList.innerHTML = '';
        
        if (projects.length === 0) {
            projectsList.innerHTML = '<div class="empty-state"><p>No projects yet. Add your first project!</p></div>';
            return;
        }
        
        projects.forEach(project => {
            const projectItem = document.createElement('div');
            projectItem.className = 'project-item';
            projectItem.innerHTML = `
                <img src="http://localhost:5000/uploads/projects/${project.image}" alt="${project.name}" onerror="this.src='https://via.placeholder.com/450x350?text=Project'">
                <div class="project-item-content">
                    <h3>${project.name}</h3>
                    <p>${project.description}</p>
                    <div class="item-actions">
                        <button class="btn btn-danger" onclick="deleteProject('${project._id}')">Delete</button>
                    </div>
                </div>
            `;
            projectsList.appendChild(projectItem);
        });
    } catch (error) {
        console.error('Error loading projects:', error);
        showMessage('Error loading projects', 'error');
    }
}

// Load clients
async function loadClients() {
    try {
        const response = await fetch(`${API_BASE_URL}/clients`);
        const clients = await response.json();
        
        const clientsList = document.getElementById('clientsList');
        clientsList.innerHTML = '';
        
        if (clients.length === 0) {
            clientsList.innerHTML = '<div class="empty-state"><p>No clients yet. Add your first client!</p></div>';
            return;
        }
        
        clients.forEach(client => {
            const clientItem = document.createElement('div');
            clientItem.className = 'client-item';
            clientItem.innerHTML = `
                <img src="http://localhost:5000/uploads/clients/${client.image}" alt="${client.name}" onerror="this.src='https://via.placeholder.com/450x350?text=Client'">
                <div class="client-item-content">
                    <h3>${client.name}</h3>
                    <p class="designation">${client.designation}</p>
                    <p>${client.description}</p>
                    <div class="item-actions">
                        <button class="btn btn-danger" onclick="deleteClient('${client._id}')">Delete</button>
                    </div>
                </div>
            `;
            clientsList.appendChild(clientItem);
        });
    } catch (error) {
        console.error('Error loading clients:', error);
        showMessage('Error loading clients', 'error');
    }
}

// Load contacts
async function loadContacts() {
    try {
        const response = await fetch(`${API_BASE_URL}/contact`);
        const contacts = await response.json();
        
        const tableBody = document.getElementById('contactsTableBody');
        tableBody.innerHTML = '';
        
        if (contacts.length === 0) {
            tableBody.innerHTML = '<tr><td colspan="5" style="text-align: center; padding: 2rem;">No contact submissions yet.</td></tr>';
            return;
        }
        
        contacts.forEach(contact => {
            const row = document.createElement('tr');
            const date = new Date(contact._id ? new Date(parseInt(contact._id.substring(0, 8), 16) * 1000) : Date.now()).toLocaleDateString();
            row.innerHTML = `
                <td>${contact.fullName || 'N/A'}</td>
                <td>${contact.email || 'N/A'}</td>
                <td>${contact.mobile || 'N/A'}</td>
                <td>${contact.city || 'N/A'}</td>
                <td>${date}</td>
            `;
            tableBody.appendChild(row);
        });
    } catch (error) {
        console.error('Error loading contacts:', error);
        showMessage('Error loading contacts', 'error');
    }
}

// Load newsletter subscriptions
async function loadNewsletter() {
    try {
        const response = await fetch(`${API_BASE_URL}/newsletter`);
        const subscriptions = await response.json();
        
        const tableBody = document.getElementById('newsletterTableBody');
        tableBody.innerHTML = '';
        
        if (subscriptions.length === 0) {
            tableBody.innerHTML = '<tr><td colspan="2" style="text-align: center; padding: 2rem;">No newsletter subscriptions yet.</td></tr>';
            return;
        }
        
        subscriptions.forEach(sub => {
            const row = document.createElement('tr');
            const date = new Date(sub._id ? new Date(parseInt(sub._id.substring(0, 8), 16) * 1000) : Date.now()).toLocaleDateString();
            row.innerHTML = `
                <td>${sub.email}</td>
                <td>${date}</td>
            `;
            tableBody.appendChild(row);
        });
    } catch (error) {
        console.error('Error loading newsletter:', error);
        showMessage('Error loading newsletter subscriptions', 'error');
    }
}

// Setup forms
function setupForms() {
    // Add project form
    const addProjectForm = document.getElementById('addProjectForm');
    addProjectForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const formData = new FormData();
        const imageFile = document.getElementById('projectImage').files[0];
        const name = document.getElementById('projectName').value;
        const description = document.getElementById('projectDescription').value;
        
        if (!imageFile || !name || !description) {
            showMessage('Please fill all fields', 'error');
            return;
        }
        
        formData.append('image', imageFile);
        formData.append('name', name);
        formData.append('description', description);
        
        try {
            const response = await fetch(`${API_BASE_URL}/projects`, {
                method: 'POST',
                body: formData
            });
            
            if (response.ok) {
                showMessage('Project added successfully!', 'success');
                closeModal('projectModal');
                addProjectForm.reset();
                loadProjects();
            } else {
                const error = await response.json();
                showMessage(error.error || 'Error adding project', 'error');
            }
        } catch (error) {
            showMessage('Error adding project', 'error');
        }
    });
    
    // Add client form
    const addClientForm = document.getElementById('addClientForm');
    addClientForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const formData = new FormData();
        const imageFile = document.getElementById('clientImage').files[0];
        const name = document.getElementById('clientName').value;
        const designation = document.getElementById('clientDesignation').value;
        const description = document.getElementById('clientDescription').value;
        
        if (!imageFile || !name || !designation || !description) {
            showMessage('Please fill all fields', 'error');
            return;
        }
        
        formData.append('image', imageFile);
        formData.append('name', name);
        formData.append('designation', designation);
        formData.append('description', description);
        
        try {
            const response = await fetch(`${API_BASE_URL}/clients`, {
                method: 'POST',
                body: formData
            });
            
            if (response.ok) {
                showMessage('Client added successfully!', 'success');
                closeModal('clientModal');
                addClientForm.reset();
                loadClients();
            } else {
                const error = await response.json();
                showMessage(error.error || 'Error adding client', 'error');
            }
        } catch (error) {
            showMessage('Error adding client', 'error');
        }
    });
}

// Delete project
async function deleteProject(projectId) {
    if (!confirm('Are you sure you want to delete this project?')) {
        return;
    }
    
    try {
        const response = await fetch(`${API_BASE_URL}/projects/${projectId}`, {
            method: 'DELETE'
        });
        
        if (response.ok) {
            showMessage('Project deleted successfully!', 'success');
            loadProjects();
        } else {
            showMessage('Error deleting project', 'error');
        }
    } catch (error) {
        showMessage('Error deleting project', 'error');
    }
}

// Delete client
async function deleteClient(clientId) {
    if (!confirm('Are you sure you want to delete this client?')) {
        return;
    }
    
    try {
        const response = await fetch(`${API_BASE_URL}/clients/${clientId}`, {
            method: 'DELETE'
        });
        
        if (response.ok) {
            showMessage('Client deleted successfully!', 'success');
            loadClients();
        } else {
            showMessage('Error deleting client', 'error');
        }
    } catch (error) {
        showMessage('Error deleting client', 'error');
    }
}

// Modal functions
function showAddProjectModal() {
    document.getElementById('projectModal').classList.add('active');
}

function showAddClientModal() {
    document.getElementById('clientModal').classList.add('active');
}

function closeModal(modalId) {
    document.getElementById(modalId).classList.remove('active');
}

// Close modal when clicking outside
window.onclick = function(event) {
    const modals = document.querySelectorAll('.modal');
    modals.forEach(modal => {
        if (event.target === modal) {
            modal.classList.remove('active');
        }
    });
}

// Show message
function showMessage(message, type) {
    // Remove existing messages
    const existingMessages = document.querySelectorAll('.message');
    existingMessages.forEach(msg => msg.remove());
    
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${type}`;
    messageDiv.textContent = message;
    
    // Insert at the top of main content
    const mainContent = document.querySelector('.main-content');
    mainContent.insertBefore(messageDiv, mainContent.firstChild);
    
    // Remove after 5 seconds
    setTimeout(() => {
        messageDiv.remove();
    }, 5000);
}

