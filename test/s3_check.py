import sys
import json

sys.path.append('../')

from jra import parser_util as pu
from jra import parser_top as pr
from jra import parser_odds_top as prot
from jra import parser_odds_kaisai as prok
from jra import parser_odds_win as prow

parser_top = pr.parser_top()
param_list = parser_top.parse()

parser_odds_top = prot.parser_odds_top('/JRADB/accessO.html', param_list['odds'])
kaisai_list = parser_odds_top.parse()

for kaisai in kaisai_list:
    #print("日付 : {}".format(kaisai['date']))
    date = pu.parser_util_convert_datestr(kaisai['date'])

    kaisai_place_list = kaisai['kaisai_list']
    for kaisai_place in kaisai_place_list:
        #print(" - 開催 : {}".format(kaisai_place['kaisai']))
        parser_odds_kaisai = prok.parser_odds_kaisai('/JRADB/accessO.html', kaisai_place['param'])
        race_list = parser_odds_kaisai.parse()
        for race in race_list:
            json_data = {}
            json_data['date'] = date
            json_data['place'] = kaisai_place['kaisai']
            json_data['no'] = race['no']
            json_data['win'] = []
            race_no = str(race['no']).zfill(2)

            if 'win' in race :
                #print('  -- {}/{}/{}/{}'.format(date, kaisai_place['kaisai'], race['no'],'win'))

                pu.func_parser.s3_folder_check('tmp', date, kaisai_place['kaisai'], race_no, 'win')
                parser_win = prow.parser_odds_win('/JRADB/accessO.html', race['win'])
                odds_info = parser_win.parse()
                
                for uma_data in odds_info['odds']:
                    uma = {}
                    uma['name'] = uma_data['uma']['name']
                    uma['sexage'] = uma_data['sexage']
                    uma['odds'] = uma_data['odds']
                    json_data['win'].append(uma)

                if odds_info['fixed'] == True:
                    file_name = '9999999999.9'
                else:
                    file_name = odds_info['timestamp']

                #file_name = 'tmp/{}/{}/{}/{}/{}.json'.format(date, kaisai_place['kaisai'], race_no, 'win', file_name)
                pu.func_parser.s3_put_data('tmp', date, kaisai_place['kaisai'], race_no, 'win', file_name, json_data)
                #with open(file_name, 'w') as wfp:
                #    json.dump(json_data, wfp, ensure_ascii = False)

