from . import parser as pr
from . import parser_util as pu
from . import parser_post as prp
import re

class parser_win5_kaisai(prp.parser_post):
    def parse_content(self, soup):
        anchors = soup.find_all("a", attrs = {"href":"#"})
        ret = {}

        for anchor in anchors:
            text = anchor.get_text()
            if re.search(r"[0-9]{4}年[0-9]*月[0-9]*日.*→", text) != None:
                print(text)
                params = pu.func_parser.parse_func_params(anchor['onclick'])
                ret['next'] = params[1]
            elif re.search(r"←[0-9]{4}年[0-9]*月[0-9]*日", text) != None:
                print(text)
                params = pu.func_parser.parse_func_params(anchor['onclick'])
                ret['prev'] = params[1]

        win5lists = soup.find_all("table", attrs = {"class":"win5List"})

        print(len(win5lists))
        return ret
