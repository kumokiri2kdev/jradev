import sys

sys.path.append('../')

from jra import parser_odds_waku as waku

use_network = False

_parser = waku.parser_odds_waku('/JRADB/accessO.html', 'pw153ouS306201704051120170918Z/20')

if use_network:
   waku_list =  _parser.parse()
else:
    args = sys.argv

    if len(args) < 2:
        print("Specify Test File Name")
        sys.exit()

    with open(args[1],'rb') as rfp:
        response_body = rfp.read().decode("'shift_jis'")
        waku_list = _parser.parse_html(response_body)

for waku in waku_list:
    print("枠番 : {}".format(waku['waku']))
    for matrix in waku['matrix']:
        if 'odds' in matrix:
            print(" - {} : {}".format(matrix['waku'], matrix['odds']))
        else:
            print(" - {} : 発売なし".format(matrix['waku']))