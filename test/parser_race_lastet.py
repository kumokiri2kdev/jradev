import sys

sys.path.append('../')

from jra import parser_top as pr
from jra import parser_race_top as prrt
from jra import parser_race_kaisai as prrk
from jra import parser_race_race as prrr

_parser = prrt.parser_race_top('/JRADB/accessS.html', 'pw01sli00/AF')
kaisai_list = _parser.parse()

for days in kaisai_list:
  #print(days['date'])
  for kaisai in days['kaisai_list']:
    k_parser = prrk.parser_race_kaisai('/JRADB/accessS.html',kaisai['param'])
    races = k_parser.parse()
    print(races)
    for race in races['race_list']:
      r_parser = prrr.parser_race_race('/JRADB/accessS.html', race['param'])
      race_json = r_parser.parse()
      print(race_json)


