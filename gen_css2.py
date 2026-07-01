css2 = r"""
/* SECTIONS SHARED */
.section { padding:100px 0; }
.section:nth-child(even) { background:var(--off-white); }
.section:nth-child(odd) { background:var(--white); }
.section-container { max-width:1280px; margin:0 auto; padding:0 2rem; }
.section-header { text-align:center; margin-bottom:4rem; }
.section-tag { display:inline-block; background:linear-gradient(135deg,rgba(201,162,39,0.12),rgba(201,162,39,0.06)); border:1px solid rgba(201,162,39,0.25); color:var(--gold); font-size:0.72rem; font-weight:700; letter-spacing:0.12em; text-transform:uppercase; padding:0.3rem 1rem; border-radius:20px; margin-bottom:1rem; }
.section-title { font-size:clamp(2rem,5vw,3rem); font-weight:800; color:var(--navy); letter-spacing:-0.02em; margin-bottom:1rem; }
.section-line { width:60px; height:3px; background:linear-gradient(90deg,var(--gold),var(--gold-light)); margin:0 auto; border-radius:2px; }
.section-subtitle { max-width:600px; margin:1.5rem auto 0; color:var(--text-mid); font-size:1rem; line-height:1.7; }

/* ABOUT */
.about-section { background:var(--navy) !important; }
.about-section .section-title { color:var(--white); }
.about-section .section-tag { color:var(--gold-light); border-color:rgba(201,162,39,0.3); }
.about-grid { display:grid; grid-template-columns:300px 1fr; gap:4rem; align-items:start; }
.about-photo-wrapper { position:relative; display:flex; justify-content:center; }
.about-photo-frame { width:240px; height:240px; border-radius:50%; overflow:hidden; border:4px solid var(--gold); position:relative; z-index:1; box-shadow:0 0 0 8px rgba(201,162,39,0.12); }
.about-photo { width:100%; height:100%; object-fit:cover; }
.photo-placeholder { width:100%; height:100%; background:linear-gradient(135deg,var(--navy-mid),var(--navy-light)); display:flex; align-items:center; justify-content:center; }
.photo-initials { font-size:4rem; font-weight:900; color:var(--gold); }
.about-photo-glow { position:absolute; inset:-20px; border-radius:50%; background:radial-gradient(circle,rgba(201,162,39,0.15) 0%,transparent 65%); animation:photoGlow 3s ease-in-out infinite alternate; }
@keyframes photoGlow { 0%{opacity:0.5;transform:scale(0.95);} 100%{opacity:1;transform:scale(1.05);} }
.about-cta-buttons { display:flex; flex-direction:column; gap:0.6rem; margin-top:1.5rem; }
.about-btn { display:block; text-align:center; padding:0.6rem 1.2rem; background:rgba(201,162,39,0.08); border:1px solid rgba(201,162,39,0.25); color:var(--gold-light); border-radius:var(--radius-sm); text-decoration:none; font-size:0.85rem; font-weight:600; transition:all var(--transition); position:relative; overflow:hidden; }
.about-btn::after { content:''; position:absolute; bottom:0; left:0; width:0; height:2px; background:var(--gold); transition:width var(--transition); }
.about-btn:hover { background:rgba(201,162,39,0.15); transform:translateX(4px); color:var(--white); }
.about-btn:hover::after { width:100%; }
.about-summary { color:rgba(255,255,255,0.78); line-height:1.85; font-size:1rem; margin-bottom:2rem; }
.mission-vision-grid { display:grid; grid-template-columns:1fr 1fr; gap:1.5rem; }
.mv-card { background:rgba(255,255,255,0.04); border:1px solid rgba(201,162,39,0.15); border-radius:var(--radius-md); padding:1.5rem; transition:all var(--transition); }
.mv-card:hover { background:rgba(201,162,39,0.06); border-color:rgba(201,162,39,0.35); transform:translateY(-4px); }
.mv-icon { width:44px; height:44px; border-radius:var(--radius-sm); background:linear-gradient(135deg,rgba(201,162,39,0.18),rgba(201,162,39,0.08)); display:flex; align-items:center; justify-content:center; color:var(--gold); margin-bottom:1rem; }
.mv-icon svg { width:22px; height:22px; }
.mv-card h3 { color:var(--gold-light); font-size:1rem; font-weight:700; margin-bottom:0.6rem; }
.mv-card p { color:rgba(255,255,255,0.65); font-size:0.88rem; line-height:1.7; }

/* EXPERIENCE */
.experience-cards { display:flex; flex-direction:column; gap:2rem; }
.exp-card { display:grid; grid-template-columns:260px 1fr; background:var(--card-bg); border-radius:var(--radius-lg); box-shadow:var(--shadow-md); overflow:hidden; border:1px solid var(--border); transition:transform var(--transition),box-shadow var(--transition); }
.exp-card:hover { transform:translateY(-6px); box-shadow:var(--shadow-lg); }
.exp-card-left { background:var(--navy); padding:2rem; display:flex; flex-direction:column; gap:0.75rem; position:relative; overflow:hidden; }
.exp-card-left::before { content:''; position:absolute; top:0; left:0; right:0; height:3px; background:linear-gradient(90deg,var(--gold),var(--gold-light)); }
.exp-icon { width:48px; height:48px; background:rgba(201,162,39,0.12); border-radius:var(--radius-sm); display:flex; align-items:center; justify-content:center; color:var(--gold); margin-bottom:0.5rem; }
.exp-icon svg { width:24px; height:24px; }
.exp-company { color:var(--white); font-weight:700; font-size:1rem; line-height:1.3; }
.exp-badge { display:inline-block; background:rgba(201,162,39,0.15); border:1px solid rgba(201,162,39,0.3); color:var(--gold-light); font-size:0.7rem; font-weight:700; letter-spacing:0.06em; padding:0.2rem 0.75rem; border-radius:20px; text-transform:uppercase; animation:badgePulse 3s ease-in-out infinite; }
@keyframes badgePulse { 0%,100%{box-shadow:0 0 0 0 rgba(201,162,39,0.2);} 50%{box-shadow:0 0 0 6px rgba(201,162,39,0);} }
.exp-location { display:flex; align-items:center; gap:4px; color:rgba(255,255,255,0.55); font-size:0.8rem; }
.exp-duration { color:rgba(255,255,255,0.45); font-size:0.8rem; font-style:italic; }
.exp-card-right { padding:2rem; }
.exp-role { font-size:1.4rem; font-weight:800; color:var(--navy); margin-bottom:1.5rem; letter-spacing:-0.01em; }
.exp-responsibilities h4,.exp-achievements-block h4 { font-size:0.78rem; font-weight:700; color:var(--gold); letter-spacing:0.08em; text-transform:uppercase; margin-bottom:0.75rem; }
.exp-responsibilities ul,.exp-achievements-block ul { list-style:none; padding:0; }
.exp-bullet { position:relative; padding-left:1.2rem; color:var(--text-mid); font-size:0.92rem; line-height:1.7; margin-bottom:0.5rem; }
.exp-bullet::before { content:''; position:absolute; left:0; top:0.65em; width:6px; height:6px; background:var(--gold); border-radius:50%; }
.exp-bullet.achievement::before { background:#22c55e; }
.exp-achievements-block { margin-top:1.5rem; }

/* EDUCATION */
.education-cards { display:flex; flex-direction:column; gap:2rem; }
.edu-card { background:var(--card-bg); border-radius:var(--radius-lg); box-shadow:var(--shadow-md); border:1px solid var(--border); overflow:hidden; position:relative; transition:transform var(--transition),box-shadow var(--transition); }
.edu-card:hover { transform:translateY(-6px); box-shadow:var(--shadow-lg); }
.edu-card-accent { height:4px; background:linear-gradient(90deg,var(--navy),var(--gold),var(--navy-light)); }
.edu-card-content { padding:2rem; }
.edu-header { display:flex; gap:1.5rem; align-items:flex-start; margin-bottom:1.5rem; }
.edu-icon { width:56px; height:56px; flex-shrink:0; background:linear-gradient(135deg,var(--navy),var(--navy-light)); border-radius:var(--radius-md); display:flex; align-items:center; justify-content:center; color:var(--gold); transition:transform var(--transition); }
.edu-card:hover .edu-icon { transform:rotate(6deg) scale(1.1); }
.edu-icon svg { width:28px; height:28px; }
.edu-degree { font-size:1.4rem; font-weight:800; color:var(--navy); letter-spacing:-0.01em; }
.edu-institution { color:var(--text-mid); font-weight:600; margin:0.25rem 0; font-size:1rem; }
.edu-duration-mode { display:flex; gap:0.75rem; align-items:center; margin-top:0.5rem; flex-wrap:wrap; }
.edu-duration { color:var(--text-light); font-size:0.85rem; }
.edu-mode-badge { background:rgba(10,22,40,0.06); color:var(--navy); font-size:0.72rem; font-weight:700; padding:0.2rem 0.65rem; border-radius:20px; letter-spacing:0.04em; }
.edu-highlights h4 { font-size:0.78rem; font-weight:700; color:var(--gold); text-transform:uppercase; letter-spacing:0.08em; margin-bottom:0.75rem; }
.edu-bullet { position:relative; padding-left:1.2rem; color:var(--text-mid); font-size:0.92rem; line-height:1.7; margin-bottom:0.5rem; list-style:none; }
.edu-bullet::before { content:''; position:absolute; left:0; top:0.65em; width:6px; height:6px; background:linear-gradient(135deg,var(--gold),var(--gold-light)); border-radius:50%; }
"""

with open("css2.css","w",encoding="utf-8") as f:
    f.write(css2)
print("css2 done",len(css2))
