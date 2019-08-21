import requests
import urllib.parse

from_station = urllib.parse.quote("東京")
to_station = urllib.parse.quote("南大沢")
url = 'https://transit.yahoo.co.jp/search/result?flatlon=&from=' + from_station + '&to=' + to_station
res = requests.get(url)

len(res.text)

print(res.text[:250])