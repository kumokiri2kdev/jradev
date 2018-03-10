import sys
sys.path.append('../')

from jra import parser_win5_kaisai as prwk
from jra import parser_util as pu
import re


param = 'pw17hde01201104241/18'

while True:
    pu.parser_util_cache_contents('/access5.html', param)
    _parser = prwk.parser_win5_kaisai('/JRADB/access5.html',param)
    win5 = _parser.parse()
    if win5 == None:
        break;

    if ('next' in win5 == False):
        break

    print(win5['date'])
    param = win5['next']
