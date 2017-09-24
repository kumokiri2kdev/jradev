import sys

sys.path.append('../')

from jra import parser_odds_wide as umw

use_network = True

_parser = umw.parser_odds_wide('/JRADB/accessO.html', 'pw155ouS309201704071120170924Z/52')

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

if odds_info['fixed'] == True:
    print("最終オッズ")
else:
    print("{} 現在のオッズ()".format(odds_info['timestamp'] ))

for uma in uma_list:
    print("馬番 : {}".format(uma['number']))
    for matrix in uma['matrix']:
        if 'odds_min' in matrix:
            print(" - {} : {} - {}".format(matrix['number'], matrix['odds_min'], matrix['odds_max']))
        else:
            print(" - {} : 発売なし".format(matrix['number']))