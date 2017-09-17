from . import parser as pr
from . import parser_odds_waku as prow


class parser_odds_exacta(prow.parser_odds_waku):
    def configure(self):
        self.table_tag1 = 'ozUmatanUmaOutTable'
        self.table_tag2 = 'ozUmatanUmaINTable' 
        self.json_tag = 'exacta'
