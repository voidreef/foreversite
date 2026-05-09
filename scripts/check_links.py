from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urldefrag
from collections import defaultdict

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links=[]
        self.assets=[]
    def handle_starttag(self, tag, attrs):
        d=dict(attrs)
        if tag=='a' and 'href' in d: self.links.append(d['href'])
        if tag=='img' and 'src' in d: self.assets.append(d['src'])

root=Path('.')
hrefs=defaultdict(list)
missing=[]
for f in root.rglob('*.html'):
    if '.git' in f.parts: continue
    p=Parser(); p.feed(f.read_text(encoding='utf-8'))
    for raw in p.links:
        h,_=urldefrag(raw)
        if not h or h.startswith(('http:','https:','mailto:','data:')): continue
        hrefs[h].append(str(f))
        target=(f.parent/h).resolve()
        if not target.exists(): missing.append((str(f),raw,str(target)))
    for raw in p.assets:
        h,_=urldefrag(raw)
        if not h or h.startswith(('http:','https:','data:')): continue
        target=(f.parent/h).resolve()
        if not target.exists(): missing.append((str(f),'IMG '+raw,str(target)))

print('MISSING')
for row in missing: print(' | '.join(row))
print('REPEATED RAW HREFS')
for h,fs in sorted(hrefs.items(), key=lambda kv:(-len(kv[1]),kv[0])):
    if len(fs)>1:
        print(f'{len(fs)} {h} <- '+', '.join(fs))
print(f'checked {sum(1 for _ in root.rglob("*.html"))} html files')
raise SystemExit(1 if missing else 0)
