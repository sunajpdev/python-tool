import requests

url = "https://automatetheboringstuff.com/files/rj.txt"
res = requests.get(url)
res.raise_for_status()
play_file = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
  play_file.write(chunk)

play_file.close()
