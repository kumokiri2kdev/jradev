import sys

sys.path.append('../')

from jra import parser_odds_trio as trio

use_network = False

_parser = trio.parser_odds_trio('/JRADB/accessO.html', 'pw157ouS306201704051120170918Z99/92')

if use_network:
   trio_list =  _parser.parse()
else:
    args = sys.argv

    if len(args) < 2:
        print("Specify Test File Name")
        sys.exit()

    with open(args[1],'rb') as rfp:
        response_body = rfp.read().decode("'shift_jis'")
        trio_list = _parser.parse_html(response_body)

for trio in trio_list:
    print("馬番 : {}".format(trio['number']))
    for matrix in trio['matrix']:
        print(" 馬番 : {}".format(matrix['number']))
        for maxtrix2 in matrix['matrix']:
            print("  馬番 : {}  : {} ".format(maxtrix2['number'], maxtrix2['odds']))
