import sys

sys.path.append('../')

from jra import parser_odds_uma as uma

use_network = True

_parser = uma.parser_odds_uma('/JRADB/accessO.html', 'pw154ouS306201704051220170918Z/59')

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
        if 'odds' in matrix:
            print(" - {} : {}".format(matrix['number'], matrix['odds']))
        else:
            print(" - {} : 発売なし".format(matrix['number']))