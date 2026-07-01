s6 = r"""
<section class="section contact-section" id="contact">
  <div class="section-container">
    <div class="section-header animate-on-scroll">
      <span class="section-tag">Get In Touch</span>
      <h2 class="section-title">Let&rsquo;s Turn Data Into Decisions</h2>
      <div class="section-line"></div>
    </div>
    <div class="contact-grid">
      <div class="contact-form-card animate-contact-left">
        <h3 class="contact-form-title">Send Me a Message</h3>
        <form class="contact-form" id="contactForm">
          <div class="form-field">
            <input type="text" id="formName" name="name" required autocomplete="off" placeholder=" "/>
            <label for="formName" class="float-label">Full Name</label>
            <div class="field-underline"></div>
          </div>
          <div class="form-field">
            <input type="email" id="formEmail" name="email" required autocomplete="off" placeholder=" "/>
            <label for="formEmail" class="float-label">Email Address</label>
            <div class="field-underline"></div>
          </div>
          <div class="form-field">
            <input type="text" id="formSubject" name="subject" required autocomplete="off" placeholder=" "/>
            <label for="formSubject" class="float-label">Subject</label>
            <div class="field-underline"></div>
          </div>
          <div class="form-field form-field-textarea">
            <textarea id="formMessage" name="message" required rows="5" placeholder=" "></textarea>
            <label for="formMessage" class="float-label">Message</label>
            <div class="field-underline"></div>
          </div>
          <button type="submit" class="send-btn" id="sendBtn">
            <span class="btn-text">Send Message</span>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
            <div class="btn-shimmer"></div>
          </button>
        </form>
      </div>
      <div class="contact-info-panel animate-contact-right">
        <h3 class="contact-info-title">Contact Information</h3>
        <div class="contact-info-items">
          <a class="contact-info-row" href="mailto:ADD_YOUR_EMAIL">
            <div class="ci-icon"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg></div>
            <div class="ci-text"><span class="ci-label">Email</span><span class="ci-value">ADD_YOUR_EMAIL</span></div>
          </a>
          <a class="contact-info-row" href="tel:7980658742">
            <div class="ci-icon"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg></div>
            <div class="ci-text"><span class="ci-label">Phone</span><span class="ci-value">7980658742</span></div>
          </a>
          <div class="contact-info-row">
            <div class="ci-icon"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg></div>
            <div class="ci-text"><span class="ci-label">Location</span><span class="ci-value">Jamshedpur, Jharkhand, India</span></div>
          </div>
          <a class="contact-info-row" href="https://www.linkedin.com/in/tusharsingh-analytics" target="_blank" rel="noopener">
            <div class="ci-icon linkedin-ci"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg></div>
            <div class="ci-text"><span class="ci-label">LinkedIn</span><span class="ci-value">tusharsingh-analytics</span></div>
          </a>
          <a class="contact-info-row" href="https://github.com/Tusharsingh23Up" target="_blank" rel="noopener">
            <div class="ci-icon github-ci"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg></div>
            <div class="ci-text"><span class="ci-label">GitHub</span><span class="ci-value">Tusharsingh23Up</span></div>
          </a>
          <a class="contact-info-row" href="https://tushar-finance-forge.lovable.app" target="_blank" rel="noopener">
            <div class="ci-icon portfolio-ci"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 010 20M12 2a15.3 15.3 0 000 20"/></svg></div>
            <div class="ci-text"><span class="ci-label">Portfolio</span><span class="ci-value">tushar-finance-forge.lovable.app</span></div>
          </a>
        </div>
      </div>
    </div>
  </div>
</section>

<footer class="footer">
  <div class="footer-container">
    <div class="footer-brand">
      <span class="footer-logo-initials">TS</span>
      <span class="footer-name">Tushar Singh</span>
    </div>
    <p class="footer-tagline">Data-driven insights. Clear dashboards. Smarter business decisions.</p>
    <div class="footer-socials">
      <a href="https://github.com/Tusharsingh23Up" target="_blank" rel="noopener" class="footer-social-icon" aria-label="GitHub">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
      </a>
      <a href="https://www.linkedin.com/in/tusharsingh-analytics" target="_blank" rel="noopener" class="footer-social-icon" aria-label="LinkedIn">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
      </a>
      <a href="mailto:ADD_YOUR_EMAIL" class="footer-social-icon" aria-label="Email">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
      </a>
    </div>
    <p class="footer-copy">&copy; 2026 Tushar Singh. All rights reserved.</p>
  </div>
</footer>

<script src="script.js"></script>
</body>
</html>
"""

with open("p6.html","w",encoding="utf-8") as f:
    f.write(s6)
print("p6 done",len(s6))
