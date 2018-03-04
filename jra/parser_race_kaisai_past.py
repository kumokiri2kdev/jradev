from . import parser as pr
from . import parser_util as pu
from . import parser_post as prp
import re

class parser_race_kaisai_past(prp.parser_post):
    def parse_content(self, soup):
      ret = {}
      ret['kaisai'] = []
      kaisais = soup.find_all("td", attrs = {"class":"kaisaiBtn"})

      for kaisai in kaisais:
        anchor = kaisai.find("a")
        if anchor:
          params = pu.func_parser.parse_func_params(anchor['onclick'])
          ret['kaisai'].append({'param': params[1]}) 

      return ret
