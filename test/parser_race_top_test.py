import sys

sys.path.append('../')

from jra import parser_top as pr
from jra import parser_race_top as prrt

_parser = prrt.parser_race_top('/JRADB/accessS.html', 'pw01sli00/AF')
kaisai_list = _parser.parse()

for days in kaisai_list:
  print(days['date'])
  for kaisai in days['kaisai_list']:
    print(kaisai)

