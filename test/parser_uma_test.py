import sys
import json

sys.path.append('../')

from jra import parser_uma as pu

#pcode = 'pw01dud002014106046/0F'
#pcode = 'pw01dud002010110078/29'
#pcode = 'pw01dud002011105960/A3'
pcode = 'pw01dud002014100833/94'

_parser = pu.parser_uma('/JRADB/accessU.html',pcode)

info =  _parser.parse()

print(info['basic']['name'])

races = info['races']

for race in races:
    print(race['date'])

with open ('test.json', 'w') as wfp:
    json.dump(info, wfp, ensure_ascii=False)

