from . import parser as pr
from . import parser_util as pu
from . import parser_post as prp
import re

def parse_win5list_0(win5list, ret):
    trs = win5list.find_all("tr")
    for tr in trs:
        th = tr.find("th")
        if th != None and th.get_text() == "キャリーオーバー！":
            td = tr.find("td")
            if td != None:
                try :
                    ret['carry_over'] = int(td.get_text().replace("円","").replace(",",""))
                except:
                    pass


def parse_win5list_1(win5list, ret):
    trs = win5list.find_all("tr")
    for tr in trs:
        th = tr.find("th")
        if th != None:
            tag = th.get_text()
            if "発売票数" in tag:
                td = tr.find("td")
                if td != None:
                    ret['bets'] = int(td.get_text().replace("票","").replace(",",""))
            elif "発売金額" in tag:
                td = tr.find("td")
                if td != None:
                    ret['bet_price'] = int(td.get_text().replace("円","").replace(",",""))

def race_index_filter(element):
    return int(element.get_text().replace("レース目",""))

def race_departurer_filter(element):
    return element.get_text().strip()

def race_race_filter(element):
    text = element.get_text().strip()

    race_info = text.split("\n")
    ret = {}
    ret['id'] = race_info[0]
    ret['name'] = race_info[1]
    
    anchor = element.find("a")
    params = pu.func_parser.parse_func_params(anchor['onclick'])

    ret['param'] = params[1]

    return ret

def race_ninki_filter(element):
    return int(element.get_text().strip().replace("番人気",""))

def race_remaining_filter(element):
    return int(element.get_text().strip().replace("票","").replace(",",""))

def parse_win5list_2(win5list, ret):
    trs = win5list.find_all("tr")

    ret['list'] = [{} for i in range(5)]
    for i,tr in enumerate(trs):
        th = tr.find("th")
        if th:
            th_tag = th.get_text()
            if th_tag in " ":
                json_tag = "index"
                filter_func = race_index_filter
                siblings = th.find_next_siblings("th")
            elif th_tag in "発走時刻":
                json_tag = "departure"
                filter_func = race_departurer_filter
                siblings = th.find_next_siblings("th")
            elif th_tag in "レース":
                json_tag = "race"
                filter_func = race_race_filter
                siblings = th.find_next_siblings("th")
            elif th_tag in "残り票数":
                json_tag = "remaining"
                filter_func = race_remaining_filter
                siblings = th.find_next_siblings("td")
            elif th_tag in "単勝人気":
                json_tag = "ninki"
                filter_func = race_ninki_filter
                siblings = th.find_next_siblings("td")
            else:
                continue

            for i,sibling in enumerate(siblings):
                ret['list'][i][json_tag] = filter_func(sibling)

def parse_win5list_3(win5list, ret):
    trs = win5list.find_all("tr")

    for tr in trs:
        th = tr.find("th")
        if th != None:
            tag = th.get_text()
            if "的中馬番" in tag:
                td = tr.find("td")
                if td != None:
                    ret['indexes'] = td.get_text().strip()
            elif "払戻金" in tag:
                td = tr.find("td")
                if td != None:
                    try :
                        ret['pay_back'] = int(td.get_text().replace("円","").replace(",",""))
                    except:
                        pass
            elif "的中票数" in tag:
                td = tr.find("td")
                if td != None:
                    ret['remaining'] = int(td.get_text().replace("票","").replace(",",""))

class parser_win5_kaisai(prp.parser_post):
    def parse_win5list_0(win5list):
        pass

    def parse_content(self, soup):
        ret = {}

        date_str = soup.find("td", attrs={"class":"header3"})
        if date_str != None:
          date, weekday = pu.parser_util_parse_date(date_str.get_text())
          ret['date']  = date
          ret['weekday'] = weekday

        anchors = soup.find_all("a", attrs = {"href":"#"})
        for anchor in anchors:
            text = anchor.get_text()
            if re.search(r"[0-9]{4}年[0-9]*月[0-9]*日.*→", text) != None:
                params = pu.func_parser.parse_func_params(anchor['onclick'])
                ret['next'] = params[1]
            elif re.search(r"←[0-9]{4}年[0-9]*月[0-9]*日", text) != None:
                params = pu.func_parser.parse_func_params(anchor['onclick'])
                ret['prev'] = params[1]

        win5lists = soup.find_all("table", attrs = {"class":"win5List"})
        win5list_parse_funcs = [parse_win5list_0, parse_win5list_1, parse_win5list_2, parse_win5list_3]

        for func, list in zip(win5list_parse_funcs, win5lists):
            func(list, ret)

        return ret
