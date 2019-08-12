#! python3
# mapIt.py - コマンドラインやクリップポードに指定した住所の地図を開く

import webbrowser
import sys
import pyperclip
import urllib.parse

# 初期値
site = 'google'
param = ''

# 第一引数がない場合はエラー
if len(sys.argv) < 2:
  print("ERROR: パラメータ不足")
  print("第一引数に調査対象を指定 [map, google, youtube]")
  sys.exit()

if len(sys.argv) > 2:
  # 第一引数をサイトパラメータとして取得
  site = sys.argv[1]

  # コマンドラインから住所取得する
  param = ' ' . join(sys.argv[2:])
else:
  # クリップポードから住所を取得する
  param = pyperclip.paste()

# 第一引数でサイトのURLを変更する
if site == 'map':
  base_url = 'https://www.google.com/maps/search/'
elif site == 'youtube':
  base_url = 'https://www.youtube.com/results?search_query='
elif site == 'google':
  base_url = 'https://www.google.com/search?q='
else:
  base_url = 'https://www.google.com/search?q='

# 日本語の可能性があるため address エンコードする
url = base_url + urllib.parse.quote(param)
webbrowser.open(url)

