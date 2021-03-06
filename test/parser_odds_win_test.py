import sys

sys.path.append('../')

from jra import parser_top as pr
from jra import parser_odds_top as prot
from jra import parser_odds_kaisai as prok
from jra import parser_odds_win as prow

use_network = True

_parser = prow.parser_odds_win('/JRADB/accessO.html', 'pw151ouS306201704071120170924Z/64')

if use_network:
    odds_info = _parser.parse()
else:
    args = sys.argv

    if len(args) < 2:
        print("Specify Test File Name")
        sys.exit()

    with open(args[1],'rb') as rfp:
        response_body = rfp.read().decode("'shift_jis'")
        odds_info = _parser.parse_html(response_body)

uma_list =  odds_info['odds']

if odds_info['fixed'] == True:
    print("最終オッズ")
else:
    print("{} 現在のオッズ()".format(odds_info['timestamp'] ))

for uma_data in uma_list:
    print("[{}]{} {}".format(uma_data['number'], uma_data['uma']['name'], uma_data['sexage']))
    print("  url : {}".format(uma_data['uma']['url']))
    print("  param : {}".format(uma_data['uma']['param']))
    print(" 単勝 : {}, 複勝 : {} - {}".format(uma_data['odds']['win'], uma_data['odds']['fuku_min'], uma_data['odds']['fuku_max']))
    if 'weight' in uma_data:
        print(" 馬体重 : {}".format(uma_data['weight']))
        print(" 増減 : {}".format(uma_data['diff']))

    print(" {} {}".format(uma_data['jokey']['name'], uma_data['sexage']))
    print("    url : {}".format(uma_data['jokey']['url']))
    print("    param : {}".format(uma_data['jokey']['param']))
    print(" {} {}".format(uma_data['stable']['name'], uma_data['sexage']))
    print("    url : {}".format(uma_data['stable']['url']))
    print("    param : {}".format(uma_data['stable']['param']))

print(odds_info)
