import parser_top as pr

_parser = pr.parser_top()


with open('jra_top.html','rb') as rfp:
	response_body = rfp.read().decode("'shift_jis'")
	_parser.parse(response_body)