import sys

sys.path.append('../')

from jra import parser_top as pr
from jra import parser_odds_top as prot
from jra import parser_odds_kaisai as prok
from jra import parser_odds_waku as prow

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
            if 'waku' in race:
                parser_waku = prow.parser_odds_waku('/JRADB/accessO.html', race['waku'])
                odds_info =  parser_waku.parse()
                if odds_info['fixed'] == True:
                    print("最終オッズ")
                else:
                    print("{} 現在のオッズ()".format(odds_info['timestamp'] ))

                waku_list =  odds_info['odds']
                for waku in waku_list:
                    print("枠番 : {}".format(waku['number']))
                    for matrix in waku['matrix']:
                        if 'odds' in matrix:
                            print(" - {} : {}".format(matrix['number'], matrix['odds']))
                        else:
                            print(" - {} : 発売なし".format(matrix['number']))
            else :
                print("枠連発売なし")
        