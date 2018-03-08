import sys

sys.path.append('../')

from jra import parser_top as pr
from jra import parser_race_race as prrr

use_network = True
#param = "pw01sde1005201801070120180217/B4"
#param = "pw01sde1005201801070220180217/69"
#param = "pw01sde1005201801071120180217/06"
param = "pw01sde1009201801041020180304/0A"

_parser = prrr.parser_race_race('/JRADB/accessS.html', param)

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

print (list)
