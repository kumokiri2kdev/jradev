import sys

sys.path.append('../')

from jra import parser_top as pr

use_network = True

_parser = pr.parser_top()

if use_network:
    param_list = _parser.parse()
else:
    args = sys.argv

    if len(args) < 2:
        print("Specify Test File Name")
        sys.exit()

    with open(args[1],'rb') as rfp:
        response_body = rfp.read().decode("'shift_jis'")
        param_list = _parser.parse_html(response_body)

print(param_list)

if 'odds' in param_list:
    print("オッズ : {}".format(param_list['odds']))
