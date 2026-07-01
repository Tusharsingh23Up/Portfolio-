s3 = r"""
<section class="section projects-section" id="projects">
  <div class="section-container">
    <div class="section-header animate-on-scroll">
      <span class="section-tag">Portfolio</span>
      <h2 class="section-title">Projects</h2>
      <div class="section-line"></div>
    </div>
    <div class="projects-list">

      <div class="project-card animate-project-in">
        <div class="project-left">
          <div class="project-number">01</div>
          <div class="project-type-badge">Remote Analytics Project</div>
          <div class="project-duration">Jun 2025 &ndash; Aug 2025</div>
        </div>
        <div class="project-right">
          <h3 class="project-title">Credit-Risk Modeling &amp; Scorecard Development</h3>
          <p class="project-desc">This project focused on analyzing credit bureau and transactional datasets to predict default risk across customer segments. It involved feature engineering, model development, validation, and dashboard deployment for credit-risk monitoring.</p>
          <div class="project-outcomes">
            <h4>Key Outcomes</h4>
            <div class="outcomes-grid">
              <div class="outcome-box">Engineered predictive features using Weight of Evidence and Information Value.</div>
              <div class="outcome-box">Trained and validated logistic regression and gradient boosting models.</div>
              <div class="outcome-box">Achieved ROC-AUC &gt; 0.85 for default-risk prediction.</div>
              <div class="outcome-box">Built a Power BI dashboard to monitor model performance and support real-time credit policy decisions.</div>
            </div>
          </div>
          <div class="project-tech">
            <span class="tech-pill">Python</span><span class="tech-pill">SQL</span><span class="tech-pill">Power BI</span>
            <span class="tech-pill">Logistic Regression</span><span class="tech-pill">Gradient Boosting</span>
            <span class="tech-pill">WOE / IV</span><span class="tech-pill">Credit Risk Analytics</span>
          </div>
        </div>
      </div>

      <div class="project-card animate-project-in">
        <div class="project-left">
          <div class="project-number">02</div>
          <div class="project-type-badge">Financial Analytics Project</div>
          <div class="project-duration">Jan 2026 &ndash; Feb 2026</div>
        </div>
        <div class="project-right">
          <h3 class="project-title">End-to-End Financial Analyst Case Study</h3>
          <p class="project-desc">This project involved cleaning and analyzing financial data to understand company performance through ratio analysis, benchmarking, and trend analysis. The outcome was a set of KPI dashboards and executive reports summarizing business performance, risks, and recommendations.</p>
          <div class="project-outcomes">
            <h4>Key Outcomes</h4>
            <div class="outcomes-grid">
              <div class="outcome-box">Cleaned financial data using SQL and Excel.</div>
              <div class="outcome-box">Conducted ratio analysis, benchmarking, and trend analysis for peer companies.</div>
              <div class="outcome-box">Created KPI dashboards covering liquidity, profitability, and leverage metrics.</div>
              <div class="outcome-box">Prepared executive-level reports summarizing trends, risks, and business recommendations.</div>
            </div>
          </div>
          <div class="project-tech">
            <span class="tech-pill">SQL</span><span class="tech-pill">Excel</span><span class="tech-pill">Power BI</span>
            <span class="tech-pill">Financial Analysis</span><span class="tech-pill">KPI Dashboards</span><span class="tech-pill">Data Storytelling</span>
          </div>
        </div>
      </div>

      <div class="project-card animate-project-in">
        <div class="project-left">
          <div class="project-number">03</div>
          <div class="project-type-badge">Self-Directed Analytics</div>
          <div class="project-duration">2024 &ndash; 2025</div>
        </div>
        <div class="project-right">
          <h3 class="project-title">Analytics Workbench &amp; KPI Dashboard</h3>
          <p class="project-desc">This project focused on building an analytics workbench to ingest, clean, merge, and analyze multi-company financial statement data. It included KPI modeling, dashboard development, and real-time insight delivery using modern analytics tools.</p>
          <div class="project-outcomes">
            <h4>Key Outcomes</h4>
            <div class="outcomes-grid">
              <div class="outcome-box">Developed an analytics workbench to process multi-company financial statements.</div>
              <div class="outcome-box">Used Python and SQL to ingest, clean, and merge structured financial data.</div>
              <div class="outcome-box">Designed data models to calculate KPIs across revenue growth, expense ratios, and cash flow metrics.</div>
              <div class="outcome-box">Built interactive dashboards using Power BI and Streamlit.</div>
            </div>
          </div>
          <div class="project-tech">
            <span class="tech-pill">Python</span><span class="tech-pill">SQL</span><span class="tech-pill">Power BI</span>
            <span class="tech-pill">Streamlit</span><span class="tech-pill">Excel</span><span class="tech-pill">KPI Modeling</span><span class="tech-pill">Financial Statements</span>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>
"""

with open("p3.html","w",encoding="utf-8") as f:
    f.write(s3)
print("p3 done",len(s3))
