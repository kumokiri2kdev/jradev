import sys

sys.path.append('../')

from jra import parser_top as pr
from jra import parser_odds_top as prot
from jra import parser_odds_kaisai as prok
from jra import parser_odds_win as prow

parser_top = pr.parser_top()
param_list = parser_top.parse()

if 'odds' in param_list == False:
    print("No odd param")
    sys.exit()

parser_odds_top = prot.parser_odds_top('/JRADB/accessO.html', param_list['odds'])
kaisai_list = parser_odds_top.parse()

for kaisai in kaisai_list:
    print("日付 : {}".format(kaisai['date']))
    kaisai_place_list = kaisai['kaisai_list']
    for kaisai_place in kaisai_place_list:
        print(" - 開催 : {}".format(kaisai_place['kaisai']))
        parser_odds_kaisai = prok.parser_odds_kaisai('/JRADB/accessO.html', kaisai_place['param'])
        race_list = parser_odds_kaisai.parse()
        for race in race_list:
            print("  -- {} {}".format(race['no'], race['condition']))
            parser_win = prow.parser_odds_win('/JRADB/accessO.html', race['win'])
            odds_info = parser_win.parse()
            if odds_info['fixed'] == True:
                print("最終オッズ")
            else:
                print("{} 現在のオッズ()".format(odds_info['timestamp'] ))

            uma_list =  odds_info['odds']
            for uma_data in uma_list:
                print("   [{}]{} {} {} ({} - {})".format(uma_data['number'], uma_data['uma']['name'], 
                                                                    uma_data['sexage'], uma_data['odds']['win'],
                                                                    uma_data['odds']['fuku_min'], uma_data['odds']['fuku_max']))


        