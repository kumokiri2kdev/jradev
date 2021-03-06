import sys

sys.path.append('../')

from jra import parser_odds_waku as waku

use_network = True

_parser = waku.parser_odds_waku('/JRADB/accessO.html', 'pw153ouS309201704071120170924Z/4A')

if use_network:
   odds_info =  _parser.parse()
else:
    args = sys.argv

    if len(args) < 2:
        print("Specify Test File Name")
        sys.exit()

    with open(args[1],'rb') as rfp:
        response_body = rfp.read().decode("'shift_jis'")
        odds_info = _parser.parse_html(response_body)

waku_list =  odds_info['odds']

for waku in waku_list:
    print("枠番 : {}".format(waku['number']))
    for matrix in waku['matrix']:
        if 'odds' in matrix:
            print(" - {} : {}".format(matrix['number'], matrix['odds']))
        else:
            print(" - {} : 発売なし".format(matrix['number']))