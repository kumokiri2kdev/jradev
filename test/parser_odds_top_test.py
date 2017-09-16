import sys

sys.path.append('../')

from jra import parser_top as pr
from jra import parser_odds_top as prot
from jra import parser_odds_kaisai as prok
from jra import parser_odds_win as prow

use_network = True

_parser = prot.parser_odds_top('/JRADB/accessO.html', 'pw15oli00/6D')

if use_network:
    kaisai_list = _parser.parse()
else:
    args = sys.argv

    if len(args) < 2:
        print("Specify Test File Name")
        sys.exit()

    with open(args[1],'rb') as rfp:
        response_body = rfp.read().decode("'shift_jis'")
        kaisai_list = _parser.parse_html(response_body)

for date in kaisai_list:
    print("日付: {}".format(date['date']))
    for kaisai in date['kaisai_list']:
        print(" 開催 : {}".format(kaisai['kaisai']))
        print(" Param : {}".format(kaisai['param']))