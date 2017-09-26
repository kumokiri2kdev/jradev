import sys
import json
from datetime import datetime
import time

sys.path.append('../')

from jra import parser_util as pu
from jra import parser_top as pr
from jra import parser_odds_top as prot
from jra import parser_odds_kaisai as prok
from jra import parser_odds_win as prow
from jra import parser_odds_waku as prowk
from jra import parser_odds_uma as prou
from jra import parser_odds_exacta as proe
from jra import parser_odds_wide as prowi
from jra import parser_odds_trio as protr
from jra import parser_odds_trioexacta as prote

def parser_factory(code, category):
    if category == 'waku':
        return prowk.parser_odds_waku('/JRADB/accessO.html', code)
    elif category == 'uma':
        return prou.parser_odds_uma('/JRADB/accessO.html', code)
    elif category == 'exacta':
        return proe.parser_odds_exacta('/JRADB/accessO.html', code)
    elif category == 'wide':
        return prowi.parser_odds_wide('/JRADB/accessO.html', code)
    elif category == 'trio':
        return protr.parser_odds_trio('/JRADB/accessO.html', code)
    elif category == 'trioexacta':
        return prote.parser_odds_trioexacta('/JRADB/accessO.html', code)

def upload_win(json_data, date, kaisai, race_no, code):
    if pu.func_parser.final_odds_exist('tmp', date, kaisai, race_no, 'win') == True :
        return

    pu.func_parser.folder_check('tmp', date, kaisai, race_no, 'win')
    parser_win = prow.parser_odds_win('/JRADB/accessO.html', code)
    odds_info = parser_win.parse()
    json_data['odds'] = []
    json_data['category'] = 'win'

    for uma_data in odds_info['odds']:
        uma = {}
        uma['name'] = uma_data['uma']['name']
        uma['sexage'] = uma_data['sexage']
        uma['odds'] = uma_data['odds']
        json_data['odds'].append(uma)

    if odds_info['fixed'] == True:
        file_name = '9999999999.9'
    else:
        file_name = odds_info['timestamp']
        json_data['category'] = odds_info['timestamp']

    pu.func_parser.put_data('tmp', date, kaisai_place['kaisai'], race_no, 'win', file_name, json_data)

def upload_odds(json_data, date, kaisai, race_no, code, category):
    if pu.func_parser.final_odds_exist('tmp', date, kaisai, race_no, category) == True :
        return

    pu.func_parser.folder_check('tmp', date, kaisai, race_no, category)

    parser  = parser_factory(code, category)

    odds_info = parser.parse()
    json_data['odds'] = odds_info['odds']
    json_data['category'] = category

    if odds_info['fixed'] == True:
        file_name = '9999999999.9'
    else:
        file_name = odds_info['timestamp']
        json_data['category'] = odds_info['timestamp']

    pu.func_parser.put_data('tmp', date, kaisai_place['kaisai'], race_no, category, file_name, json_data)


start = datetime.now()

parser_top = pr.parser_top()
param_list = parser_top.parse()

parser_odds_top = prot.parser_odds_top('/JRADB/accessO.html', param_list['odds'])
kaisai_list = parser_odds_top.parse()

for kaisai in kaisai_list:
    date = pu.parser_util_convert_datestr(kaisai['date'])

    kaisai_place_list = kaisai['kaisai_list']
    for kaisai_place in kaisai_place_list:
        parser_odds_kaisai = prok.parser_odds_kaisai('/JRADB/accessO.html', kaisai_place['param'])
        race_list = parser_odds_kaisai.parse()
        for race in race_list:
            json_data = {}
            json_data['date'] = date
            json_data['place'] = kaisai_place['kaisai']
            json_data['no'] = race['no']
            json_data['odds'] = []
            race_no = str(race['no']).zfill(2)

            if 'win' in race:
                upload_win(json_data, date, kaisai_place['kaisai'], race_no, race['win'])

            if 'waku' in race:
                upload_odds(json_data, date,  kaisai_place['kaisai'], race_no, race['waku'], 'waku')

            if 'uma' in race:
                upload_odds(json_data, date,  kaisai_place['kaisai'], race_no, race['uma'], 'uma')

            if 'exacta' in race:
                upload_odds(json_data, date,  kaisai_place['kaisai'], race_no, race['exacta'], 'exacta')

            if 'wide' in race:
                upload_odds(json_data, date,  kaisai_place['kaisai'], race_no, race['wide'], 'wide')

            if 'trio' in race:
                upload_odds(json_data, date,  kaisai_place['kaisai'], race_no, race['trio'], 'trio')

            if 'trioexacta' in race:
                upload_odds(json_data, date,  kaisai_place['kaisai'], race_no, race['trioexacta'], 'trioexacta')


end = datetime.now()

print("{}".format(end.timestamp() - start.timestamp()))

