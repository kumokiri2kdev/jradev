import sys

sys.path.append('../')

from jra import parser_win5_kaisai as prwk

use_network = True
param = 'pw17hde01201104241/18'
#param = 'pw17hde01201105011/75'

while True:
    _parser = prwk.parser_win5_kaisai('/JRADB/access5.html',param)

    if use_network:
        kaisai = _parser.parse()
    else:
        args = sys.argv

        if len(args) < 2:
            print("Specify Test File Name")
            sys.exit()

        with open(args[1],'rb') as rfp:
            response_body = rfp.read().decode("'shift_jis'")
            kaisai = _parser.parse_html(response_body)


    if param == None:
        break

    print(kaisai)

    if "next" in kaisai:
        param = kaisai['next']
    else:
        break

