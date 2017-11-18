from urllib.request import urlopen
import time
print("waiting 10 secs...")
time.sleep(10)
content = urlopen('http://localhost:5000/').read()
if content == "Looks OK.":
    exit(0)
else:
    exit(1)
