import sys

sys.path.append('../')

from jra import parser_top as pr
from jra import parser_race_kaisai as prrk

use_network = True

_parser = prrk.parser_race_kaisai('/JRADB/accessS.html','pw01srl10052018010720180217/97')

if use_network:
    list = _parser.parse()
else:
    args = sys.argv

    if len(args) < 2:
        print("Specify Test File Name")
        sys.exit()

    with open(args[1],'rb') as rfp:
        response_body = rfp.read().decode("'shift_jis'")
        list = _parser.parse_html(response_body)


print(list)