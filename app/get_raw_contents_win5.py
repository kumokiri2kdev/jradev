import sys
sys.path.append('../')

import urllib.request
from jra import parser_win5_kaisai as prwk
import re


def cache_contents(param):
  cname = "cname={}".format(param).encode('utf-8')
  request = urllib.request.Request('http://www.jra.go.jp/JRADB/access5.html', data=cname, method='POST')

  param = param.replace('/','-')
  with urllib.request.urlopen(request) as response:
    response_body = response.read()
    with open("/Users/seiichikataoka/Documents/development/jra/testdata/data/" + param,'wb') as wfp:
      wfp.write(response_body)


param = 'pw17hde01201104241/18'

while True:
    cache_contents(param)
    _parser = prwk.parser_win5_kaisai('/JRADB/access5.html',param)
    param = _parser.parse()
    if param == None:
        break;
