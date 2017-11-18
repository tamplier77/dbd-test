from urllib.request import urlopen
content = urlopen('http://localhost:5000/').read()
if content == "Looks OK.":
    exit(0)
else:
    exit(1)
