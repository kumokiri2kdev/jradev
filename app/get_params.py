import sys

sys.path.append('../')

from jra import parser_top as pr
from jra import parser_odds_top as prot
from jra import parser_odds_kaisai as prok

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
        print("  {}".format(kaisai_place['param']))
        race_list = parser_odds_kaisai.parse()
        for race in race_list:
            print("  -- {} {}".format(race['no'], race['condition']))
            if 'win' in race:
                print("    -- 単勝 : {}".format(race['win']))
            if 'waku' in race:
                print("    -- 枠連 : {}".format(race['waku']))
            if 'uma' in race:
                print("    -- 馬蓮 : {}".format(race['uma']))
            if 'exacta' in race:
                print("    -- 馬単 : {}".format(race['exacta']))
            if 'wide' in race:
                print("    -- ワイド : {}".format(race['wide']))
            if 'trio' in race:
                print("    -- 三連複 : {}".format(race['trio']))
            if 'trioexacta' in race:
                print("    -- 三連単 : {}".format(race['trioexacta']))
