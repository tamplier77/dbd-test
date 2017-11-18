import urllib2
content = urllib2.urlopen('http://127.0.0.1:5000/').read()
if content == "Looks OK.":
    exit(0)
else:
    exit(1)
