import sys
import json

sys.path.append('../')
from jra import parser as pr
from jra import parser_util as pu
from jra import parser_top as pt
from jra import parser_odds_top as prot
from jra import parser_odds_kaisai as prok
from jra import parser_odds_win as prow

parser_top = pt.parser_top()
param_list = parser_top.parse()

parser_odds_top = prot.parser_odds_top('/JRADB/accessO.html', param_list['odds'])
kaisai_list = parser_odds_top.parse()

print(kaisai_list)

for kaisai in kaisai_list:
    #print("日付 : {}".format(kaisai['date']))
    kaisai_place_list = kaisai['kaisai_list']
    for kaisai_place in kaisai_place_list:
        #print(" - 開催 : {}".format(kaisai_place['kaisai']))
        parser_odds_kaisai = prok.parser_odds_kaisai('/JRADB/accessO.html', kaisai_place['param'])
        race_list = parser_odds_kaisai.parse()
        for race in race_list:
            json_data = {}
            json_data['date'] = pu.parser_util_convert_datestr(kaisai['date'])
            json_data['place'] = kaisai_place['kaisai']
            json_data['no'] = race['no']
            print(race['status'])
            json_data['win'] = []
            #print("  -- {} {}".format(race['no'], race['condition']))
            parser_win = prow.parser_odds_win('/JRADB/accessO.html', race['win'])
            uma_list =  parser_win.parse()
            for uma_data in uma_list:
                uma = {}
                uma['name'] = uma_data['uma']['name']
                uma['sexage'] = uma_data['sexage']
                uma['odds'] = uma_data['odds']
                json_data['win'].append(uma)

            #file_name = 'tmp/test.json'
            file_name = 'tmp/{}{}{}.json'.format(json_data['date'],  json_data['place'],
                    str(json_data['no']).zfill(2))

            print(file_name)
            #with open('tmp/{}{}.json'.format(json_data['date'],  json_data['place'],json_data['no'],'w')) as wfp:
            with open (file_name, 'w') as wfp:
                json.dump(json_data, wfp, ensure_ascii=False)
                
            #print(json.dumps(json_data, ensure_ascii=False))

