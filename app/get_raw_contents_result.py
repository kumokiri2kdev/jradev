import sys

sys.path.append('../')

from jra import parser_race_kaisai_past as prkp
from jra import parser_race_params as prp
from jra import parser_race_kaisai as prrk
from jra import parser_util as pu

import os

start = 201803

while start < 201804:
  param = prp.parser_race_params_get_cname(start)
  print(param)
  pu.parser_util_cache_contents('accessS.html',param)
  past_parser = prkp.parser_race_kaisai_past('/JRADB/accessS.html',param)
  kaisai_list = past_parser.parse()

  for kaisai in kaisai_list['kaisai']:
    print(kaisai['param'])
    kaisai_parser = prrk.parser_race_kaisai('/JRADB/accessS.html',kaisai['param'])
    race_list = kaisai_parser.parse()
    for race in race_list['race_list']:
      print(race['param'])
      pu.parser_util_cache_contents('accessS.html', race['param'])

  start += 1
  if (start % 100) % 13 == 0:
    start += 88
