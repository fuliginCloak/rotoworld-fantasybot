
import sys  
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView,QWebEnginePage as QWebPage
from PyQt5.QtWebEngineWidgets import QWebEngineSettings as QWebSettings
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from bs4 import BeautifulSoup
import urllib.request


class Page(QWebPage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv) 
    QWebPage.__init__(self) 
    self.html = '' 
    self.loadFinished.connect(self._on_load_Finished)  
    self.load(QUrl(url))  
    self.app.exec_()  
  
  def _on_load_Finished(self):  
    self.html = self.toHtml(self.Callable)
    print('Load finished')  

  def Callable(self, html_str):
      self.html = html_str
      self.app.quit()
  
def main():
    page = Page('https://www.rotoworld.com/football/nfl/teams/chi/chicago-bears')  
    soup = BeautifulSoup(page.html, 'html.parser') 
    js_test = soup.find('p', _class = 'player-news-article__summary')
    print(js_test.text)

if __name__ == '__main__':
    main()

# bears = Render()
# bears._loadFinished