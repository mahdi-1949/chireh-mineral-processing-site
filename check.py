from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
r=Path(__file__).parent/'dist';errors=[];count=0
class P(HTMLParser):
 def __init__(self,p):super().__init__();self.path=p;self.h1=0;self.refs=[]
 def handle_starttag(self,t,attrs):
  d=dict(attrs)
  if t=='h1':self.h1+=1
  if t=='img' and 'alt' not in d:errors.append((str(self.path),'missing alt'))
  for k in ('src','href'):
   u=d.get(k,'')
   if u.startswith('/') and not u.startswith('//'):self.refs.append(urlsplit(u).path)
for f in r.rglob('*.html'):
 if f.name=='chireh-equipment-catalog.html':continue
 p=P(f);p.feed(f.read_text());count+=1
 if p.h1!=1:errors.append((str(f),'h1 count '+str(p.h1)))
 for u in p.refs:
  path=r/unquote(u).lstrip('/')
  if u.endswith('/'):path=path/'index.html'
  if not path.exists():errors.append((str(f.relative_to(r)),u))
print('Checked',count,'HTML documents; errors:',len(errors))
for e in errors:print(e)
assert not errors
