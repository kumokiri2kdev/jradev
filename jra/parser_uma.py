from . import parser as pr
from . import parser_post as prp
from . import parser_util as pu

class parser_uma(prp.parser_post):
    
    def filter_tables(self, tbls):
        ret_tbls = {}

        for tbl in tbls:
            td = tbl.find('td')
            if td:
                tag = pu.func_parser.trim_clean(td.get_text())
                print(tag)
                if tag == '【出走レース】':
                    ret_tbls['races'] = tbl
            

        return ret_tbls

    def parse_races(self, races):
        trs = races.find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            
            print(tds[0].get_text())
        
    def parse_content(self, soup):
        print("uma parser")
        tbls = soup.find_all("table")
        filtered_tbls = self.filter_tables(tbls)

        if 'races' in filtered_tbls:
            #print(filtered_tbls['races'].get_text())
            self.parse_races(filtered_tbls['races'])
            
