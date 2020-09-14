import requests
from bs4 import BeautifulSoup

login_url = "YourServer"
crawling_url = "YourServer/dashboard?mode=events"
session = requests.session()

params = dict()
params['username'] = 'admin'
params['password'] = 'Superscret'

# Login your server
res = session.post(login_url, data = params, verify=False)
res.raise_for_status()

res = session.get(crawling_url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

div = soup.find("div", attrs={"class":"left"})
table = div.find_all("table")[1]

values = table.find_all("td")

print('+------------------------------------------+')
print('|    Web Crawling tool...                  |')
print('|    AKiPS Status Exceptions               |')
print('|    Version 1.0.0                         |')
print('+------------------------------------------+')
print()

idx = 1
for i in range(0, len(values), 3):
    print(f"[{idx}] - {values[i].a.get_text()} : {values[i + 1].string}")
    idx += 1
