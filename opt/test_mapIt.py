import unittest
import mapIt
import pyperclip

class TestMapIt(unittest.TestCase):
  def test_argv_enc_string(self):
    argv = ['mapIt.py', 'gmap', 'hogehoge']
    param = mapIt.argv_enc_string(argv)
    expected = "hogehoge"
    self.assertEqual(expected, param)

    # clipbordにコピー
    pyperclip.copy('python')
    argv = ['mapIt.py', 'gmap']
    param = mapIt.argv_enc_string(argv)
    expected = "python"
    self.assertEqual(expected, param)

  def test_sitename(self):
    argv = ['mapIt.py', 'gmap', 'hogehoge']
    site = mapIt.sitename(argv)
    expected = "gmap"
    self.assertEqual(expected, site)

  def test_create_url(self):
    argv = ['mapIt.py', 'gmap', 'hogehoge']
    expected = "https://www.google.com/maps/search/hogehoge"
    url = mapIt.create_url(argv)
    self.assertEqual(expected,url)

    argv = ['mapIt.py', 'youtube', 'hogehoge']
    expected = "https://www.youtube.com/results?search_query=hogehoge"
    url = mapIt.create_url(argv)
    self.assertEqual(expected,url)

    argv = ['mapIt.py', 'ggl', 'hogehoge']
    expected = "https://www.google.com/search?q=hogehoge"
    url = mapIt.create_url(argv)
    self.assertEqual(expected,url)

    argv = ['mapIt.py', 'gphoto', 'hogehoge']
    expected = "https://www.google.com/search?q=hogehoge&tbm=isch"
    url = mapIt.create_url(argv)
    self.assertEqual(expected,url)

    argv = ['mapIt.py', 'trans', 'hogehoge']
    expected = "https://translate.google.com/?hl=ja#view=home&op=translate&sl=auto&tl=en&text=hogehoge"
    url = mapIt.create_url(argv)
    self.assertEqual(expected,url)

    # norkae
    argv = ['mapIt.py', 'norikae', 'a', 'b']
    expected = 'https://transit.yahoo.co.jp/main/top?from=' + argv[2] +'&to=' + argv[3]
    url = mapIt.create_url(argv)
    self.assertEqual(expected,url)

    ## パラメータがない場合はFalse
    argv = ['mapIt.py', 'norikae']
    url = mapIt.create_url(argv)
    self.assertEqual(False,url)

    ## パラメータが１つしかない場合もFalse
    argv = ['mapIt.py', 'norikae', 'a']
    url = mapIt.create_url(argv)
    self.assertEqual(False,url)

    # 引数不足
    argv = ['mapIt.py']
    url = mapIt.create_url(argv)
    self.assertEqual(False, url)

    # clipboard
    argv = ['mapIt.py', 'ggl']
    pyperclip.copy('python')
    expected = "https://www.google.com/search?q=python"
    url = mapIt.create_url(argv)
    self.assertEqual(expected, url)

  # norikae
  def test_create_url_norikae(self):
    argv = ['mapIt.py', 'norikae', 'a', 'b']
    expected = 'https://transit.yahoo.co.jp/main/top?from=' + argv[2] +'&to=' + argv[3]
    url = mapIt.create_url_norikae(argv)
    self.assertEqual(expected, url)

    # 経由地がある場合
    argv = ['mapIt.py', 'norikae', 'a', 'b', 'c']
    expected = 'https://transit.yahoo.co.jp/main/top?from=' + argv[2] +'&to=' + argv[3] + '&via=' + argv[4]
    url = mapIt.create_url_norikae(argv)
    self.assertEqual(expected, url)


  def test_create_url_norikae_vias(self):
    argv = ['mapIt.py', 'norikae', 'a', 'b', 'c']
    expected = "&via=c"
    url = mapIt.create_url_norikae_vias(argv)
    self.assertEqual(expected, url)

    # 経由地２つ
    argv = ['mapIt.py', 'norikae', 'a', 'b', 'c', 'd']
    expected = "&via=c&via=d"
    url = mapIt.create_url_norikae_vias(argv)
    self.assertEqual(expected, url)

if __name__ == "__main__":
  unittest.main()
