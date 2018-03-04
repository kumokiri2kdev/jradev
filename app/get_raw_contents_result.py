import sys

sys.path.append('../')

from jra import parser_race_kaisai_past as prkp
from jra import parser_race_params as prp
from jra import parser_race_kaisai as prrk
import urllib.request

def cache_contents(param):
  cname = "cname={}".format(param).encode('utf-8')
  request = urllib.request.Request('http://www.jra.go.jp/JRADB/accessS.html', data=cname, method='POST')

  param = param.replace('/','-')
  with urllib.request.urlopen(request) as response:
    response_body = response.read()
    with open("/Users/seiichikataoka/Documents/development/jra/testdata/data/" + param,'wb') as wfp:
      wfp.write(response_body)

start = 201501

while start < 201701:
  param = prp.parser_race_params_get_cname(start)
  print(param)
  cache_contents(param)
  past_parser = prkp.parser_race_kaisai_past('/JRADB/accessS.html',param)
  kaisai_list = past_parser.parse()

  for kaisai in kaisai_list['kaisai']:
    print(kaisai['param'])
    cache_contents(kaisai['param'])
    kaisai_parser = prrk.parser_race_kaisai('/JRADB/accessS.html',kaisai['param'])
    race_list = kaisai_parser.parse()
    for race in race_list['race_list']:
      print(race['param'])
      cache_contents(race['param'])

  start += 1
  if (start % 100) % 13 == 0:
    start += 88
