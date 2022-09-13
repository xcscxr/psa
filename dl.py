import base64
import re
import time
import requests
from bs4 import BeautifulSoup


url = 'https://psa.pm/exit/d131b9c1f9cb281390cad99fe6b8cb6f/meBhW5x8PH6BemidHPgl4G3uMujdl0cTkOdRu3j3zJDlbsgWMhhKL05gHzsvnx64MSV0WuetpAQdjguU0sgtUhgmrUb0b3i98PCi3usyeiyy9D86gmKk6scex5bPciAM:SGZlajBGRDBVMEpib3F5aU1OaXozZz09:Hfej0FD0U0JboqyiMNiz3mVkZTk3ZDcwZjU1ZjQ2M2I1Mzk2MWRhOGQ0NjRjOGMx'


# --------------------------------------

client = requests.Session()
h = {
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}
res = client.get(url, cookies={}, headers=h)

url = 'https://try2link.com/'+re.findall('try2link\.com\/(.*?) ', res.text)[0]

res = client.head(url)

id = re.findall('d=(.*?)&', res.headers['location'])[0]
id = base64.b64decode(id).decode('utf-8')

url += f'/?d={id}'
res = client.get(url)

bs4 = BeautifulSoup(res.content, 'html.parser')
inputs = bs4.find_all('input')
data = { input.get('name'): input.get('value') for input in inputs }

time.sleep(6.5)
res = client.post(
    'https://try2link.com/links/go',
    headers={
        'referer': url,
        'x-requested-with': 'XMLHttpRequest',
    }, data=data
)
out = res.json()['url'].replace('\/','/')

print(out)
