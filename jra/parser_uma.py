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
                #print(tag)
                if tag == '【出走レース】':
                    ret_tbls['races'] = tbl
                elif tag == '【プロフィール】':
                    ret_tbls['profile'] = tbl
            

        return ret_tbls

    def parse_races(self, races):
        tags = ['date', 'place','name','distance','condition','number','ninki','rank','jokey','hande','weight','time','winner']

        trs = races.find_all('tr')
        ret = []

        for tr in trs:
            if tr.has_attr('class') and 'gray12_h' in tr['class']:
                continue

            ret_race = {}
            tds = tr.find_all('td')
            
            for tag, td in zip(tags,tds):
                #print(pu.func_parser.trim_clean(td.get_text()))
                ret_race[tag] = pu.func_parser.trim_clean(td.get_text())
               
            ret.append(ret_race)

        return ret

    def parse_profile(self, profile):
        #print(profile)
        trs = profile.find_all('tr')
        ret_profile = {}

        for tr in trs:
            tds = tr.find_all('td')

            for i in range(0, len(tds) - len(tds) % 2, 2):
                if len(tds) > i:
                    tag = pu.func_parser.trim_clean(tds[i].get_text())
                if len(tds) > (i + 1):
                    value = pu.func_parser.trim_clean(tds[i + 1].get_text())
               
                if 'tag' in locals() and 'value'  in locals():
                    ret_profile[tag] = value
                    del(tag)
                    del(value)

        return ret_profile


    def parse_content(self, soup):
        print("uma parser")
        tbls = soup.find_all("table")
        filtered_tbls = self.filter_tables(tbls)

        parsed_data = {}

        if 'races' in filtered_tbls:
            #print(filtered_tbls['races'].get_text())
            parsed_race = self.parse_races(filtered_tbls['races'])
        if 'profile' in filtered_tbls:
            parsed_profile = self.parse_profile(filtered_tbls['profile'])

        parsed_data['profile'] = parsed_profile
        parsed_data['races'] = parsed_race

        return parsed_data

