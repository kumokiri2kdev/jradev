import sys

sys.path.append('../')

from jra import parser_top as pr
from jra import parser_odds_top as prot
from jra import parser_odds_kaisai as prok
import urllib.request

parser_top = pr.parser_top()
param_list = parser_top.parse()

if 'odds' in param_list == False:
    print("No odd param")
    sys.exit()

parser_odds_top = prot.parser_odds_top('/JRADB/accessO.html', param_list['odds'])
kaisai_list = parser_odds_top.parse()

param_list_x = []
param_list_x.append(param_list['odds'])
for kaisai in kaisai_list:
    kaisai_place_list = kaisai['kaisai_list']
    for kaisai_place in kaisai_place_list:
        parser_odds_kaisai = prok.parser_odds_kaisai('/JRADB/accessO.html', kaisai_place['param'])
        param_list_x.append(kaisai_place['param'])
        race_list = parser_odds_kaisai.parse()
        for race in race_list:
            if 'win' in race:
                param_list_x.append(race['win'])
            if 'waku' in race:
                param_list_x.append(race['waku'])
            if 'uma' in race:
                param_list_x.append(race['uma'])
            if 'exacta' in race:
                param_list_x.append(race['exacta'])
            if 'wide' in race:
                param_list_x.append(race['wide'])
            if 'trio' in race:
                param_list_x.append(race['trio'])
            if 'trioexacta' in race:
                param_list_x.append(race['trioexacta'])

for param in param_list_x:
    cname = "cname={}".format(param).encode('utf-8')
    request = urllib.request.Request('http://www.jra.go.jp/JRADB/accessO.html', data=cname, method='POST')

    param = param.replace('/','-')
    with urllib.request.urlopen(request) as response:
        response_body = response.read()
        with open("data/" + param,'wb') as wfp:
            wfp.write(response_body)
