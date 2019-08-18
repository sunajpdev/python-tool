import unittest
import mapIt
import pyperclip

class TestMapIt(unittest.TestCase):
  def test_argv_enc_string(self):
    # clipbordにコピー
    pyperclip.copy('python')
    argv = ['mapIt.py', 'gmap', 'hogehoge']
    param = mapIt.argv_enc_string(argv)
    expected = "hogehoge"
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

if __name__ == "__main__":
  unittest.main()
