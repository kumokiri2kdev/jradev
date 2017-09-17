from . import parser as pr
from . import parser_odds_waku as prow


class parser_odds_uma(prow.parser_odds_waku):
    def configure(self):
        self.table_tag1 = 'ozUmarenUmaOutTable'
        self.table_tag2 = 'ozUmarenUmaINTable' 
        self.json_tag = 'uma'   


