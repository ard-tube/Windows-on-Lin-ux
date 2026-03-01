// script.js

// Functionality for website navigation
function navigateTo(section) {
    const sections = document.querySelectorAll('.section');
    sections.forEach(sec => {
        sec.style.display = 'none';
    });
    document.querySelector(`#${section}`).style.display = 'block';
}

// Event listeners for navigation
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const targetSection = e.target.getAttribute('data-target');
        navigateTo(targetSection);
    });
});

// Initial setup
navigateTo('home'); // Show home section by default

// Add more interactivity functionality as needed.