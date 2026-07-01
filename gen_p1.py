import sys

# ---- SECTION 1: HEAD + NAV + HERO ----
s1 = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>Tushar Singh | Data Analyst &amp; Business Analyst Portfolio</title>
  <meta name="description" content="Tushar Singh - Data Analyst, Business Analyst, Power BI Developer, SQL and Python Analyst. Portfolio showcasing projects, skills and certifications."/>
  <meta property="og:title" content="Tushar Singh | Data Analyst Portfolio"/>
  <meta property="og:description" content="Turning raw datasets into practical business insights."/>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet"/>
  <link rel="stylesheet" href="style.css"/>
</head>
<body>

<nav class="navbar" id="navbar">
  <div class="nav-container">
    <a href="#hero" class="nav-logo">
      <span class="logo-initials">TS</span>
      <span class="logo-name">Tushar Singh</span>
    </a>
    <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation">
      <span></span><span></span><span></span>
    </button>
    <ul class="nav-links" id="navLinks">
      <li><a href="#hero" class="nav-link">Home</a></li>
      <li><a href="#about" class="nav-link">About</a></li>
      <li><a href="#experience" class="nav-link">Experience</a></li>
      <li><a href="#education" class="nav-link">Education</a></li>
      <li><a href="#projects" class="nav-link">Projects</a></li>
      <li><a href="#skills" class="nav-link">Skills</a></li>
      <li><a href="#certifications" class="nav-link">Certifications</a></li>
      <li><a href="#achievements" class="nav-link">Achievements</a></li>
      <li><a href="#contact" class="nav-link nav-cta">Contact</a></li>
    </ul>
  </div>
</nav>

<section class="hero" id="hero">
  <div class="hero-particles" id="heroParticles"></div>
  <div class="hero-container">
    <div class="hero-content">
      <div class="hero-badge animate-fade-in-up">
        <span class="hero-logo-initials">TS</span>
        <span>Portfolio</span>
      </div>
      <h1 class="hero-name animate-fade-in-up">Tushar Singh</h1>
      <div class="hero-designations animate-fade-in-up">
        <span class="designation-item">Data Analyst</span>
        <span class="designation-sep">|</span>
        <span class="designation-item">Business Analyst</span>
        <span class="designation-sep">|</span>
        <span class="designation-item">Power BI Developer</span>
        <span class="designation-sep">|</span>
        <span class="designation-item">SQL &amp; Python Analyst</span>
      </div>
      <p class="hero-intro animate-fade-in-up">I am Tushar Singh, a final-year B.Tech student in Data Analysis with hands-on experience in SQL, Python, Excel, Power BI, dashboarding, and business reporting. I have completed a remote Data Analyst internship focused on credit-risk modeling, KPI reporting, portfolio analytics, and data-driven decision-making. My work combines analytical thinking, financial domain understanding, and clear data storytelling to turn raw datasets into practical business insights. I enjoy building dashboards, cleaning complex data, and using models to support smarter business decisions. Explore my work to see how I use analytics to solve real-world business problems.</p>
      <div class="hero-cta animate-slide-up">
        <a href="#about" class="btn btn-primary">Learn More About Me</a>
        <a href="#contact" class="btn btn-outline">Get In Touch</a>
      </div>
      <div class="hero-socials">
        <a href="https://github.com/Tusharsingh23Up" target="_blank" rel="noopener" class="social-icon animate-pop" aria-label="GitHub">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
        </a>
        <a href="https://www.linkedin.com/in/tusharsingh-analytics" target="_blank" rel="noopener" class="social-icon animate-pop" aria-label="LinkedIn">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
        </a>
        <a href="mailto:ADD_YOUR_EMAIL" class="social-icon animate-pop" aria-label="Email">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
        </a>
      </div>
    </div>
  </div>
  <div class="hero-scroll-indicator"><div class="scroll-dot"></div></div>
</section>
"""

with open("p1.html","w",encoding="utf-8") as f:
    f.write(s1)
print("p1 done",len(s1))
