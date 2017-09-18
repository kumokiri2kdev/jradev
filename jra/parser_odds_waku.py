from . import parser as pr
from . import parser_post as prp


class parser_odds_waku(prp.parser_post):
    def __init__(self, path, param):
        super(parser_odds_waku, self).__init__(path, param)
        self.configure()

    def configure(self):
        self.table_tag1 = 'ozWakuOutTable'
        self.table_tag2 = 'ozWakuINTable'   

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

    def parse_odds(self, matrix, tr):
        td = tr.find('td')
        odds = td.get_text()
        if odds != '':
            try :
                matrix['odds'] = pr.func_parser.get_float(odds)
            except:
                if odds == '取消':
                    pass


    def parse_content(self, soup):
        odds = soup.find("table", attrs = {'class' : self.table_tag1})

        odds_tables = odds.find_all("table", attrs = {'class' : self.table_tag2})

        odds_list = [{} for i in range(len(odds_tables))]

        for i, odds_table in enumerate(odds_tables):
            entry = odds_list[i]
            tr = odds_table.find('tr')
            th = tr.find('th')
            entry['number'] = pr.func_parser.get_number(th.get_text())

            trs =  tr.find_next_siblings('tr')
            entry['matrix'] = [{} for i in range(len(trs))]
            for i, tr in enumerate(trs) :
                matrix = entry['matrix'][i]
                th = tr.find('th')
                matrix['number'] = pr.func_parser.get_number(th.get_text())

                self.parse_odds(matrix, tr)

        odds_list = self.sort_list(odds_list, 'number')

        return odds_list


