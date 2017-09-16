import sys

sys.path.append('../')

from jra import parser_top as pr
from jra import parser_odds_top as prot
from jra import parser_odds_kaisai as prok
from jra import parser_odds_win as prow

use_network = True

_parser = prok.parser_odds_kaisai('/JRADB/accessO.html', 'pw15orl00062017040320170916/CE')

if use_network:
    list = _parser.parse()
else:
    args = sys.argv

    if len(args) < 2:
        print("Specify Test File Name")
        sys.exit()

    with open(args[1],'rb') as rfp:
        response_body = rfp.read().decode("'shift_jis'")
        list = _parser.parse_html(response_body)

for race in list:
    print("レース : {}".format(race['no']))
    print(" 発走 : {}".format(race['status']))
    if 'name' in race:
        print(" レース名 : {}".format(race['name']))

    print(" 条件 : {}".format(race['condition']))

    print(" 単勝 : {}".format(race['win']))
    if 'waku' in race:
        print(" 枠連 : {}".format(race['waku']))
    print(" 馬連 : {}".format(race['uma']))
    print(" 馬単 : {}".format(race['exacta']))
    print(" ワイド : {}".format(race['wide']))
    print(" 三連複 : {}".format(race['trio']))
    print(" 三連単 : {}".format(race['trioexacta']))


