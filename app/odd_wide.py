import sys

sys.path.append('../')

from jra import parser_top as pr
from jra import parser_odds_top as prot
from jra import parser_odds_kaisai as prok
from jra import parser_odds_wide as umw

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
            if 'wide' in race:
                parser_uma = umw.parser_odds_wide('/JRADB/accessO.html', race['wide'])
                uma_list =  parser_uma.parse()
                for uma in uma_list:
                    print("馬番 : {}".format(uma['wide']))
                    for matrix in uma['matrix']:
                        if 'odds_min' in matrix:
                            print(" - {} : {} - {}".format(matrix['wide'], matrix['odds_min'], matrix['odds_max']))
                        else:
                            print(" - {} : 発売なし".format(matrix['wide']))
            else :
                print("ワイド発売なし")
        