css3 = r"""
/* PROJECTS */
.projects-section { background:var(--navy) !important; }
.projects-section .section-title { color:var(--white); }
.projects-section .section-tag { color:var(--gold-light); border-color:rgba(201,162,39,0.3); }
.projects-list { display:flex; flex-direction:column; gap:2rem; }
.project-card { display:grid; grid-template-columns:200px 1fr; background:rgba(255,255,255,0.04); border:1px solid rgba(201,162,39,0.12); border-radius:var(--radius-lg); overflow:hidden; transition:all var(--transition); }
.project-card:hover { background:rgba(255,255,255,0.06); border-color:rgba(201,162,39,0.3); transform:translateY(-4px); box-shadow:0 20px 48px rgba(0,0,0,0.4); }
.project-left { background:linear-gradient(180deg,rgba(201,162,39,0.08) 0%,rgba(201,162,39,0.02) 100%); border-right:1px solid rgba(201,162,39,0.1); padding:2rem 1.5rem; display:flex; flex-direction:column; gap:1rem; }
.project-number { font-size:3.5rem; font-weight:900; color:rgba(201,162,39,0.15); line-height:1; letter-spacing:-0.05em; }
.project-type-badge { background:rgba(201,162,39,0.12); border:1px solid rgba(201,162,39,0.25); color:var(--gold-light); font-size:0.68rem; font-weight:700; letter-spacing:0.06em; padding:0.25rem 0.7rem; border-radius:20px; text-transform:uppercase; display:inline-block; }
.project-duration { color:rgba(255,255,255,0.4); font-size:0.78rem; font-style:italic; }
.project-right { padding:2rem; }
.project-title { font-size:1.3rem; font-weight:800; color:var(--white); margin-bottom:1rem; letter-spacing:-0.01em; transition:letter-spacing var(--transition); }
.project-card:hover .project-title { letter-spacing:0.01em; }
.project-desc { color:rgba(255,255,255,0.6); font-size:0.9rem; line-height:1.75; margin-bottom:1.5rem; }
.project-outcomes h4 { font-size:0.75rem; font-weight:700; color:var(--gold); text-transform:uppercase; letter-spacing:0.08em; margin-bottom:0.75rem; }
.outcomes-grid { display:grid; grid-template-columns:1fr 1fr; gap:0.75rem; margin-bottom:1.5rem; }
.outcome-box { background:rgba(255,255,255,0.03); border:1px solid rgba(201,162,39,0.1); border-radius:var(--radius-sm); padding:0.75rem 1rem; color:rgba(255,255,255,0.65); font-size:0.82rem; line-height:1.55; transition:all var(--transition); }
.outcome-box:hover { background:rgba(201,162,39,0.06); border-color:rgba(201,162,39,0.25); }
.project-tech { display:flex; flex-wrap:wrap; gap:0.5rem; }
.tech-pill { background:rgba(201,162,39,0.08); border:1px solid rgba(201,162,39,0.2); color:var(--gold-light); font-size:0.72rem; font-weight:600; padding:0.3rem 0.75rem; border-radius:20px; letter-spacing:0.02em; transition:all var(--transition); }
.tech-pill:hover { background:rgba(201,162,39,0.18); border-color:var(--gold); transform:translateY(-2px); }

/* SKILLS */
.skills-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(340px,1fr)); gap:1.5rem; }
.skill-category { background:var(--card-bg); border:1px solid var(--border); border-radius:var(--radius-lg); padding:1.75rem; box-shadow:var(--shadow-sm); transition:all var(--transition); position:relative; overflow:hidden; }
.skill-category::before { content:''; position:absolute; top:0; left:0; right:0; height:3px; background:linear-gradient(90deg,var(--navy),var(--gold)); transform:scaleX(0); transform-origin:left; transition:transform var(--transition); }
.skill-category:hover::before { transform:scaleX(1); }
.skill-category:hover { transform:translateY(-6px); box-shadow:var(--shadow-lg); border-color:rgba(201,162,39,0.2); }
.skill-category:hover .skill-cat-icon svg { transform:rotate(360deg); }
.skill-category-header { display:flex; align-items:center; gap:1rem; margin-bottom:1.5rem; }
.skill-cat-icon { width:44px; height:44px; background:linear-gradient(135deg,var(--navy),var(--navy-light)); border-radius:var(--radius-sm); display:flex; align-items:center; justify-content:center; color:var(--gold); flex-shrink:0; }
.skill-cat-icon svg { width:22px; height:22px; transition:transform 0.7s ease; }
.skill-category-header h3 { font-size:1rem; font-weight:700; color:var(--navy); line-height:1.3; }
.skill-bars { display:flex; flex-direction:column; gap:1rem; }
.skill-item { display:flex; flex-direction:column; gap:0.35rem; }
.skill-label { display:flex; justify-content:space-between; font-size:0.83rem; font-weight:600; color:var(--text-dark); }
.skill-pct { color:var(--gold); font-weight:700; font-size:0.8rem; }
.skill-bar-track { height:6px; width:100%; background:var(--off-white); border-radius:3px; overflow:hidden; border:1px solid var(--border); }
.skill-bar-fill { height:100%; width:0; background:linear-gradient(90deg,var(--navy),var(--gold)); border-radius:3px; transition:width 1.1s cubic-bezier(0.4,0,0.2,1); }

/* CERTIFICATIONS */
.cert-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(300px,1fr)); gap:1.75rem; }
.cert-card { background:var(--card-bg); border:1px solid var(--border); border-radius:var(--radius-lg); overflow:hidden; box-shadow:var(--shadow-sm); transition:all var(--transition); cursor:default; }
.cert-card:hover { transform:translateY(-6px) rotate(1deg); box-shadow:var(--shadow-gold); background:#fffdf4; }
.cert-image-wrapper { height:220px; overflow:hidden; background:linear-gradient(135deg,var(--navy) 0%,var(--navy-mid) 100%); position:relative; }
.cert-image { width:100%; height:100%; object-fit:cover; transition:transform 0.6s ease; }
.cert-card:hover .cert-image { transform:scale(1.05); }
.cert-img-placeholder { width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:0.75rem; color:rgba(255,255,255,0.3); }
.cert-img-placeholder svg { width:48px; height:48px; }
.cert-img-placeholder span { font-size:0.8rem; color:rgba(255,255,255,0.4); }
.cert-body { padding:1.5rem; }
.cert-provider-badge { display:inline-block; font-size:0.7rem; font-weight:700; letter-spacing:0.06em; text-transform:uppercase; padding:0.25rem 0.8rem; border-radius:20px; margin-bottom:0.75rem; }
.cert-provider-badge.google { background:#e8f0fe; color:#1967d2; }
.cert-provider-badge.microsoft { background:#e6f3ff; color:#0078d4; }
.cert-provider-badge.specialization { background:rgba(201,162,39,0.1); color:var(--gold); border:1px solid rgba(201,162,39,0.25); }
.cert-title { font-size:0.95rem; font-weight:700; color:var(--navy); line-height:1.4; margin-bottom:0.75rem; }
.cert-meta { display:flex; align-items:center; gap:0.75rem; }
.cert-year { font-size:0.8rem; font-weight:600; color:var(--text-light); }
.cert-type-badge { background:rgba(10,22,40,0.06); color:var(--navy); font-size:0.7rem; font-weight:700; padding:0.2rem 0.65rem; border-radius:20px; }
"""

with open("css3.css","w",encoding="utf-8") as f:
    f.write(css3)
print("css3 done",len(css3))
