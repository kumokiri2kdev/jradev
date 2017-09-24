import sys

sys.path.append('../')

from jra import parser_odds_exacta as ume

use_network = True

_parser = ume.parser_odds_exacta('/JRADB/accessO.html', 'pw156ouS309201704071120170924Z/D6')

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

uma_list =  odds_info['odds']

for uma in uma_list:
    print("馬番 : {}".format(uma['number']))
    for matrix in uma['matrix']:
        if 'odds' in matrix:
            print(" - {} : {}".format(matrix['number'], matrix['odds']))
        else:
            print(" - {} : 発売なし".format(matrix['number']))