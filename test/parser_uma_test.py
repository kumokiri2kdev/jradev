import sys

sys.path.append('../')

from jra import parser_uma as pu

#pcode = 'pw01dud002014106046/0F'
pcode = 'pw01dud002010110078/29'

_parser = pu.parser_uma('/JRADB/accessU.html',pcode)

info =  _parser.parse()

print(info)

