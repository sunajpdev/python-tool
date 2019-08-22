import requests
import urllib.parse

from_station = urllib.parse.quote("東京")
to_station = urllib.parse.quote("南大沢")
url = 'https://transit.yahoo.co.jp/search/result?flatlon=&from=' + from_station + '&to=' + to_station
res = requests.get(url)
res.raise_for_status()

print(res.test[:250])
len(res.text)


