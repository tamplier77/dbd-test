from urllib.request import urlopen
import time
print("waiting 10 secs...")
time.sleep(5)
content = urlopen('http://localhost:5000/').read().decode("utf-8")
if content == "OK":
    print("OK")
    exit(0)
else:
    print("Failed")
    exit(1)

