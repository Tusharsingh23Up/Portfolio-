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
          <div class="exp-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 00-2-2h-4a2 2 0 00-2 2v2"/></svg>
          </div>
          <div class="exp-company">FinAnalytics Solutions</div>
          <div class="exp-badge">Remote Internship</div>
          <div class="exp-location">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="14" height="14"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
            Remote
          </div>
          <div class="exp-duration">Mar 2026 &ndash; May 2026</div>
        </div>
        <div class="exp-card-right">
          <h3 class="exp-role">Data Analyst Intern</h3>
          <div class="exp-responsibilities">
            <h4>Key Responsibilities</h4>
            <ul>
              <li class="exp-bullet">Performed credit-risk modeling and portfolio analytics using Python and SQL.</li>
              <li class="exp-bullet">Designed automated data pipelines and ETL processes to improve data quality for real-time dashboards.</li>
              <li class="exp-bullet">Built interactive Power BI dashboards to visualize loan approval rates and risk segmentation.</li>
              <li class="exp-bullet">Collaborated with cross-functional teams using Git, JIRA, and Slack to prioritize tasks and deliver actionable insights.</li>
            </ul>
          </div>
          <div class="exp-achievements-block">
            <h4>Key Achievements</h4>
            <ul>
              <li class="exp-bullet achievement">Improved scorecard accuracy and reduced default prediction error through credit-risk modeling.</li>
              <li class="exp-bullet achievement">Delivered stakeholder-ready dashboards that helped visualize risk segmentation, loan approval trends, and portfolio performance.</li>
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
