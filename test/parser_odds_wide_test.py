import sys

sys.path.append('../')

from jra import parser_odds_wide as umw

use_network = False

_parser = umw.parser_odds_wide('/JRADB/accessO.html', 'pw155ouS306201704051220170918Z/DD')

if use_network:
   uma_list =  _parser.parse()
else:
    args = sys.argv

    if len(args) < 2:
        print("Specify Test File Name")
        sys.exit()

    with open(args[1],'rb') as rfp:
        response_body = rfp.read().decode("'shift_jis'")
        uma_list = _parser.parse_html(response_body)

for uma in uma_list:
    print("馬番 : {}".format(uma['number']))
    for matrix in uma['matrix']:
        if 'odds_min' in matrix:
            print(" - {} : {} - {}".format(matrix['number'], matrix['odds_min'], matrix['odds_max']))
        else:
            print(" - {} : 発売なし".format(matrix['number']))