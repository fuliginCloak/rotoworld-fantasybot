from paths import extract
from nfl_database import nfl_database

import requests
import collections.abc
import json
import itertools


import urllib.request
from urllib.parse import  (
    urlencode, unquote, urlparse, parse_qsl, ParseResult
)

def search_nfl():

    main_url = 'https://www.rotoworld.com/'

    path_value = extract(nfl_database(), 'path')

    player_search = input(str("Player name?")).lower()

    

    if any:
        player_path =  [path for path in path_value if isinstance(path, collections.Iterable) and (player_search in path)]
        player_url_params = {main_url:player_path}

        player_url = urllib.parse.urlencode(player_url_params, doseq=True)

        # removes special url characters, replaces a misplaced = char as a result of parsing, and splits by & for easier viewing 
        abs_player_url = unquote(player_url).replace('=/', '').split(('&'))

        # sort and clean up any duplicates(it happens)
        # abs_player_url.sort()
        abs_clean_player_url = list(abs_player_url for abs_player_url ,_ in itertools.groupby(abs_player_url))
        
        # put url on its own line
        # formated_abs_clean_player_url =  '\n'.join([str(i)for i in abs_clean_player_url])



  
        # print( abs_clean_player_url)
        return abs_clean_player_url


       


    


   





