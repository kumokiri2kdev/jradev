import sys

sys.path.append('../')

from jra import parser_top as pr
from jra import parser_race_race as prrr

use_network = True

_parser = prrr.parser_race_race('/JRADB/accessS.html','pw01sde1005201801071120180217/06')

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

