import sys

sys.path.append('../')

from jra import parser as pr
from jra import parser_util as pu
from jra import parser_top as pt
from jra import parser_odds_top as prot
from jra import parser_odds_kaisai as prok

parser_top = pt.parser_top()
param_list = parser_top.parse()

parser_odds_top = prot.parser_odds_top('/JRADB/accessO.html', param_list['odds'])
kaisai_list = parser_odds_top.parse()

for kaisai in kaisai_list:
    print("日付 : {}".format(kaisai['date']))
    converted = pu.parser_util_convert_datestr(kaisai['date'])
    pr.func_parser.s3_folder_check(converted)



