from pathlib import Path
import re, base64, zipfile
import mistune
from bs4 import BeautifulSoup
root=Path(__file__).parent
md=mistune.create_markdown(plugins=['table'])
src=(root/'content.md').read_text()
# Convert widget markers to safe HTML placeholders after Markdown conversion.
chunks=re.split(r'(?m)(?=^#{1,2} )',src)
articles=[]; nav=[]; counter=0
for chunk in chunks:
 if not chunk.strip():continue
 h=chunk.splitlines()[0]
 if not h.startswith('#'):continue
 title=h.lstrip('#').strip()
 if h.startswith('# Stage '):
  aid='stage-'+('1' if 'Stage 1' in h else '2')
  cls='stage'; attr=''
 elif h.startswith('## Chapter '):
  num=re.match(r'## Chapter (\d+)',h).group(1);aid='chapter-'+num;cls='';attr=' data-chapter="true"'
 else:
  counter+=1;aid='section-'+str(counter);cls='';attr=''
 html=md(chunk)
 html=re.sub(r'<p>\{\{([a-zA-Z0-9_-]+)\}\}</p>',r'<div data-widget="\1"></div>',html)
 # Mistune sometimes joins markers on one line into same paragraph.
 html=re.sub(r'\{\{([a-zA-Z0-9_-]+)\}\}',r'<div data-widget="\1"></div>',html)
 html=html.replace('<table>','<div class="tablewrap"><table>').replace('</table>','</table></div>')
 articles.append(f'<article id="{aid}"{attr}>{html}</article>')
 if not h.startswith('# Robotics,'):
  nav.append(f'<a href="#{aid}" class="{cls}">{title}</a>')
page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Tejeel Innovations LLP robotics learning portal: electronics, mechanics, Arduino, ESP32, projects and interactive laboratories."><title>Tejeel Robotics Academy | Stages 1 &amp; 2</title><link rel="stylesheet" href="style.css"></head><body><header class="top"><button id="menu" class="mobileMenu" aria-label="Open course navigation" aria-expanded="false">☰</button><div class="brand">TEJEEL INNOVATIONS LLP<small>ROBOTICS ACADEMY</small></div><div class="spacer"></div><input id="search" type="search" aria-label="Search course" placeholder="Search course…"><button id="theme">Dark</button><button id="print">Print</button></header><div class="shell"><aside><h2>Course contents</h2><nav aria-label="Course contents">'''+''.join(nav)+'''</nav><div class="sideprogress"><div id="chapterCount"></div><div class="progress"><span id="chapterBar"></span></div></div></aside><main><section class="hero"><div class="eyebrow">Interactive engineering handbook · Foundation &amp; application</div><h1>Learn robotics from first principles.</h1><p>Electronics, mechanisms, embedded programming, wireless robotics and IoT — a practical learning pathway for students and instructors.</p><div class="stats"><div><b>80</b><small>Guided hours</small></div><div><b>10</b><small>Chapters</small></div><div><b>33</b><small>Activities</small></div><div><b>15</b><small>Quiz questions</small></div></div><a href="#chapter-1">Start learning ↓</a></section><div id="searchstatus" aria-live="polite"></div>'''+''.join(articles)+'''<footer>TEJEEL INNOVATIONS LLP · Robotics Explorer &amp; Robotics Maker<br>Educational simulations · Verify hardware specifications before laboratory use.</footer></main></div><script src="app.js"></script></body></html>'''
soup=BeautifulSoup(page,'html.parser')
# normalize widget divs outside invalid paragraph markup
for p in soup.find_all('p'):
 ds=p.find_all('div',attrs={'data-widget':True},recursive=False)
 if ds and not p.get_text(strip=True):
  for d in ds:p.insert_before(d.extract())
  p.decompose()
for a in soup.find_all('a',href=True):
 if a['href'].startswith('http'):a['target']='_blank';a['rel']='noopener noreferrer'
page=str(soup)
(root/'index.html').write_text(page)
# Single file offline version with embedded assets and CSS/JS.
standalone=page.replace('<link href="style.css" rel="stylesheet"/>','<style>'+(root/'style.css').read_text()+'</style>').replace('<script src="app.js"></script>','<script>'+(root/'app.js').read_text().replace('</script>','<\\/script>')+'</script>')
for f in (root/'assets').glob('*'):
 if f.is_file(): standalone=standalone.replace('assets/'+f.name,'data:image/jpeg;base64,'+base64.b64encode(f.read_bytes()).decode())
Path('/mnt/data/Tejeel_Robotics_Academy.html').write_text(standalone)
(root/'README.md').write_text('''# Tejeel Robotics Academy\n\nOpen `index.html` in Chrome, Edge or Firefox. No installation, build step, backend or API keys required. All included images and diagrams work offline; reference links require internet. Progress and dark mode are stored locally in each browser.\n\n## Deployment\nUpload `index.html`, `style.css`, `app.js` and the `assets` directory to a GitHub repository. Import it in Vercel, select **Other** as framework, leave build command blank and deploy the repository root. You can also use any static web host.\n\n`content.md` is the editable curriculum source; `build.py` is optional and requires Python, mistune and beautifulsoup4. The included site is already built. The simulations are idealized teaching models, not hardware emulators. Code examples require board-specific wiring and validation. Images are extracted from the supplied course PDF; technical diagrams are original.\n''')
with zipfile.ZipFile('/mnt/data/Tejeel_Robotics_Website.zip','w',zipfile.ZIP_DEFLATED) as z:
 for f in root.rglob('*'):
  if f.is_file():z.write(f,'tejeel-robotics/'+str(f.relative_to(root)))
print('Articles',len(soup.select('article')),'Chapters',len(soup.select('[data-chapter]')),'Widgets',len(soup.select('[data-widget]')),'Code samples',len(soup.select('pre')),'Tables',len(soup.select('table')))
print('Standalone inline?', '<style>' in standalone, '<script>' in standalone, 'src="app.js"' in standalone)
