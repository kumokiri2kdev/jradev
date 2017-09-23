from . import parser as pr
from . import parser_util as pu
from . import parser_post as prp

class parser_odds(prp.parser_post):

    def parse_content(self, soup):
        fixed = True
        div = soup.find('div', attrs={'class' : 'raceTtlTable'})
        if div:
            spans = div.find_all('span')
            for span in spans:
                if span.has_attr('class'):
                    if 'headerOdds2' in span['class']:
                        value = span.get_text()
                        if "現在" in value:
                            try:
                                time_value = pu.func_parser.parse_time(value)
                                full, stamp = pu.parser_util_convert_timestr_full_and_stamp(time_value)
                                fixed = False
                            except:
                                print("ValueError : {}".format(value))
                                pass
                        else:
                            print("最終オッズ")
                    else:
                        print("最終オッズ")
        
        if fixed == False:
            print("{} 現在のオッズ({})".format(time_value, full))            

        return self.parse_odds_content(soup)
