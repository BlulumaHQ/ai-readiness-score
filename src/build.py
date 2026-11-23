import base64,re
src=open('/home/claude/ai-readiness-score/src/src.html').read()
a=src.index('const P=['); b=src.index('let S={')
data=src[a:b]
assert 'const ALL=' in data and 'const HRS' in data
s=open('/home/claude/ai-readiness-score/src/v3.html').read().replace('/*DATA*/',data)
d='/home/claude/src/bluluma-design/public/images/'
e=lambda f:'data:image/svg+xml;base64,'+base64.b64encode(open(d+f,'rb').read()).decode()
s=s.replace('{{LOGO}}',e('bluluma-logo.svg')).replace('{{LOGOW}}',e('bluluma-logo-white.svg'))
open('/home/claude/ai-readiness-score/public/index.html','w').write(s)
open('/tmp/t.js','w').write(re.findall(r'<script>(.*?)</script>',s,re.S)[-1])
