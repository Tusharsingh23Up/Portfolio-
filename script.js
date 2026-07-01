document.addEventListener('DOMContentLoaded', () => {
    // 1. Mobile Navbar Toggle
    const navToggle = document.getElementById('navToggle');
    const navLinks = document.querySelector('.nav-links');
    
    if (navToggle) {
        navToggle.addEventListener('click', () => {
            navLinks.classList.toggle('open');
            // Toggle hamburger icon appearance
            const spans = navToggle.querySelectorAll('span');
            if (navLinks.classList.contains('open')) {
                spans[0].style.transform = 'translateY(7px) rotate(45deg)';
                spans[1].style.opacity = '0';
                spans[2].style.transform = 'translateY(-7px) rotate(-45deg)';
            } else {
                spans[0].style.transform = 'none';
                spans[1].style.opacity = '1';
                spans[2].style.transform = 'none';
            }
        });
    }

    // Close mobile menu on link click
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            if (navLinks.classList.contains('open')) {
                navToggle.click();
            }
        });
    });

    // 2. Navbar Solidify on Scroll
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // 3. Highlight Active Nav Link on Scroll
    const sections = document.querySelectorAll('section');
    const navItems = document.querySelectorAll('.nav-link');

    window.addEventListener('scroll', () => {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (pageYOffset >= (sectionTop - 150)) {
                current = section.getAttribute('id');
            }
        });

        navItems.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    });

    // 4. Intersection Observer for Scroll Animations
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const scrollObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                
                // If it's the achievements section, trigger counters
                if (entry.target.classList.contains('achievements-section')) {
                    startCounters();
                }
                
                // If it's a skill category, trigger skill bar animation
                if (entry.target.classList.contains('skill-category')) {
                    animateSkills(entry.target);
                }
                
                // Optional: stop observing once animated
                // observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe various elements
    document.querySelectorAll('.animate-on-scroll, .animate-slide-left, .animate-slide-right, .animate-slide-left-exp, .animate-drop-in, .animate-project-in, .animate-skill-card, .animate-cert-cascade, .animate-ach-zoom, .animate-contact-left, .animate-contact-right').forEach(el => {
        scrollObserver.observe(el);
    });

    // Randomize rotation slightly for cert cascading
    document.querySelectorAll('.animate-cert-cascade').forEach(card => {
        const randomRot = (Math.random() * 4 - 2).toFixed(1); // -2deg to 2deg
        card.style.setProperty('--cert-rotation', `${randomRot}deg`);
    });

    // Observe section itself to trigger counters
    const achSection = document.querySelector('.achievements-section');
    if (achSection) {
        scrollObserver.observe(achSection);
    }

    // 5. Number Counters Animation
    let countersStarted = false;
    function startCounters() {
        if (countersStarted) return;
        countersStarted = true;

        const counters = document.querySelectorAll('.stat-number');
        const speed = 2000; // 2 seconds total

        counters.forEach(counter => {
            const target = +counter.getAttribute('data-target');
            const suffix = counter.getAttribute('data-suffix') || '';
            const increment = target / (speed / 16); // 16ms per frame (60fps)

            let current = 0;
            const updateCount = () => {
                current += increment;
                if (current < target) {
                    counter.innerText = Math.ceil(current) + suffix;
                    requestAnimationFrame(updateCount);
                } else {
                    counter.innerText = target + suffix;
                }
            };
            updateCount();
        });
    }

    // 5b. Skills Animation
    function animateSkills(card) {
        if (card.classList.contains('skills-animated')) return;
        card.classList.add('skills-animated');

        const fills = card.querySelectorAll('.skill-bar-fill');
        const pcts = card.querySelectorAll('.skill-pct');

        fills.forEach(fill => {
            const width = fill.getAttribute('data-width');
            fill.style.width = width + '%';
        });

        pcts.forEach(pct => {
            const target = +pct.getAttribute('data-pct');
            const speed = 1500; // 1.5s total
            const increment = target / (speed / 16);
            let current = 0;

            const updatePct = () => {
                current += increment;
                if (current < target) {
                    pct.innerText = Math.ceil(current) + '%';
                    requestAnimationFrame(updatePct);
                } else {
                    pct.innerText = target + '%';
                }
            };
            updatePct();
        });
    }

    // 6. Form Submission Logic
    const contactForm = document.getElementById('contactForm');
    const sendBtn = document.getElementById('sendBtn');
    
    if (contactForm && sendBtn) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault(); // Prevent page reload
            
            const btnText = sendBtn.querySelector('.btn-text');
            const originalText = btnText.innerText;
            const icon = sendBtn.querySelector('svg');
            
            // Visual feedback: Sending...
            btnText.innerText = 'Sending...';
            sendBtn.style.opacity = '0.8';
            sendBtn.style.pointerEvents = 'none';

            // Simulate network request
            setTimeout(() => {
                // Success feedback
                btnText.innerText = 'Message Sent!';
                if (icon) icon.style.display = 'none';
                sendBtn.style.background = '#22c55e'; // Green success color
                sendBtn.style.opacity = '1';

                // Reset form
                contactForm.reset();

                // Revert button after 3 seconds
                setTimeout(() => {
                    btnText.innerText = originalText;
                    if (icon) icon.style.display = 'block';
                    sendBtn.style.background = ''; // Revert to original CSS gradient
                    sendBtn.style.pointerEvents = 'auto';
                }, 3000);
            }, 1500);
        });
    }
});
