import sys

sys.path.append('../')

import urllib.request

from jra import parser_win5_kaisai as prwk
from jra import parser_race_race as prrr
from jra import parser_util as pu

param = 'pw17hde01201104241/18'
#param = 'pw17hde01201105011/75'

while True:
    _parser = prwk.parser_win5_kaisai('/JRADB/access5.html',param)

    kaisai = _parser.parse()

    print(kaisai['date'])

    if 'list' in kaisai:
      for race in kaisai['list']:
        print(race['index'])
        print(race['race']['param'])
        race_parser = prrr.parser_race_race('/JRADB/accessS.html', race['race']['param'])
        race_info = race_parser.parse()
        print(race_info['race']['odds_param'])
        pu.parser_util_cache_contents('accessS.html', race_info['race']['odds_param'])

    if param == None:
        break

    if "next" in kaisai:
        param = kaisai['next']
    else:
        break

    #break


