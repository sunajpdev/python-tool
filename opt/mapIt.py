#!/usr/bin/env python3
# mapIt.py - コマンドラインやクリップポードに指定した住所の地図を開く

import webbrowser
import sys
import pyperclip
import urllib.parse

# # 乗換案内 start: 開始駅 to:到着駅 
# def norikae(start, to):
#   return 'https://transit.yahoo.co.jp/main/top?from=' + start +'&to=' + to

# サイトごとにURLとパラメータをセットした文字列を返す
def create_url(argv):
  site = sitename(argv)
  # 検索パラメータ取得
  param = argv_enc_string(argv)

  # 第一引数でサイトのURLを変更する
  if site == 'gmap':
    url = 'https://www.google.com/maps/search/'+ param
  elif site == 'youtube':
    url = 'https://www.youtube.com/results?search_query=' + param
  elif site == 'ggl':
    url = 'https://www.google.com/search?q=' + param
  elif site == 'gphoto':
    url = 'https://www.google.com/search?q=' + param + '&tbm=isch'
  elif site == 'trans':
    url = "https://translate.google.com/?hl=ja#view=home&op=translate&sl=auto&tl=en&text=" + param
  else:
    print('ERROR: Site Not Found')
    return False

  return url

# パラメータより検索先サイトを返す。ない場合はFalseを返す
def sitename(argv):
  # 第一引数がない場合はエラー
  if len(argv) < 2:
    print("ERROR: パラメータ不足")
    return False
  else:
    return argv[1]

# パラメータの第二パラメータ以降、ない場合はクリップボードから検索用文字列を返す
def argv_enc_string(argv):
  if len(argv) > 2:
    # 第一引数をサイトパラメータとして取得
    site = argv[1]  
    # コマンドラインから住所取得する
    param = ' ' . join(argv[2:])
  else:
    # クリップポードから住所を取得する
    param = pyperclip.paste()

  # 日本語の可能性があるため address エンコードする  
  param = urllib.parse.quote(param)
  return param


if __name__ == "__main__":
  # urlを生成
  url = create_url(sys.argv)
  if url != False:
    webbrowser.open(url)
  else:
    print('false')    
