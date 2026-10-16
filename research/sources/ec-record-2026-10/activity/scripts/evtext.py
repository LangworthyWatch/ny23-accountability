import re,sys
s=open(sys.argv[1]).read()
t=re.sub(r'<(script|style).*?</\1>','',s,flags=re.S); t=re.sub(r'<a[^>]*href="([^"]+)"[^>]*>',r' [\1] ',t); t=re.sub(r'<[^>]+>','\n',t); t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
i=t.find('JavaScript is required'); print(t[i:])
