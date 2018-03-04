import sys

sys.path.append('../')

from jra import parser_race_kaisai_past as prkp
from jra import parser_race_params as prp
from jra import parser_race_kaisai as prrk

use_network = True

param = prp.parser_race_params_get_cname(201801)
#print(param)
_parser = prkp.parser_race_kaisai_past('/JRADB/accessS.html',param)

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

for kaisai in list['kaisai']:
  #print(kaisai['param'])
  _parser = prrk.parser_race_kaisai('/JRADB/accessS.html',kaisai['param'])
  race_list = _parser.parse()
  for race in race_list['race_list']:
    print(race['param'])


