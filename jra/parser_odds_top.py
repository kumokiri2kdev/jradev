from . import parser as pr
from . import parser_post as prp
import re

class parser_odds_top(prp.parser_post):
    def parse_content(self, soup):
        areas = soup.find_all("div", attrs = {"class":"joSelectArea"})

        kaisai_list = []

        for area in areas:
            th = area.find('th')
            if th :
                date = pr.func_parser.trim_clean(th.get_text())
                date = re.sub(r'（.*）',"", date)
                #print(date)
                kaisai = {}
                kaisai['date'] = date
                kaisai_list.append(kaisai)
            else:
                continue

            buttons = area.find_all("td", attrs = {"class":"kaisaiBtn"})
            kaisais = [{} for i in range(len(buttons))] 
            kaisai['kaisai_list'] = kaisais
            for i, button in enumerate(buttons) :
                anchor = button.find("a")
                params = pr.func_parser.parse_func_params(anchor['onclick'])
                #print(params)
                kaisai_id = pr.func_parser.trim_clean(anchor.get_text())
                #print(kaisai_id)
                kaisais[i]['kaisai'] = kaisai_id
                kaisais[i]['param'] = params[1]

        return kaisai_list