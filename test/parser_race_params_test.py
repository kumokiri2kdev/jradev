import sys

sys.path.append('../')

from jra import parser_race_params as prp

year = 2000
month = 1

while True:
  param = year * 100 + month
  print(prp.parser_race_params_get_cname(param))
  month +=1
  if month > 12:
    year += 1
    month = 1
    if year > 2018:
      break;
  