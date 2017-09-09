import parser_top as pr
import sys

args = sys.argv

if len(args) < 2:
    print("Specify Test File Name")
    sys.exit()

_parser = pr.parser_top()


with open(args[1],'rb') as rfp:
	response_body = rfp.read().decode("'shift_jis'")
	_parser.parse(response_body)