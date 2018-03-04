from . import parser as pr
from . import parser_util as pu
from . import parser_post as prp
import re

class parser_race_kaisai(prp.parser_post):
    def parse_content(self, soup):
        ret = {}

        kaisai = soup.find("div",  attrs = {"class":"heading1Text"})
        date, weekday, kaisuu, place, day =  pu.parser_util_parse_kaisai(kaisai.get_text())

        ret['date'] = date
        ret['weekday'] = weekday
        ret['kaisuu'] = kaisuu
        ret['place'] = place
        ret['nichisuu'] = day

        races = soup.find_all("td", attrs = {"class":"racekekkaCol"})

        race_list = [{} for i in range(len(races))]
        ret['race_list'] = race_list 

        for race, race_ret in zip(races, race_list):
            anchors = race.find_all("a")
            for anchor in anchors:
              img = anchor.find("img")
              if img['class'][0] != "win5Image":
                params = pu.func_parser.parse_func_params(anchor['onclick'])
                race_ret['param'] = params[1]
                break

            #print("レース番号 : {}".format(int(img['alt'].replace('レース',''))))
            race_ret['number'] = int(img['alt'].replace('レース',''))
            tr = race.parent
            tds = tr.find_all('td')
            for td in tds :
                if td.has_attr('class'):
                    class_name = td['class']
                    if 'kyousouCol' in class_name:
                        #print("レース名 : {}".format(td.get_text()))
                        race_ret['name'] = td.get_text().strip()
                    elif 'kyoriCol' in class_name:
                        #print("距離 : {}".format(int(td.get_text().replace('m',''))))
                        race_ret['distance'] = int(td.get_text().replace('m',''))
                    elif 'babaCol' in class_name:
                        #print("コース : {}".format(td.get_text()))
                        race_ret['course'] = td.get_text()
                    elif 'tousuCol' in class_name:
                        uma_num = td.get_text().replace('頭','')
                        if uma_num != "":
                          #print("頭数 : {}".format(int(uma_num)))
                          race_ret['uma_num'] = int(uma_num)

        return ret



