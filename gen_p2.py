s2 = r"""
<section class="section about-section" id="about">
  <div class="section-container">
    <div class="section-header animate-on-scroll">
      <span class="section-tag">About Me</span>
      <h2 class="section-title">Who I Am</h2>
      <div class="section-line"></div>
    </div>
    <div class="about-grid">
      <div class="about-photo-col animate-slide-left">
        <div class="about-photo-wrapper">
          <div class="about-photo-frame">
            <img src="profile_photo.jpg" alt="Tushar Singh - Data Analyst" class="about-photo"
                 onerror="this.parentElement.innerHTML='&lt;div class=&quot;photo-placeholder&quot;&gt;&lt;span class=&quot;photo-initials&quot;&gt;TS&lt;/span&gt;&lt;/div&gt;'" />
          </div>
          <div class="about-photo-glow"></div>
        </div>
        <div class="about-cta-buttons">
          <a href="#experience" class="about-btn">Work Experience</a>
          <a href="#education" class="about-btn">Education</a>
          <a href="#projects" class="about-btn">Projects</a>
          <a href="#skills" class="about-btn">Skills</a>
          <a href="#certifications" class="about-btn">Certifications</a>
        </div>
      </div>
      <div class="about-content-col animate-slide-right">
        <p class="about-summary">I am a Data Analyst and Business Analyst focused on transforming data into clear, actionable business insights. I am currently pursuing a B.Tech in Data Analysis from Bennett University, where I have built strong foundations in Python, SQL, Data Analytics, Financial Analysis, Business Analysis, and Financial Modeling. My experience includes a remote Data Analyst internship at FinAnalytics Solutions, where I worked on credit-risk modeling, portfolio analytics, automated data pipelines, and Power BI dashboards. I have also completed multiple self-directed analytics projects involving credit-risk scorecards, financial ratio analysis, KPI dashboards, and interactive business reporting. I work with tools such as Python, SQL, Excel, Power BI, Jupyter Notebooks, Git, and Streamlit. What makes me stand out is my ability to combine technical analysis with business communication, helping stakeholders understand trends, risks, and opportunities through clean dashboards and executive-ready insights.</p>
        <div class="mission-vision-grid">
          <div class="mv-card mission-card animate-flip-in">
            <div class="mv-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
            </div>
            <h3>Mission</h3>
            <p>To use data analytics, business analysis, and visualization to help organizations make faster, clearer, and more confident decisions.</p>
          </div>
          <div class="mv-card vision-card animate-flip-in">
            <div class="mv-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
            </div>
            <h3>Vision</h3>
            <p>To become a high-impact Data Analyst and Business Analyst who builds reliable analytics systems, meaningful dashboards, and business insights that create measurable value.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section experience-section" id="experience">
  <div class="section-container">
    <div class="section-header animate-on-scroll">
      <span class="section-tag">Career</span>
      <h2 class="section-title">Work Experience</h2>
      <div class="section-line"></div>
    </div>
    <div class="experience-cards">
      <div class="exp-card animate-slide-left-exp">
        <div class="exp-card-left">
          <div class="exp-icon exp-icon-logo">
            <span class="exp-logo-text">EXL</span>
          </div>
          <div class="exp-company">EXL</div>
          <div class="exp-badge">Internship</div>
          <div class="exp-location">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="14" height="14"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
            India &middot; Remote
          </div>
          <div class="exp-duration">Jun 2026 &ndash; Present</div>
        </div>
        <div class="exp-card-right">
          <h3 class="exp-role">Data Analyst Intern</h3>
          <p class="exp-description">Data Analyst Intern role focused on supporting data cleaning, analysis, KPI reporting, dashboard development, and business insights. The role involves using SQL, Excel, Python, and Power BI to work with business data, identify trends, prepare reports, and support data-driven decision-making across operations, finance, and risk-related projects.</p>
          <div class="exp-responsibilities">
            <h4>Key Responsibilities</h4>
            <ul>
              <li class="exp-bullet">Clean, validate, and organize raw datasets for analysis.</li>
              <li class="exp-bullet">Perform data analysis to identify trends, patterns, and performance gaps.</li>
              <li class="exp-bullet">Build dashboards and reports using Power BI and Excel.</li>
              <li class="exp-bullet">Write SQL queries to extract and analyze business data.</li>
              <li class="exp-bullet">Support KPI tracking, business reporting, and performance analysis.</li>
              <li class="exp-bullet">Prepare insights and summaries for stakeholders.</li>
              <li class="exp-bullet">Assist in automating reports and improving data accuracy.</li>
              <li class="exp-bullet">Collaborate with teams to understand business requirements and deliver actionable insights.</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section education-section" id="education">
  <div class="section-container">
    <div class="section-header animate-on-scroll">
      <span class="section-tag">Academic</span>
      <h2 class="section-title">Education</h2>
      <div class="section-line"></div>
    </div>
    <div class="education-cards">
      <div class="edu-card animate-drop-in">
        <div class="edu-card-accent"></div>
        <div class="edu-card-content">
          <div class="edu-header">
            <div class="edu-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5-10-5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>
            </div>
            <div class="edu-meta">
              <h3 class="edu-degree">B.Tech in Data Analysis</h3>
              <div class="edu-institution">Bennett University</div>
              <div class="edu-duration-mode">
                <span class="edu-duration">Aug 2023 &ndash; May 2027</span>
                <span class="edu-mode-badge">Full-time</span>
              </div>
            </div>
          </div>
          <div class="edu-highlights">
            <h4>Key Highlights</h4>
            <ul>
              <li class="edu-bullet">Built strong academic foundations in Python, SQL, Data Analytics, Business Analysis, and Financial Analysis.</li>
              <li class="edu-bullet">Completed coursework in Financial Modeling and analytical problem-solving.</li>
              <li class="edu-bullet">Developed practical project experience across credit-risk modeling, financial analysis, KPI reporting, and dashboard development.</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
"""

with open("p2.html","w",encoding="utf-8") as f:
    f.write(s2)
print("p2 done",len(s2))
