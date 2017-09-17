from . import parser as pr
from . import parser_post as prp


class parser_odds_waku(prp.parser_post):
    def parse_content(self, soup):
        wakus = soup.find("table", attrs = {"class":"ozWakuOutTable"})

        waku_tables = wakus.find_all("table", attrs = {"class":"ozWakuINTable"})

        waku_list = [{} for i in range(len(waku_tables))]

        for i, waku_table in enumerate(waku_tables):
            entry = waku_list[i]
            tr = waku_table.find('tr')
            th = tr.find('th')
            entry['waku'] = pr.func_parser.get_number(th.get_text())

            trs =  tr.find_next_siblings('tr')
            entry['matrix'] = [{} for i in range(len(trs))]
            for i, tr in enumerate(trs) :
                matrix = entry['matrix'][i]
                th = tr.find('th')
                td = tr.find('td')
                #print(" {} : {}".format(th.get_text(), td.get_text()))
                odds = td.get_text()
                matrix['waku'] = pr.func_parser.get_number(th.get_text())
                if odds != '':
                    try :
                        matrix['odds'] = pr.func_parser.get_float(odds)
                    except:
                        if odds == '取消':
                            pass
            
        return waku_list


