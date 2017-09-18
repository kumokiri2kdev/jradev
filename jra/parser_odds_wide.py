from . import parser as pr
from . import parser_odds_waku as prow


class parser_odds_wide(prow.parser_odds_waku):
    def configure(self):
        self.table_tag1 = 'ozWideUmaOutTable'
        self.table_tag2 = 'ozWideUmaINTable' 

    def parse_odds(self, matrix, tr):
        tds = tr.find_all('td')
        if len(tds) < 3:
            return

        odds_min = tds[0].get_text()
        if odds_min != '':
            try :
                matrix['odds_min'] = pr.func_parser.get_float(odds_min)
            except:
                if odds == '取消':
                    pass

        odds_max = tds[2].get_text()
        if odds_max != '':
            try :
                matrix['odds_max'] = pr.func_parser.get_float(odds_max)
            except:
                if odds == '取消':
                    pass
