import sys

sys.path.append('../')

from jra import parser_race_kaisai_past as prkp
from jra import parser_race_params as prp
from jra import parser_race_kaisai as prrk
from jra import parser_race_race as prrr

start = 201001

while start < 201804:
  param = prp.parser_race_params_get_cname(start)
  print(param)
  past_parser = prkp.parser_race_kaisai_past('/JRADB/accessS.html',param)
  kaisai_list = past_parser.parse()

  for kaisai in kaisai_list['kaisai']:
    print(kaisai['param'])
    kaisai_parser = prrk.parser_race_kaisai('/JRADB/accessS.html',kaisai['param'])
    race_list = kaisai_parser.parse()
    for race in race_list['race_list']:
      race_parser = prrr.parser_race_race('/JRADB/accessS.html', race['param'])
      race_info = race_parser.parse()
      print(race_info)

  start += 1
  if (start % 100) % 13 == 0:
    start += 88
