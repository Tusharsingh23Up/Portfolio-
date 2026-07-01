css1 = r"""/* ============================================================
   TUSHAR SINGH PORTFOLIO — style.css
   Theme: Navy Blue / White / Gold  |  Font: Inter
   ============================================================ */
:root {
  --navy: #0a1628; --navy-mid: #0f2044; --navy-light: #1a3260;
  --gold: #c9a227; --gold-light: #e8c555; --gold-pale: #f5e6b2;
  --white: #ffffff; --off-white: #f8f9fc;
  --text-dark: #0d1b2e; --text-mid: #4a5568; --text-light: #718096;
  --card-bg: #ffffff; --border: #e2e8f0;
  --shadow-sm: 0 2px 8px rgba(10,22,40,0.08);
  --shadow-md: 0 8px 24px rgba(10,22,40,0.12);
  --shadow-lg: 0 16px 48px rgba(10,22,40,0.18);
  --shadow-gold: 0 8px 32px rgba(201,162,39,0.25);
  --radius-sm: 8px; --radius-md: 14px; --radius-lg: 20px;
  --transition: 0.3s cubic-bezier(0.4,0,0.2,1);
}
*,*::before,*::after { box-sizing:border-box; margin:0; padding:0; }
html { scroll-behavior:smooth; scroll-padding-top:70px; }
body { font-family:'Inter',sans-serif; color:var(--text-dark); background:var(--off-white); line-height:1.6; overflow-x:hidden; }
::-webkit-scrollbar { width:6px; }
::-webkit-scrollbar-track { background:var(--navy); }
::-webkit-scrollbar-thumb { background:var(--gold); border-radius:3px; }

/* NAVBAR */
.navbar { position:fixed; top:0; left:0; right:0; z-index:1000; background:rgba(10,22,40,0.92); backdrop-filter:blur(12px); -webkit-backdrop-filter:blur(12px); border-bottom:1px solid rgba(201,162,39,0.15); transition:background var(--transition),box-shadow var(--transition); }
.navbar.scrolled { background:rgba(10,22,40,0.98); box-shadow:0 4px 20px rgba(0,0,0,0.4); }
.nav-container { max-width:1280px; margin:0 auto; padding:0 2rem; height:68px; display:flex; align-items:center; justify-content:space-between; }
.nav-logo { display:flex; align-items:center; gap:10px; text-decoration:none; color:var(--white); }
.logo-initials { width:38px; height:38px; background:linear-gradient(135deg,var(--gold),var(--gold-light)); border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:0.9rem; color:var(--navy); flex-shrink:0; }
.logo-name { font-weight:700; font-size:1rem; letter-spacing:0.02em; }
.nav-links { display:flex; list-style:none; gap:0.25rem; align-items:center; }
.nav-link { text-decoration:none; color:rgba(255,255,255,0.75); font-size:0.85rem; font-weight:500; padding:0.4rem 0.75rem; border-radius:var(--radius-sm); transition:color var(--transition),background var(--transition); letter-spacing:0.01em; }
.nav-link:hover,.nav-link.active { color:var(--white); background:rgba(201,162,39,0.1); }
.nav-link.nav-cta { background:linear-gradient(135deg,var(--gold),var(--gold-light)); color:var(--navy); font-weight:700; padding:0.45rem 1.1rem; }
.nav-link.nav-cta:hover { opacity:0.9; }
.nav-toggle { display:none; flex-direction:column; gap:5px; background:none; border:none; cursor:pointer; padding:4px; }
.nav-toggle span { display:block; width:24px; height:2px; background:var(--white); border-radius:2px; transition:transform var(--transition),opacity var(--transition); }

/* HERO */
.hero { min-height:100vh; background:linear-gradient(135deg,var(--navy) 0%,var(--navy-mid) 60%,#0d1f3c 100%); display:flex; align-items:center; justify-content:center; position:relative; overflow:hidden; padding:100px 2rem 80px; }
.hero::before { content:''; position:absolute; top:-50%; left:-20%; width:80vw; height:80vw; background:radial-gradient(circle,rgba(201,162,39,0.06) 0%,transparent 65%); pointer-events:none; }
.hero-particles { position:absolute; inset:0; pointer-events:none; overflow:hidden; }
.particle { position:absolute; background:var(--gold); border-radius:50%; opacity:0.15; animation:floatParticle linear infinite; }
@keyframes floatParticle { 0%{transform:translateY(0) scale(1);opacity:0;} 10%{opacity:0.2;} 90%{opacity:0.1;} 100%{transform:translateY(-110vh) scale(0.6);opacity:0;} }
.hero-container { max-width:900px; width:100%; position:relative; z-index:2; text-align:center; }
.hero-content { display:flex; flex-direction:column; align-items:center; gap:1.5rem; }
.hero-badge { display:inline-flex; align-items:center; gap:10px; background:rgba(201,162,39,0.12); border:1px solid rgba(201,162,39,0.3); border-radius:40px; padding:0.45rem 1.2rem; color:var(--gold-light); font-size:0.8rem; font-weight:600; letter-spacing:0.08em; text-transform:uppercase; }
.hero-logo-initials { width:26px; height:26px; background:var(--gold); border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:0.65rem; color:var(--navy); flex-shrink:0; }
.hero-name { font-size:clamp(3rem,8vw,5.5rem); font-weight:900; color:var(--white); letter-spacing:-0.02em; line-height:1.05; background:linear-gradient(135deg,#fff 30%,var(--gold-light) 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; }
.hero-designations { display:flex; flex-wrap:wrap; justify-content:center; gap:0.4rem 0.8rem; font-size:clamp(0.75rem,2.5vw,1rem); color:rgba(255,255,255,0.65); font-weight:500; }
.designation-item { white-space:nowrap; }
.designation-sep { color:var(--gold); opacity:0.6; }
.hero-intro { font-size:clamp(0.9rem,2vw,1.05rem); color:rgba(255,255,255,0.7); max-width:700px; line-height:1.8; }
.hero-cta { display:flex; gap:1rem; flex-wrap:wrap; justify-content:center; margin-top:0.5rem; }
.btn { display:inline-flex; align-items:center; gap:8px; padding:0.85rem 2rem; border-radius:50px; font-weight:700; font-size:0.9rem; text-decoration:none; transition:all var(--transition); cursor:pointer; border:2px solid transparent; letter-spacing:0.02em; }
.btn-primary { background:linear-gradient(135deg,var(--gold),var(--gold-light)); color:var(--navy); box-shadow:var(--shadow-gold); }
.btn-primary:hover { transform:translateY(-3px); box-shadow:0 12px 40px rgba(201,162,39,0.4); }
.btn-outline { background:transparent; color:var(--white); border-color:rgba(255,255,255,0.35); }
.btn-outline:hover { background:rgba(255,255,255,0.08); border-color:var(--gold); color:var(--gold-light); transform:translateY(-3px); }
.hero-socials { display:flex; gap:1rem; margin-top:0.5rem; }
.social-icon { width:44px; height:44px; border-radius:50%; background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.15); display:flex; align-items:center; justify-content:center; color:rgba(255,255,255,0.7); text-decoration:none; transition:all var(--transition); }
.social-icon svg { width:18px; height:18px; }
.social-icon:hover { background:rgba(201,162,39,0.15); border-color:var(--gold); color:var(--gold-light); transform:translateY(-4px) scale(1.1); }
.hero-scroll-indicator { position:absolute; bottom:2rem; left:50%; transform:translateX(-50%); z-index:2; }
.scroll-dot { width:8px; height:8px; background:var(--gold); border-radius:50%; animation:scrollBounce 1.6s ease-in-out infinite; }
@keyframes scrollBounce { 0%,100%{transform:translateY(0);opacity:0.8;} 50%{transform:translateY(10px);opacity:0.3;} }
"""

with open("css1.css","w",encoding="utf-8") as f:
    f.write(css1)
print("css1 done",len(css1))
