from . import parser as pr
from . import parser_post as prp


class parser_odds_uma(prp.parser_post):
    def sort_list(self, list, key):
        for i in range(0, len(list)):
            j = len(list) - 1
            while j > i:
                if list[j][key] < list[j-1][key]:
                    tmp = list[j-1]
                    list[j-1] = list[j]
                    list[j] = tmp
                j = j - 1

        return list

    def parse_content(self, soup):
        umas = soup.find("table", attrs = {"class":"ozUmarenUmaOutTable"})

        uma_tables = umas.find_all("table", attrs = {"class":"ozUmarenUmaINTable"})

        uma_list = [{} for i in range(len(uma_tables))]

        for i, uma_table in enumerate(uma_tables):
            entry = uma_list[i]
            tr = uma_table.find('tr')
            th = tr.find('th')
            entry['uma'] = pr.func_parser.get_number(th.get_text())

            trs =  tr.find_next_siblings('tr')
            entry['matrix'] = [{} for i in range(len(trs))]
            for i, tr in enumerate(trs) :
                matrix = entry['matrix'][i]
                th = tr.find('th')
                td = tr.find('td')
                #print(" {} : {}".format(th.get_text(), td.get_text()))
                odds = td.get_text()
                matrix['uma'] = pr.func_parser.get_number(th.get_text())
                if odds != '':
                    try :
                        matrix['odds'] = pr.func_parser.get_float(odds)
                    except:
                        if odds == '取消':
                            pass

        uma_list = self.sort_list(uma_list, 'uma')

        return uma_list


