from . import parser as pr
from . import parser_util as pu
from . import parser_post as prp
import re

def parse_kaisai(kaisai):
    kaisai = kaisai.strip()
    date = re.search(r'[0-9]{4}年[0-9]{1,2}月[0-9]{1,2}日', kaisai)
    weekday = re.search(r'（[土日]曜）', kaisai)
    kaisuu = re.search(r'[0-9]*回', kaisai)
    day = re.search(r'[0-9]*日$', kaisai)
    place = re.search(r'(東京|中山|京都|阪神|札幌|函館|新潟|福島|中京|小倉)', kaisai)

    return date[0], weekday[0], int(kaisuu[0].replace("回","")), place[0], int(day[0].replace("日",""))
class parser_race_kaisai(prp.parser_post):
    def parse_content(self, soup):
        ret = {}

        kaisai = soup.find("div",  attrs = {"class":"heading1Text"})
        date, weekday, kaisuu, place, day =  parse_kaisai(kaisai.get_text())
        print(weekday)
        print(kaisuu)
        print(place)
        print(day)

        ret['date'] = date
        ret['weekday'] = weekday
        ret['kaisuu'] = kaisuu
        ret['place'] = place
        ret['nichisuu'] = day

        races = soup.find_all("td", attrs = {"class":"racekekkaCol"})

        race_list = [{} for i in range(len(races))]
        ret['race_list'] = race_list 

        for race, race_ret in zip(races, race_list):
            anchor = race.find("a")
            params = pu.func_parser.parse_func_params(anchor['onclick'])
            print(params)
            race_ret['param'] = params[1]
            img = race.find("img")
            print("レース番号 : {}".format(int(img['alt'].replace('レース',''))))
            race_ret['number'] = int(img['alt'].replace('レース',''))
            tr = race.parent
            tds = tr.find_all('td')
            for td in tds :
                if td.has_attr('class'):
                    class_name = td['class']
                    if 'kyousouCol' in class_name:
                        print("レース名 : {}".format(td.get_text()))
                        race_ret['name'] = td.get_text().strip()
                    elif 'kyoriCol' in class_name:
                        print("距離 : {}".format(int(td.get_text().replace('m',''))))
                        race_ret['distance'] = int(td.get_text().replace('m',''))
                    elif 'babaCol' in class_name:
                        print("コース : {}".format(td.get_text()))
                        race_ret['course'] = td.get_text()
                    elif 'tousuCol' in class_name:
                        print("頭数 : {}".format(int(td.get_text().replace('頭',''))))
                        race_ret['uma_num'] = int(td.get_text().replace('頭',''))

        return ret



