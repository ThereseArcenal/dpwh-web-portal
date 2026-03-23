// Initialize AOS
AOS.init({
    duration: 1000,
    once: true,
    offset: 100
});

// Navbar scroll effect
window.addEventListener('scroll', function() {
    const nav = document.getElementById('mainNav');
    if (window.scrollY > 50) {
        nav.classList.add('navbar-scrolled');
    } else {
        nav.classList.remove('navbar-scrolled');
    }
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
            
            // Close mobile menu after clicking a link (for mobile)
            const navbarCollapse = document.getElementById('navbarNav');
            if (navbarCollapse.classList.contains('show')) {
                navbarCollapse.classList.remove('show');
                const toggler = document.querySelector('.navbar-toggler');
                if (toggler) {
                    toggler.setAttribute('aria-expanded', 'false');
                }
            }
        }
    });
});

// Active nav link on scroll
const sections = document.querySelectorAll('section[id]');
window.addEventListener('scroll', () => {
    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (scrollY >= sectionTop - 200) {
            current = section.getAttribute('id');
        }
    });
    
    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
});

// Close mobile menu when window resizes to desktop
window.addEventListener('resize', function() {
    if (window.innerWidth > 991) {
        const navbarCollapse = document.getElementById('navbarNav');
        if (navbarCollapse.classList.contains('show')) {
            navbarCollapse.classList.remove('show');
            const toggler = document.querySelector('.navbar-toggler');
            if (toggler) {
                toggler.setAttribute('aria-expanded', 'false');
            }
        }
    }
});

// ===== ORGANIZATIONAL CHART MODAL - FULLY FUNCTIONAL =====
function openOrgChartModal() {
    const modal = document.getElementById('orgChartModal');
    if (modal) {
        modal.style.display = 'flex';
        document.body.style.overflow = 'hidden';
    }
}

function closeOrgChartModal() {
    const modal = document.getElementById('orgChartModal');
    if (modal) {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
    }
}

// Close modal with ESC key
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        const modal = document.getElementById('orgChartModal');
        if (modal && modal.style.display === 'flex') {
            closeOrgChartModal();
        }
    }
});
// ===== ZOOM FUNCTION FOR ORGANIZATIONAL CHART =====
let isZoomed = false;

function toggleZoom() {
    const img = document.getElementById('orgChartImage');
    if (img) {
        if (isZoomed) {
            img.style.maxWidth = '100%';
            img.style.maxHeight = '85vh';
            img.style.cursor = 'zoom-in';
            isZoomed = false;
        } else {
            img.style.maxWidth = '180%';
            img.style.maxHeight = '180%';
            img.style.cursor = 'zoom-out';
            isZoomed = true;
        }
    }
}