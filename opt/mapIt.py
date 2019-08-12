#! python3
# mapIt.py - コマンドラインやクリップポードに指定した住所の地図を開く

import webbrowser, sys

if len(sys.argv) > 1:
  # コマンドラインから住所取得する
  address = ' ' . join(sys.argv[1:])
else:
  # TODO: クリップポードから住所を取得する
  address = pyperclip.paste()

url = 'https://www.google.com/maps/place/' + address
webbrowser.open(url)
