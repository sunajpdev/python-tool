#! python3
# mapIt.py - コマンドラインやクリップポードに指定した住所の地図を開く

import webbrowser
import sys
import pyperclip
import urllib.parse

if len(sys.argv) > 1:
  # コマンドラインから住所取得する
  address = ' ' . join(sys.argv[1:])
else:
  # クリップポードから住所を取得する
  address = pyperclip.paste()

base_url = 'https://www.google.com/maps/search/'
# 日本語の可能性があるため address エンコードする
url = base_url + urllib.parse.quote(address)
webbrowser.open(url)
