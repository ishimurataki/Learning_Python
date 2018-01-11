import re, urllib

import urllib.request

sites = 'google cnn msn'.split()
pat = re.compile(r'<title>+.*</title>+', re.I|re.M)

for s in sites:
    print('Searching: ' + s)
    u = urllib.request.urlopen('http://' + s + '.com')
    text = u.read()
    title = re.findall(pat,str(text))
    print(title[0])

