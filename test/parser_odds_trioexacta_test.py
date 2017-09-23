import sys

sys.path.append('../')

from jra import parser_odds_trioexacta as trio

use_network = True

_parser = trio.parser_odds_trioexacta('/JRADB/accessO.html', 'pw158ouS309201704071120170924Z/DE')

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

trio_list =  odds_info['odds']

for trio in trio_list:
    print("馬番 : {}".format(trio['number']))
    for matrix in trio['matrix']:
        print(" 馬番 : {}".format(matrix['number']))
        for maxtrix2 in matrix['matrix']:
            print("  馬番 : {}  : {} ".format(maxtrix2['number'], maxtrix2['odds']))
