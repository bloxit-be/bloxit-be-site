"""Build a dependency-free bilingual static website for GitHub Pages."""
from pathlib import Path
from html import escape
import os, json, shutil
ROOT = Path(__file__).parent
OUT = ROOT / '_site'
BASE = os.environ.get('SITE_URL', 'https://bloxit-be.github.io/bloxit-be-site').rstrip('/')
DATA = {
'en': {
 'title':'Blox-It | Software engineering, DevOps & AI integration',
 'description':'Freelance Java engineering, DevOps and practical AI integration. Blox-It connects your software, agents and workflows. Based in Belgium.',
 'nav':['Expertise','Technology','Our approach','Contact'],
 'eyebrow':'INDEPENDENT EXPERTISE. CONNECTED THINKING.',
 'headline':'Solid engineering.<br><span>Intelligent connections.</span>',
 'intro':'We build software, strengthen engineering teams and connect AI to the way your business works. From Java and DevOps to agents, MCP and automation.',
 'cta':"Let’s talk",'explore':'Explore our expertise','location':'Based in Belgium · Working with your team',
 'diagram':['SOFTWARE','INTELLIGENCE','CONNECTED BY DESIGN','BUILD','CONNECT','OPERATE'],
 'strip':['Java & Spring Boot','DevOps & cloud','AI agents & MCP','APIs & automation'],
 'expertLabel':'01 / WHAT WE DO','expertTitle':'Engineering depth.<br>A practical AI mindset.',
 'expertIntro':'Hands-on freelance expertise for your team. Focused implementation for your next challenge.',
 'cards':[
 ('01','Java & software engineering','Reliable foundations for software that needs to last. We join your team to build backend services, evolve existing applications and make complex integrations manageable.',['Java','Spring Boot','REST APIs','Event-driven architecture']),
 ('02','AI agents & integrations','Move AI into your daily operations. We connect models to your tools and knowledge, build agents with clear boundaries and make their actions observable.',['OpenAI','Anthropic','Hermes agents','MCP','RAG']),
 ('03','DevOps & cloud','A clear path from code to production. We help streamline delivery, containerise applications and make deployments repeatable and easier to operate.',['Docker','CI/CD','Cloud','Observability']),
 ('04','Workflow automation','Less copying, chasing and repetitive work. We connect applications and automate the handovers between systems, with custom code where it adds value.',['n8n','Make.com','Webhooks','API integrations'])],
 'focusLabel':'BUILT INTO YOUR BUSINESS','focusTitle':'AI is useful when<br>it connects.',
 'focusText':'An agent needs more than a model. It needs the right context, access to the right tools and a reliable way to act. We bring those pieces together with the engineering to support them.',
 'focusItems':[('Context','Connect relevant documents, knowledge and business data.'),('Tools','Give agents controlled access through APIs and MCP.'),('Control','Keep approvals, permissions and monitoring in the design.')],
 'techLabel':'02 / OUR TOOLBOX','techTitle':'The right tools.<br>For your real-world stack.',
 'techIntro':'We work with your existing environment and choose what fits the problem. Modern where it helps. Straightforward where it can be.',
 'techGroups':['ENGINEERING','AI & AGENTS','DELIVERY & AUTOMATION'],
 'approachLabel':'03 / HOW WE WORK','approachTitle':'Part of your team.<br>Focused on the outcome.',
 'approachText':'Blox-It is an independent Belgian engineering company. We combine freelance development and DevOps expertise with a growing focus on practical AI. Direct communication, thoughtful technical decisions and code your team can keep building on.',
 'steps':[('Understand','Start with your systems, constraints and the work that needs to get done.'),('Build & connect','Deliver in useful increments, with feedback from the people who will use it.'),('Make it maintainable','Include documentation, deployment and a clear handover from the start.')],
 'contactLabel':'HAVE SOMETHING IN MIND?','contactTitle':'Let’s connect<br>the next piece.',
 'contactText':'Need extra engineering expertise, a reliable integration or a practical starting point with AI? Tell us what you are working on.',
 'emailLabel':'Email us','callLabel':'Or give us a call','legal':'Company information & privacy','rights':'All rights reserved.','skip':'Skip to content','home':'Home','legalTitle':'Company information & privacy',
 'registered':'Registered office','companyNumber':'Enterprise number','vat':'VAT number','registry':'Register of legal entities','country':'Belgium',
 'privacyTitle':'Privacy, in plain language',
 'privacy':[
 ('Who is responsible?','blox-it BV is responsible for the personal information you share with us directly. For privacy questions or requests, email info@bloxit.be or write to our registered office.'),
 ('Visiting this website','This website has no contact form, account system, analytics or advertising trackers. We do not set cookies or save your language choice on your device. On the English homepage, your browser language may select Dutch; the language switch always lets you choose explicitly.'),
 ('Hosting','This website is hosted on GitHub Pages. GitHub processes technical information, including IP addresses, to deliver and secure the service. Hosting data is handled according to GitHub’s privacy statement, including its provisions for international transfers and retention.'),
 ('Contacting us','If you email or call us, we process your contact details and the information you provide to answer your enquiry, discuss an assignment or manage our business relationship. The legal basis is taking steps at your request before a contract, performing a contract, or our legitimate interest in responding to business enquiries. Legal obligations may require retention of business records.'),
 ('Access and retention','Information is accessible to those who need it to handle your enquiry and to service providers supporting our email and business administration. We do not sell your information. We keep correspondence only for as long as needed for the enquiry or relationship, and longer where a legal retention duty or the establishment, exercise or defence of legal claims requires it.'),
 ('Your rights','You may request access, correction, erasure, restriction or portability of your personal information, where applicable, and object to processing based on legitimate interests. Contact info@bloxit.be. You may also lodge a complaint with the Belgian Data Protection Authority.'),
 ],'githubPrivacy':'GitHub privacy statement','authority':'Belgian Data Protection Authority','updated':'Last updated: 21 September 2026',
},
'nl': {
 'title':'Blox-It | Softwareontwikkeling, DevOps & AI-integratie',
 'description':'Freelance Javaontwikkeling, DevOps en praktische AI-integratie. Blox-It verbindt software, agents en workflows. Vanuit België.',
 'nav':['Expertise','Technologie','Onze aanpak','Contact'],
 'eyebrow':'ONAFHANKELIJKE EXPERTISE. VERBONDEN DENKEN.',
 'headline':'Sterke software.<br><span>Slimme verbindingen.</span>',
 'intro':'We bouwen software, versterken developmentteams en verbinden AI met de werking van je bedrijf. Van Java en DevOps tot agents, MCP en automatisatie.',
 'cta':'Laten we kennismaken','explore':'Ontdek onze expertise','location':'Vanuit België · Samen met jouw team',
 'diagram':['SOFTWARE','INTELLIGENTIE','ONTWORPEN OM TE VERBINDEN','BOUWEN','VERBINDEN','BEHEREN'],
 'strip':['Java & Spring Boot','DevOps & cloud','AI-agents & MCP','API’s & automatisatie'],
 'expertLabel':'01 / ONZE EXPERTISE','expertTitle':'Technische diepgang.<br>Een praktische kijk op AI.',
 'expertIntro':'Freelance expertise die meewerkt in jouw team. Gerichte uitvoering voor je volgende uitdaging.',
 'cards':[
 ('01','Java & softwareontwikkeling','Een betrouwbare basis voor software die moet meegaan. We versterken je team, bouwen backenddiensten, ontwikkelen bestaande applicaties verder en maken complexe integraties beheersbaar.',['Java','Spring Boot','REST API’s','Event-driven architectuur']),
 ('02','AI-agents & integraties','Geef AI een plek in je dagelijkse werking. We verbinden modellen met je tools en kennis, bouwen agents met duidelijke grenzen en maken hun acties inzichtelijk.',['OpenAI','Anthropic','Hermes agents','MCP','RAG']),
 ('03','DevOps & cloud','Een helder traject van code naar productie. We verbeteren je ontwikkelproces, brengen applicaties in containers en maken deployments herhaalbaar en eenvoudiger te beheren.',['Docker','CI/CD','Cloud','Observability']),
 ('04','Workflowautomatisatie','Minder kopiëren, opvolgen en herhalen. We koppelen applicaties en automatiseren de overdracht tussen systemen, met maatwerkcode waar die waarde toevoegt.',['n8n','Make.com','Webhooks','API-integraties'])],
 'focusLabel':'VERWEVEN MET JE WERKING','focusTitle':'AI wordt nuttig<br>als het verbindt.',
 'focusText':'Een agent heeft meer nodig dan een model. De juiste context, toegang tot de juiste tools en een betrouwbare manier om acties uit te voeren. We brengen die onderdelen samen met de techniek die ze ondersteunt.',
 'focusItems':[('Context','Verbind relevante documenten, kennis en bedrijfsgegevens.'),('Tools','Geef agents gecontroleerde toegang via API’s en MCP.'),('Controle','Neem goedkeuringen, toegangsrechten en monitoring mee in het ontwerp.')],
 'techLabel':'02 / ONZE TOOLBOX','techTitle':'De juiste tools.<br>Voor jouw omgeving.',
 'techIntro':'We werken met je bestaande omgeving en kiezen wat bij het probleem past. Modern waar het helpt. Eenvoudig waar het kan.',
 'techGroups':['DEVELOPMENT','AI & AGENTS','DELIVERY & AUTOMATISATIE'],
 'approachLabel':'03 / ONZE AANPAK','approachTitle':'Deel van jouw team.<br>Gericht op resultaat.',
 'approachText':'Blox-It is een onafhankelijk Belgisch IT-bedrijf. We combineren freelance development en DevOps met een groeiende focus op praktische AI. Met rechtstreeks contact, doordachte technische keuzes en code waarop je team kan voortbouwen.',
 'steps':[('Begrijpen','We starten bij je systemen, randvoorwaarden en het werk dat moet gebeuren.'),('Bouwen & verbinden','We leveren in bruikbare stappen, met feedback van de mensen die ermee werken.'),('Onderhoudbaar maken','Documentatie, deployment en een heldere overdracht zitten van bij de start in de aanpak.')],
 'contactLabel':'EEN VRAAG OF IDEE?','contactTitle':'Samen de volgende<br>verbinding leggen.',
 'contactText':'Extra technische expertise nodig, een betrouwbare koppeling of een praktisch vertrekpunt met AI? Vertel ons waaraan je werkt.',
 'emailLabel':'Mail ons','callLabel':'Of bel ons even','legal':'Bedrijfsgegevens & privacy','rights':'Alle rechten voorbehouden.','skip':'Ga naar de inhoud','home':'Home','legalTitle':'Bedrijfsgegevens & privacy',
 'registered':'Maatschappelijke zetel','companyNumber':'Ondernemingsnummer','vat':'Btw-nummer','registry':'Rechtspersonenregister','country':'België',
 'privacyTitle':'Privacy, helder uitgelegd',
 'privacy':[
 ('Wie is verantwoordelijk?','blox-it BV is verantwoordelijk voor de persoonsgegevens die je rechtstreeks met ons deelt. Voor privacyvragen of verzoeken kun je mailen naar info@bloxit.be of schrijven naar onze maatschappelijke zetel.'),
 ('Deze website bezoeken','Deze website heeft geen contactformulier, accounts, analytics of advertentietrackers. We plaatsen geen cookies en slaan je taalkeuze niet op je toestel op. Op de Engelse homepage kan je browsertaal Nederlands selecteren; via de taalwissel kun je altijd zelf kiezen.'),
 ('Hosting','Deze website wordt gehost op GitHub Pages. GitHub verwerkt technische gegevens, waaronder IP-adressen, om de dienst te leveren en te beveiligen. Daarop is de privacyverklaring van GitHub van toepassing, inclusief de bepalingen over internationale doorgiften en bewaartermijnen.'),
 ('Contact opnemen','Als je ons mailt of belt, verwerken we je contactgegevens en de informatie die je verstrekt om je vraag te beantwoorden, een opdracht te bespreken of onze zakelijke relatie te beheren. De rechtsgrond is het nemen van stappen op jouw verzoek vóór een overeenkomst, de uitvoering van een overeenkomst of ons gerechtvaardigd belang om zakelijke vragen te beantwoorden. Wettelijke verplichtingen kunnen het bewaren van zakelijke documenten vereisen.'),
 ('Toegang en bewaring','Gegevens zijn toegankelijk voor wie ze nodig heeft om je vraag te behandelen en voor dienstverleners die onze e-mail en bedrijfsadministratie ondersteunen. We verkopen je gegevens niet. We bewaren correspondentie zolang nodig voor de vraag of relatie, en langer als een wettelijke bewaarplicht of de vaststelling, uitoefening of verdediging van rechtsvorderingen dit vereist.'),
 ('Je rechten','Je kunt waar toepasselijk inzage, verbetering, verwijdering, beperking of overdracht van je persoonsgegevens vragen en bezwaar maken tegen verwerking op grond van gerechtvaardigd belang. Contacteer info@bloxit.be. Je kunt ook een klacht indienen bij de Belgische Gegevensbeschermingsautoriteit.'),
 ],'githubPrivacy':'Privacyverklaring van GitHub','authority':'Belgische Gegevensbeschermingsautoriteit','updated':'Laatst bijgewerkt: 21 september 2026',
}}

def tags(items): return ''.join(f'<span>{escape(x)}</span>' for x in items)
def page(lang, legal=False):
 d=DATA[lang]; p='../' if lang=='nl' else './'; home='./index.html?lang='+lang
 canonical=BASE+('/nl' if lang=='nl' else '')+('/legal.html' if legal else '/')
 en=p+('legal.html' if legal else 'index.html?lang=en'); nl=p+'nl/'+('legal.html' if legal else 'index.html')
 nav=''.join(f'<a href="{home if legal else ""}#{id}">{label}</a>' for id,label in zip(['expertise','technology','approach','contact'],d['nav']))
 schema={'@context':'https://schema.org','@type':'Organization','name':'Blox-It','legalName':'blox-it BV','url':BASE+'/','email':'info@bloxit.be','telephone':'+32485606840','vatID':'BE0730696050','address':{'@type':'PostalAddress','streetAddress':'Terwestvaart 11','postalCode':'9180','addressLocality':'Lokeren','addressCountry':'BE'}}
 start=f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(d['legalTitle']+' | Blox-It' if legal else d['title'])}</title><meta name="description" content="{escape(d['description'],quote=True)}"><meta name="theme-color" content="#081426"><link rel="canonical" href="{canonical}"><link rel="alternate" hreflang="en" href="{BASE+('/legal.html' if legal else '/')}"><link rel="alternate" hreflang="nl" href="{BASE+'/nl/'+('legal.html' if legal else '')}"><link rel="alternate" hreflang="x-default" href="{BASE+('/legal.html' if legal else '/')}"><meta property="og:title" content="{escape(d['title'])}"><meta property="og:description" content="{escape(d['description'],quote=True)}"><meta property="og:type" content="website"><meta property="og:url" content="{canonical}"><meta property="og:locale" content="{'nl_BE' if lang=='nl' else 'en_GB'}"><meta property="og:image" content="{BASE}/assets/logo.png"><link rel="icon" href="{p}assets/logo.png" type="image/png"><link rel="stylesheet" href="{p}assets/style.css"><script defer src="{p}assets/site.js"></script><script type="application/ld+json">{json.dumps(schema)}</script></head><body{' data-auto-language="true"' if lang=='en' and not legal else ''}><a class="skip" href="#main">{d['skip']}</a><header><div class="wrap header-inner"><a class="brand" href="{home}" aria-label="Blox-It {d['home']}"><img src="{p}assets/logo.png" width="76" height="94" alt="Blox-It Software Solutions"></a><nav aria-label="{'Hoofdnavigatie' if lang=='nl' else 'Main navigation'}">{nav}</nav><div class="languages" aria-label="Language / Taal"><a lang="en" hreflang="en" href="{en}" {'aria-current="true"' if lang=='en' else ''}>EN</a><span>/</span><a lang="nl" hreflang="nl" href="{nl}" {'aria-current="true"' if lang=='nl' else ''}>NL</a></div></div></header>'''
 footer=f'''<footer><div class="wrap footer-top"><a class="footer-brand" href="{home}">BLOX<span>·</span>IT</a><p>blox-it BV<br>Terwestvaart 11 · 9180 Lokeren · {d['country']}</p><p>{d['companyNumber']}: 0730.696.050<br>{d['vat']}: BE 0730.696.050<br>RPR Gent, afdeling Dendermonde</p></div><div class="wrap footer-bottom"><span>© <span data-year>2026</span> Blox-It. {d['rights']}</span><a href="./legal.html">{d['legal']}</a></div></footer></body></html>'''
 if legal:
  sections=''.join(f'<section><h2>{h}</h2><p>{t}</p></section>' for h,t in d['privacy'])
  return start+f'''<main id="main" class="wrap legal"><a class="back" href="{home}">← {d['home']}</a><h1>{d['legalTitle']}</h1><dl><dt>{'Company' if lang=='en' else 'Onderneming'}</dt><dd>blox-it BV</dd><dt>{d['registered']}</dt><dd>Terwestvaart 11, 9180 Lokeren, {d['country']}</dd><dt>{d['companyNumber']}</dt><dd>0730.696.050</dd><dt>{d['vat']}</dt><dd>BE 0730.696.050</dd><dt>{d['registry']}</dt><dd>RPR Gent, afdeling Dendermonde</dd><dt>Email</dt><dd><a href="mailto:info@bloxit.be">info@bloxit.be</a></dd><dt>{'Phone' if lang=='en' else 'Telefoon'}</dt><dd><a href="tel:+32485606840">+32 485 60 68 40</a></dd></dl><h2 class="privacy-heading">{d['privacyTitle']}</h2>{sections}<p><a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">{d['githubPrivacy']} ↗</a><br><a href="https://www.gegevensbeschermingsautoriteit.be/burger">{d['authority']} ↗</a></p><p class="small">{d['updated']}</p></main>'''+footer
 cards=''.join(f'<article class="service service-{i}"><div class="card-top"><span class="number">{n}</span><span class="card-icon" aria-hidden="true">{icon}</span></div><h3>{h}</h3><p>{t}</p><div class="tags">{tags(ts)}</div></article>' for i,((n,h,t,ts),icon) in enumerate(zip(d['cards'],['&lt;/&gt;','✳','↗','⇄'])))
 focus=''.join(f'<li><span class="check" aria-hidden="true">↗</span><div><h3>{h}</h3><p>{t}</p></div></li>' for h,t in d['focusItems'])
 tech=[['Java','Spring Boot','REST APIs','Event-driven systems','Frontend development'],['OpenAI','Anthropic','Hermes agents','MCP','RAG','Tool calling'],['Docker','CI/CD','Cloud','n8n','Make.com','Webhooks']]
 techhtml=''.join(f'<div class="tech-row"><h3>{h}</h3><div>{tags(ts)}</div></div>' for h,ts in zip(d['techGroups'],tech))
 steps=''.join(f'<li><span>0{i+1}</span><div><h3>{h}</h3><p>{t}</p></div></li>' for i,(h,t) in enumerate(d['steps']))
 graphic=f'''<div class="connection-art" aria-hidden="true"><div class="art-label"><span class="status-dot"></span>{d['diagram'][2]}</div><svg class="wiring" viewBox="0 0 480 380" fill="none"><path class="wire" d="M0 90H110L195 175H240M480 90H360L275 175H240M0 290H110L195 205H240M480 290H360L275 205H240M240 0V140M240 380V240"/><circle cx="110" cy="90" r="5"/><circle cx="360" cy="90" r="5"/><circle cx="110" cy="290" r="5"/><circle cx="360" cy="290" r="5"/><circle cx="240" cy="52" r="5"/><circle cx="240" cy="328" r="5"/></svg><div class="orbit orbit-one"></div><div class="orbit orbit-two"></div><div class="node node-java">Java<span>Spring Boot</span></div><div class="node node-ai">AI<span>Agents & MCP</span></div><div class="node node-api">API<span>Integrations</span></div><div class="node node-ops">DevOps<span>Build & deploy</span></div><div class="core"><span>↗</span><small>BLOX·IT</small></div><div class="art-footer"><span>{d['diagram'][3]}</span><b>+</b><span>{d['diagram'][4]}</span><b>+</b><span>{d['diagram'][5]}</span></div></div>'''
 return start+f'''<main id="main"><section class="hero"><div class="wrap hero-grid"><div class="hero-copy"><p class="eyebrow">{d['eyebrow']}</p><h1>{d['headline']}</h1><p class="intro">{d['intro']}</p><div class="hero-actions"><a class="button" href="mailto:info@bloxit.be">{d['cta']} <span aria-hidden="true">↗</span></a><a class="text-link" href="#expertise">{d['explore']} <span aria-hidden="true">↓</span></a></div><p class="location"><span></span>{d['location']}</p></div>{graphic}</div><div class="wrap expertise-strip">{''.join(f'<span>{x}</span>' for x in d['strip'])}</div></section><section id="expertise" class="section wrap"><div class="section-head"><div><p class="eyebrow">{d['expertLabel']}</p><h2>{d['expertTitle']}</h2></div><p>{d['expertIntro']}</p></div><div class="services">{cards}</div></section><section class="focus"><div class="wrap focus-grid"><div><p class="eyebrow">{d['focusLabel']}</p><h2>{d['focusTitle']}</h2><p>{d['focusText']}</p><div class="focus-mark" aria-hidden="true">[ context + tools + control ]</div></div><ul>{focus}</ul></div></section><section id="technology" class="section wrap"><div class="section-head"><div><p class="eyebrow">{d['techLabel']}</p><h2>{d['techTitle']}</h2></div><p>{d['techIntro']}</p></div><div class="toolbox">{techhtml}</div></section><section id="approach" class="approach section"><div class="wrap approach-grid"><div><p class="eyebrow">{d['approachLabel']}</p><h2>{d['approachTitle']}</h2><p>{d['approachText']}</p></div><ol>{steps}</ol></div></section><section id="contact" class="contact"><div class="wrap contact-grid"><div><p class="eyebrow">{d['contactLabel']}</p><h2>{d['contactTitle']}</h2><p>{d['contactText']}</p></div><div class="contact-links"><span>{d['emailLabel']}</span><a class="email" href="mailto:info@bloxit.be">info@bloxit.be <span aria-hidden="true">↗</span></a><span>{d['callLabel']}</span><a class="phone" href="tel:+32485606840">+32 485 60 68 40</a></div></div></section></main>'''+footer

if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir(); (OUT/'nl').mkdir()
shutil.copytree(ROOT/'assets',OUT/'assets')
for lang in DATA:
 folder=OUT/('nl' if lang=='nl' else '')
 (folder/'index.html').write_text(page(lang),encoding='utf-8')
 (folder/'legal.html').write_text(page(lang,True),encoding='utf-8')
(OUT/'.nojekyll').touch()
(OUT/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n')
(OUT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{BASE}{x}</loc></url>' for x in ['/','/nl/','/legal.html','/nl/legal.html'])+'</urlset>')
(OUT/'404.html').write_text(f'<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Page not found | Blox-It</title><style>body{{background:#081426;color:#fff;font:20px system-ui;padding:12vw}}a{{color:#f27676}}</style><h1>This connection is missing.</h1><p>Page not found / Pagina niet gevonden</p><a href="{BASE}/">Back to Blox-It ↗</a></html>')
print('Built EN/NL site in',OUT)
