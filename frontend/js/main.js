const API_BASE_URL = 'http://localhost:5000/api';

// Load projects on page load
document.addEventListener('DOMContentLoaded', () => {
    loadProjects();
    loadClients();
    setupForms();
});

// Load projects from backend
async function loadProjects() {
    try {
        const response = await fetch(`${API_BASE_URL}/projects`);
        const projects = await response.json();
        
        const projectsGrid = document.getElementById('projectsGrid');
        projectsGrid.innerHTML = '';
        
        if (projects.length === 0) {
            projectsGrid.innerHTML = '<p style="text-align: center; grid-column: 1/-1;">No projects available yet.</p>';
            return;
        }
        
        projects.forEach(project => {
            const projectCard = document.createElement('div');
            projectCard.className = 'project-card';
            projectCard.innerHTML = `
                <img src="http://localhost:5000/uploads/projects/${project.image}" alt="${project.name}" class="project-image" onerror="this.src='https://via.placeholder.com/450x350?text=Project+Image'">
                <div class="project-info">
                    <h3>${project.name}</h3>
                    <p>${project.description}</p>
                    <button class="read-more-btn">Read More</button>
                </div>
            `;
            projectsGrid.appendChild(projectCard);
        });
    } catch (error) {
        console.error('Error loading projects:', error);
        document.getElementById('projectsGrid').innerHTML = '<p style="text-align: center; grid-column: 1/-1; color: red;">Error loading projects. Please try again later.</p>';
    }
}

// Load clients from backend
async function loadClients() {
    try {
        const response = await fetch(`${API_BASE_URL}/clients`);
        const clients = await response.json();
        
        const clientsGrid = document.getElementById('clientsGrid');
        clientsGrid.innerHTML = '';
        
        if (clients.length === 0) {
            clientsGrid.innerHTML = '<p style="text-align: center; grid-column: 1/-1;">No clients available yet.</p>';
            return;
        }
        
        clients.forEach(client => {
            const clientCard = document.createElement('div');
            clientCard.className = 'client-card';
            clientCard.innerHTML = `
                <img src="http://localhost:5000/uploads/clients/${client.image}" alt="${client.name}" class="client-image" onerror="this.src='https://via.placeholder.com/120x120?text=Client'">
                <h3>${client.name}</h3>
                <p class="client-designation">${client.designation}</p>
                <p>${client.description}</p>
            `;
            clientsGrid.appendChild(clientCard);
        });
    } catch (error) {
        console.error('Error loading clients:', error);
        document.getElementById('clientsGrid').innerHTML = '<p style="text-align: center; grid-column: 1/-1; color: red;">Error loading clients. Please try again later.</p>';
    }
}

// Setup form handlers
function setupForms() {
    // Consultation form (hero section)
    const consultationForm = document.getElementById('consultationForm');
    if (consultationForm) {
        consultationForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(consultationForm);
            // This form uses the same contact endpoint
            const data = {
                fullName: consultationForm.querySelector('input[type="text"]').value,
                email: consultationForm.querySelector('input[type="email"]').value,
                mobile: consultationForm.querySelector('input[type="tel"]').value,
                city: 'N/A'
            };
            
            try {
                const response = await fetch(`${API_BASE_URL}/contact`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                });
                
                if (response.ok) {
                    showMessage('Thank you! We will contact you soon.', 'success');
                    consultationForm.reset();
                } else {
                    showMessage('Error submitting form. Please try again.', 'error');
                }
            } catch (error) {
                showMessage('Error submitting form. Please try again.', 'error');
            }
        });
    }
    
    // Contact form
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const data = {
                fullName: document.getElementById('fullName').value,
                email: document.getElementById('email').value,
                mobile: document.getElementById('mobile').value,
                city: document.getElementById('city').value
            };
            
            try {
                const response = await fetch(`${API_BASE_URL}/contact`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                });
                
                if (response.ok) {
                    showMessage('Thank you for contacting us! We will get back to you soon.', 'success');
                    contactForm.reset();
                } else {
                    showMessage('Error submitting form. Please try again.', 'error');
                }
            } catch (error) {
                showMessage('Error submitting form. Please try again.', 'error');
            }
        });
    }
    
    // Newsletter form
    const newsletterForm = document.getElementById('newsletterForm');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const email = document.getElementById('newsletterEmail').value;
            
            try {
                const response = await fetch(`${API_BASE_URL}/newsletter`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ email })
                });
                
                if (response.ok) {
                    showMessage('Thank you for subscribing!', 'success');
                    newsletterForm.reset();
                } else {
                    showMessage('Error subscribing. Please try again.', 'error');
                }
            } catch (error) {
                showMessage('Error subscribing. Please try again.', 'error');
            }
        });
    }
}

// Show message to user
function showMessage(message, type) {
    // Remove existing messages
    const existingMessages = document.querySelectorAll('.message');
    existingMessages.forEach(msg => msg.remove());
    
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${type}`;
    messageDiv.textContent = message;
    
    // Insert at the top of the body
    document.body.insertBefore(messageDiv, document.body.firstChild);
    
    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
    
    // Remove after 5 seconds
    setTimeout(() => {
        messageDiv.remove();
    }, 5000);
}

