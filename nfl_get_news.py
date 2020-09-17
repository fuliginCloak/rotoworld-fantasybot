from requests_html import HTMLSession
from nfl_player_search import search_nfl
from paths import  extract
from bs4 import  BeautifulSoup

class RotoworldBot():


    def main(self):
        print('Starting session...')
     
         # for urls in url:
       
        session = HTMLSession()

        headers = {
            'x-api-key':'y0fAF1r59s4JQ7kDjxGqx2lGrcM1zxl75JaKI13v',
            'schema': 'htttp'
        }

        
        # for url in search_nfl():
        #     r = session.get(url, headers=headers)
        #     print (r)
        #     print(url)
        url = 'https://secure.quantserve.com/aquant.js?a=p-9eJ8k4iSzux46'
        r = session.get(url, headers=headers)

        # print(r)
            # r.html.render(timeout=30)

        soup = BeautifulSoup(r.text, 'lxml')
        print (soup)
            # yield soup


  
        





attempt1 = RotoworldBot()

attempt1.main()



