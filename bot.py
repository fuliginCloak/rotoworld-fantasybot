"""

This bot will allow you to search for a player and returns 
the latest blurb from rotoworld:
    Type @sport playername

"""







from telegram.ext import Updater, InlineQueryHandler
from telegram.ext import CommandHandler
from requests_html import HTMLSession
from nfl_player_search import search_nfl
from paths import  extract
from bs4 import  BeautifulSoup
import re
import  requests
import json

def get_url():
    contents = search_nfl()
    return contents.json()

def news(bot,update):

    url = get_url()
    chat_id = update.message.chat_id
    bot.send_news(chat_id=chat_id, news=url)

def main():
    updater = Updater(token='1228218082:AAFkRcCxPNA9xMgTQK59V-7DexOMaveLoKw', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('news', news))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
